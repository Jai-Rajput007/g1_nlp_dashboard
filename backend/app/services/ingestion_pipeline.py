"""Document ingestion pipeline with progress tracking and async processing."""

import os
import asyncio
from pathlib import Path
from typing import Optional, Callable, Dict, Any, List
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid

from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.document import Document, DocumentStatus
from app.models.activity import Activity, ActivityType
from app.services.document_loaders.loader_factory import load_document_from_bytes
from app.services.embedding_service import embedding_service
from app.services.vector_db_service import vector_db_service
from app.core.config import settings
from app.core.logging import logger
from app.core.exceptions import DocumentProcessingError


class IngestionStage(Enum):
    """Stages of document ingestion."""
    UPLOADED = "uploaded"
    EXTRACTING = "extracting"
    CHUNKING = "chunking"
    EMBEDDING = "embedding"
    INDEXING = "indexing"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class IngestionProgress:
    """Track ingestion progress."""
    document_id: int
    stage: IngestionStage
    progress_percent: float
    message: str
    details: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None
    started_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "document_id": self.document_id,
            "stage": self.stage.value,
            "progress_percent": self.progress_percent,
            "message": self.message,
            "details": self.details,
            "error": self.error,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }


# Global progress tracking
_progress_callbacks: Dict[int, List[Callable[[IngestionProgress], None]]] = {}
_current_progress: Dict[int, IngestionProgress] = {}


def register_progress_callback(document_id: int, callback: Callable[[IngestionProgress], None]):
    """Register callback for progress updates."""
    if document_id not in _progress_callbacks:
        _progress_callbacks[document_id] = []
    _progress_callbacks[document_id].append(callback)


def unregister_progress_callback(document_id: int, callback: Callable[[IngestionProgress], None]):
    """Unregister progress callback."""
    if document_id in _progress_callbacks:
        if callback in _progress_callbacks[document_id]:
            _progress_callbacks[document_id].remove(callback)


def _update_progress(progress: IngestionProgress):
    """Update progress and notify callbacks."""
    _current_progress[progress.document_id] = progress
    
    # Notify callbacks
    callbacks = _progress_callbacks.get(progress.document_id, [])
    for callback in callbacks:
        try:
            callback(progress)
        except Exception as e:
            logger.error(f"Progress callback error: {e}")
    
    # Log progress
    logger.info(f"Doc {progress.document_id}: {progress.stage.value} - {progress.progress_percent}%")


def get_progress(document_id: int) -> Optional[IngestionProgress]:
    """Get current progress for document."""
    return _current_progress.get(document_id)


class IngestionPipeline:
    """Document ingestion pipeline."""
    
    def __init__(self):
        self.embedding_service = embedding_service
        self.vector_db = vector_db_service
    
    async def process_document(
        self,
        document_id: int,
        file_content: bytes,
        filename: str,
        file_type: str,
        db: Session
    ) -> bool:
        """
        Process document through full ingestion pipeline.
        
        Stages:
        1. Extract content from document
        2. Chunk text into segments
        3. Generate embeddings
        4. Store in vector database
        5. Update document status
        """
        progress = IngestionProgress(
            document_id=document_id,
            stage=IngestionStage.UPLOADED,
            progress_percent=0,
            message="Starting ingestion..."
        )
        
        try:
            # Stage 1: Extract content
            await self._extract_content(progress, file_content, filename, file_type)
            
            # Stage 2: Chunk text
            chunks = await self._chunk_text(progress, progress.details.get("content", ""))
            
            if not chunks:
                raise DocumentProcessingError("No text chunks generated")
            
            # Stage 3: Generate embeddings
            embeddings = await self._generate_embeddings(progress, chunks)
            
            # Stage 4: Index in vector DB
            await self._index_document(progress, document_id, chunks, embeddings, filename)
            
            # Stage 5: Update document status
            await self._finalize_document(progress, document_id, len(chunks), db)
            
            return True
            
        except Exception as e:
            logger.error(f"Ingestion failed for doc {document_id}: {e}")
            await self._handle_failure(progress, document_id, str(e), db)
            return False
    
    async def _extract_content(
        self,
        progress: IngestionProgress,
        file_content: bytes,
        filename: str,
        file_type: str
    ) -> None:
        """Extract content from document."""
        progress.stage = IngestionStage.EXTRACTING
        progress.progress_percent = 10
        progress.message = "Extracting document content..."
        _update_progress(progress)
        
        # Run extraction in thread pool
        loop = asyncio.get_event_loop()
        doc_content = await loop.run_in_executor(
            None,
            lambda: load_document_from_bytes(file_content, filename, file_type)
        )
        
        full_text = doc_content.to_text()
        
        progress.details.update({
            "content": full_text,
            "elements_count": len(doc_content.elements),
            "headings": [h.to_text() for h in doc_content.get_headings()[:10]],
            "tables_count": len(doc_content.get_tables()),
            "images_count": len(doc_content.get_images()),
            "lists_count": len(doc_content.get_lists()),
        })
        
        progress.progress_percent = 25
        progress.message = f"Extracted {len(full_text)} characters, {len(doc_content.elements)} elements"
        _update_progress(progress)
    
    async def _chunk_text(self, progress: IngestionProgress, text: str) -> List[str]:
        """Chunk text into segments."""
        progress.stage = IngestionStage.CHUNKING
        progress.progress_percent = 30
        progress.message = "Chunking text..."
        _update_progress(progress)
        
        from app.services.document_loaders.base import DocumentContent
        
        # Create temporary DocumentContent for chunking
        temp_doc = DocumentContent(
            elements=[],
            raw_text=text
        )
        
        # Get chunks
        chunks = temp_doc.get_text_chunks(
            chunk_size=settings.CHUNK_SIZE,
            overlap=settings.CHUNK_OVERLAP
        )
        
        progress.details["chunks_count"] = len(chunks)
        progress.progress_percent = 40
        progress.message = f"Created {len(chunks)} chunks"
        _update_progress(progress)
        
        return chunks
    
    async def _generate_embeddings(
        self,
        progress: IngestionProgress,
        chunks: List[str]
    ) -> List[List[float]]:
        """Generate embeddings for chunks."""
        progress.stage = IngestionStage.EMBEDDING
        progress.progress_percent = 45
        progress.message = "Generating embeddings..."
        _update_progress(progress)
        
        # Generate embeddings in batches
        loop = asyncio.get_event_loop()
        embeddings = await loop.run_in_executor(
            None,
            lambda: self.embedding_service.embed_documents(chunks)
        )
        
        progress.details["embeddings_count"] = len(embeddings)
        progress.progress_percent = 70
        progress.message = f"Generated {len(embeddings)} embeddings"
        _update_progress(progress)
        
        return embeddings
    
    async def _index_document(
        self,
        progress: IngestionProgress,
        document_id: int,
        chunks: List[str],
        embeddings: List[List[float]],
        filename: str
    ) -> None:
        """Index document in vector database."""
        progress.stage = IngestionStage.INDEXING
        progress.progress_percent = 75
        progress.message = "Indexing in vector database..."
        _update_progress(progress)
        
        # Add to vector DB
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(
            None,
            lambda: self.vector_db.add_documents(
                document_id=str(document_id),
                chunks=chunks,
                embeddings=embeddings,
                metadata={
                    "source_file": filename,
                    "document_id": document_id,
                }
            )
        )
        
        progress.progress_percent = 95
        progress.message = "Indexing complete"
        _update_progress(progress)
    
    async def _finalize_document(
        self,
        progress: IngestionProgress,
        document_id: int,
        chunks_count: int,
        db: Session
    ) -> None:
        """Finalize document processing."""
        # Update document record
        document = db.query(Document).filter(Document.id == document_id).first()
        if document:
            document.status = DocumentStatus.INDEXED
            document.chunks_count = chunks_count
            document.indexed_at = datetime.utcnow()
            db.commit()
        
        # Log activity
        activity = Activity(
            action="Document indexed",
            target=document.name if document else f"Document {document_id}",
            target_type="document",
            target_id=document_id,
            activity_type=ActivityType.SUCCESS,
            details={
                "chunks_count": chunks_count,
                "document_id": document_id,
            }
        )
        db.add(activity)
        db.commit()
        
        progress.stage = IngestionStage.COMPLETED
        progress.progress_percent = 100
        progress.message = "Ingestion complete"
        progress.completed_at = datetime.utcnow()
        _update_progress(progress)
        
        logger.info(f"Document {document_id} ingestion completed")
    
    async def _handle_failure(
        self,
        progress: IngestionProgress,
        document_id: int,
        error: str,
        db: Session
    ) -> None:
        """Handle ingestion failure."""
        progress.stage = IngestionStage.FAILED
        progress.error = error
        progress.message = f"Ingestion failed: {error}"
        progress.completed_at = datetime.utcnow()
        _update_progress(progress)
        
        # Update document status
        document = db.query(Document).filter(Document.id == document_id).first()
        if document:
            document.status = DocumentStatus.ERROR
            document.error_message = error
            db.commit()
        
        # Log activity
        activity = Activity(
            action="Document ingestion failed",
            target=document.name if document else f"Document {document_id}",
            target_type="document",
            target_id=document_id,
            activity_type=ActivityType.ERROR,
            details={"error": error}
        )
        db.add(activity)
        db.commit()


# Global pipeline instance
ingestion_pipeline = IngestionPipeline()


async def process_document_async(
    document_id: int,
    file_content: bytes,
    filename: str,
    file_type: str
) -> bool:
    """Process document asynchronously."""
    db = SessionLocal()
    try:
        return await ingestion_pipeline.process_document(
            document_id, file_content, filename, file_type, db
        )
    finally:
        db.close()
