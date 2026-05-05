"""Vector database service using pgvector."""

from typing import List, Optional, Dict, Any
import uuid
from sqlalchemy import Column, String, Integer, Float, Text, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import ARRAY, JSONB

from app.core.config import settings
from app.core.logging import logger
from app.core.exceptions import VectorDBError

Base = declarative_base()


class VectorChunk(Base):
    """Vector chunk model for pgvector storage."""
    __tablename__ = "vector_chunks"
    
    id = Column(String, primary_key=True)
    document_id = Column(String, nullable=False, index=True)
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    embedding = Column(ARRAY(Float), nullable=False)
    metadata_json = Column(JSONB, nullable=True)
    score = Column(Float, nullable=True)  # Used for search results
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "document_id": self.document_id,
            "chunk_index": self.chunk_index,
            "content": self.content,
            "metadata": self.metadata_json or {},
            "score": self.score,
        }


class VectorDBService:
    """Vector database service using pgvector for PostgreSQL."""
    
    def __init__(self):
        self.engine = None
        self.SessionLocal = None
        self.embedding_dim = settings.EMBEDDING_DIMENSIONS
        self._initialize()
    
    def _initialize(self):
        """Initialize vector database connection."""
        try:
            # Use the same database URL as the main app
            database_url = settings.DATABASE_URL
            
            # Convert sqlite URL to PostgreSQL if needed for development
            # In production on Linux, this should be a real PostgreSQL URL
            if database_url.startswith("sqlite"):
                logger.warning("SQLite detected - pgvector requires PostgreSQL. Using fallback mode.")
                self._init_fallback()
                return
            
            self.engine = create_engine(database_url)
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            
            # Create extension if not exists
            with self.engine.connect() as conn:
                conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
                conn.commit()
            
            # Create tables
            Base.metadata.create_all(bind=self.engine)
            
            logger.info("pgvector initialized with PostgreSQL")
            
        except Exception as e:
            logger.error(f"Vector DB initialization failed: {str(e)}")
            logger.info("Falling back to in-memory storage")
            self._init_fallback()
    
    def _init_fallback(self):
        """Initialize fallback in-memory storage for development."""
        self._fallback_storage: Dict[str, Dict[str, Any]] = {}
        logger.info("Fallback vector storage initialized")
    
    def _is_fallback(self) -> bool:
        """Check if using fallback storage."""
        return self.engine is None
    
    def add_documents(
        self,
        document_id: str,
        chunks: List[str],
        embeddings: List[List[float]],
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Add document chunks to vector DB."""
        if not chunks or not embeddings:
            logger.warning("No chunks or embeddings to add")
            return
        
        try:
            if self._is_fallback():
                self._add_documents_fallback(document_id, chunks, embeddings, metadata)
                return
            
            session = self.SessionLocal()
            try:
                base_metadata = metadata or {}
                
                for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
                    chunk_id = f"{document_id}_chunk_{i}"
                    
                    # Prepare metadata
                    chunk_meta = {
                        **base_metadata,
                        "document_id": document_id,
                        "chunk_index": i,
                        "chunk_text": chunk[:200],  # Store preview
                    }
                    
                    vector_chunk = VectorChunk(
                        id=chunk_id,
                        document_id=document_id,
                        chunk_index=i,
                        content=chunk,
                        embedding=embedding,
                        metadata_json=chunk_meta,
                    )
                    
                    session.merge(vector_chunk)  # Use merge to upsert
                
                session.commit()
                logger.info(f"Added {len(chunks)} chunks for document {document_id}")
                
            finally:
                session.close()
            
        except Exception as e:
            logger.error(f"Failed to add documents: {str(e)}")
            raise VectorDBError(f"Failed to add documents: {str(e)}")
    
    def _add_documents_fallback(
        self,
        document_id: str,
        chunks: List[str],
        embeddings: List[List[float]],
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Fallback method for adding documents when PostgreSQL is not available."""
        base_metadata = metadata or {}
        
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            chunk_id = f"{document_id}_chunk_{i}"
            self._fallback_storage[chunk_id] = {
                "id": chunk_id,
                "document_id": document_id,
                "chunk_index": i,
                "content": chunk,
                "embedding": embedding,
                "metadata": {
                    **base_metadata,
                    "document_id": document_id,
                    "chunk_index": i,
                    "chunk_text": chunk[:200],
                },
            }
        
        logger.info(f"Added {len(chunks)} chunks to fallback storage for document {document_id}")
    
    def search(
        self,
        query_embedding: List[float],
        top_k: int = None,
        similarity_threshold: float = None,
        filter_dict: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Search for similar chunks using cosine similarity."""
        top_k = top_k or settings.TOP_K
        similarity_threshold = similarity_threshold or settings.SIMILARITY_THRESHOLD
        
        try:
            if self._is_fallback():
                return self._search_fallback(query_embedding, top_k, similarity_threshold, filter_dict)
            
            session = self.SessionLocal()
            try:
                # Convert query embedding to PostgreSQL array format
                embedding_str = ",".join(str(x) for x in query_embedding)
                
                # Build filter conditions
                filter_conditions = ""
                if filter_dict:
                    conditions = []
                    for key, value in filter_dict.items():
                        conditions.append(f"metadata_json->>'{key}' = '{value}'")
                    if conditions:
                        filter_conditions = "WHERE " + " AND ".join(conditions)
                
                # Perform vector similarity search
                # Using 1 - (embedding <=> query_embedding) for cosine similarity
                sql = f"""
                    SELECT id, document_id, chunk_index, content, metadata_json,
                           1 - (embedding <=> ARRAY[{embedding_str}]::vector) as score
                    FROM vector_chunks
                    {filter_conditions}
                    ORDER BY embedding <=> ARRAY[{embedding_str}]::vector
                    LIMIT {top_k * 2}  -- Get more than needed for filtering
                """
                
                result = session.execute(text(sql))
                
                # Format results
                formatted_results = []
                for row in result:
                    if row.score >= similarity_threshold:
                        formatted_results.append({
                            "id": row.id,
                            "text": row.content,
                            "metadata": row.metadata_json or {},
                            "score": row.score,
                        })
                
                # Limit to top_k after filtering
                formatted_results = formatted_results[:top_k]
                
                logger.info(f"Search returned {len(formatted_results)} results")
                return formatted_results
                
            finally:
                session.close()
            
        except Exception as e:
            logger.error(f"Search failed: {str(e)}")
            raise VectorDBError(f"Search failed: {str(e)}")
    
    def _search_fallback(
        self,
        query_embedding: List[float],
        top_k: int,
        similarity_threshold: float,
        filter_dict: Optional[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Fallback search using cosine similarity calculation."""
        import numpy as np
        
        def cosine_similarity(a, b):
            return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        
        query_vec = np.array(query_embedding)
        results = []
        
        for chunk_id, chunk_data in self._fallback_storage.items():
            # Apply filters if provided
            if filter_dict:
                skip = False
                for key, value in filter_dict.items():
                    if chunk_data["metadata"].get(key) != value:
                        skip = True
                        break
                if skip:
                    continue
            
            # Calculate similarity
            chunk_vec = np.array(chunk_data["embedding"])
            score = float(cosine_similarity(query_vec, chunk_vec))
            
            if score >= similarity_threshold:
                results.append({
                    "id": chunk_id,
                    "text": chunk_data["content"],
                    "metadata": chunk_data["metadata"],
                    "score": score,
                })
        
        # Sort by score and limit
        results.sort(key=lambda x: x["score"], reverse=True)
        results = results[:top_k]
        
        logger.info(f"Fallback search returned {len(results)} results")
        return results
    
    def delete_document(self, document_id: str):
        """Delete all chunks for a document."""
        try:
            if self._is_fallback():
                # Delete from fallback storage
                keys_to_delete = [
                    key for key, data in self._fallback_storage.items()
                    if data["document_id"] == document_id
                ]
                for key in keys_to_delete:
                    del self._fallback_storage[key]
                logger.info(f"Deleted {len(keys_to_delete)} chunks from fallback for document {document_id}")
                return
            
            session = self.SessionLocal()
            try:
                count = session.query(VectorChunk).filter(
                    VectorChunk.document_id == document_id
                ).delete()
                session.commit()
                logger.info(f"Deleted {count} chunks for document {document_id}")
            finally:
                session.close()
            
        except Exception as e:
            logger.error(f"Failed to delete document: {str(e)}")
            raise VectorDBError(f"Failed to delete document: {str(e)}")
    
    def get_stats(self) -> Dict[str, int]:
        """Get vector DB statistics."""
        try:
            if self._is_fallback():
                return {"total_chunks": len(self._fallback_storage)}
            
            session = self.SessionLocal()
            try:
                count = session.query(VectorChunk).count()
                return {"total_chunks": count}
            finally:
                session.close()
                
        except Exception as e:
            logger.error(f"Failed to get stats: {str(e)}")
            return {"total_chunks": 0}
    
    def persist(self):
        """No-op for pgvector (automatic persistence)."""
        logger.debug("pgvector persistence handled automatically by PostgreSQL")


# Global service instance
vector_db_service = VectorDBService()
