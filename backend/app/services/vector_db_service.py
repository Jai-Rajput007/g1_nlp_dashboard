"""Vector database service."""

from typing import List, Optional, Dict, Any
import uuid

from app.core.config import settings
from app.core.logging import logger
from app.core.exceptions import VectorDBError


class VectorDBService:
    """Vector database service for managing document embeddings."""
    
    def __init__(self):
        self.client = None
        self.collection = None
        self._initialize()
    
    def _initialize(self):
        """Initialize vector database connection."""
        try:
            if settings.VECTOR_DB_TYPE == "chroma":
                self._init_chroma()
            else:
                raise VectorDBError(f"Unsupported vector DB: {settings.VECTOR_DB_TYPE}")
        except Exception as e:
            logger.error(f"Vector DB initialization failed: {str(e)}")
            raise VectorDBError(f"Vector DB initialization failed: {str(e)}")
    
    def _init_chroma(self):
        """Initialize ChromaDB."""
        import chromadb
        from chromadb.config import Settings
        
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=settings.CHROMA_PERSIST_DIR
        ))
        
        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )
        
        logger.info("ChromaDB initialized")
    
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
            # Generate IDs for chunks
            chunk_ids = [f"{document_id}_chunk_{i}" for i in range(len(chunks))]
            
            # Prepare metadata for each chunk
            metadatas = []
            base_metadata = metadata or {}
            
            for i, chunk in enumerate(chunks):
                chunk_meta = {
                    **base_metadata,
                    "document_id": document_id,
                    "chunk_index": i,
                    "chunk_text": chunk[:200],  # Store preview
                }
                metadatas.append(chunk_meta)
            
            # Add to collection
            self.collection.add(
                embeddings=embeddings,
                documents=chunks,
                metadatas=metadatas,
                ids=chunk_ids
            )
            
            logger.info(f"Added {len(chunks)} chunks for document {document_id}")
            
        except Exception as e:
            logger.error(f"Failed to add documents: {str(e)}")
            raise VectorDBError(f"Failed to add documents: {str(e)}")
    
    def search(
        self,
        query_embedding: List[float],
        top_k: int = None,
        similarity_threshold: float = None,
        filter_dict: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Search for similar chunks."""
        top_k = top_k or settings.TOP_K
        similarity_threshold = similarity_threshold or settings.SIMILARITY_THRESHOLD
        
        try:
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
                where=filter_dict,
                include=["documents", "metadatas", "distances"]
            )
            
            # Format results
            formatted_results = []
            
            if results["ids"] and results["ids"][0]:
                for i, chunk_id in enumerate(results["ids"][0]):
                    distance = results["distances"][0][i]
                    # Convert distance to similarity (cosine distance to similarity)
                    similarity = 1 - distance
                    
                    if similarity >= similarity_threshold:
                        formatted_results.append({
                            "id": chunk_id,
                            "text": results["documents"][0][i],
                            "metadata": results["metadatas"][0][i],
                            "score": similarity,
                        })
            
            logger.info(f"Search returned {len(formatted_results)} results")
            return formatted_results
            
        except Exception as e:
            logger.error(f"Search failed: {str(e)}")
            raise VectorDBError(f"Search failed: {str(e)}")
    
    def delete_document(self, document_id: str):
        """Delete all chunks for a document."""
        try:
            # Find all chunks for this document
            results = self.collection.get(
                where={"document_id": document_id}
            )
            
            if results["ids"]:
                self.collection.delete(ids=results["ids"])
                logger.info(f"Deleted {len(results['ids'])} chunks for document {document_id}")
            
        except Exception as e:
            logger.error(f"Failed to delete document: {str(e)}")
            raise VectorDBError(f"Failed to delete document: {str(e)}")
    
    def get_stats(self) -> Dict[str, int]:
        """Get vector DB statistics."""
        try:
            count = self.collection.count()
            return {
                "total_chunks": count,
            }
        except Exception as e:
            logger.error(f"Failed to get stats: {str(e)}")
            return {"total_chunks": 0}
    
    def persist(self):
        """Persist changes to disk (for ChromaDB)."""
        if settings.VECTOR_DB_TYPE == "chroma":
            try:
                # ChromaDB persists automatically with duckdb+parquet
                logger.debug("ChromaDB persistence handled automatically")
            except Exception as e:
                logger.error(f"Failed to persist: {str(e)}")


# Global service instance
vector_db_service = VectorDBService()
