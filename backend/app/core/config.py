"""Application configuration management."""

import os
from typing import List, Optional
from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # App
    APP_NAME: str = "RAG System API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # Database
    DATABASE_URL: str = "sqlite:///./rag_system.db"
    
    # Vector Database
    VECTOR_DB_TYPE: str = "pgvector"  # pgvector (recommended), chroma, qdrant, pinecone, weaviate
    # Note: pgvector stores vectors in PostgreSQL alongside your data - no separate persist dir needed
    
    # LLM Configuration
    LLM_PROVIDER: str = "ollama"  # ollama, openai, anthropic, cohere
    LLM_MODEL: str = "llama3.2:latest"
    LLM_TEMPERATURE: float = 0.7
    LLM_MAX_TOKENS: int = 2048
    LLM_TOP_P: float = 0.9
    LLM_SYSTEM_PROMPT: str = "You are a helpful AI assistant. Answer questions based on the provided context."
    
    # Embedding Configuration
    EMBEDDING_PROVIDER: str = "ollama"
    EMBEDDING_MODEL: str = "nomic-embed-text:latest"
    EMBEDDING_DIMENSIONS: int = 768
    
    # Chunking Configuration
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 50
    CHUNKING_STRATEGY: str = "semantic"
    
    # Embedding Configuration
    BATCH_SIZE: int = 32
    EMBEDDING_BATCH_SIZE: int = 16  # Texts per batch for embedding
    EMBEDDING_CONCURRENCY: int = 4   # Concurrent embedding requests
    EMBEDDING_MAX_RETRIES: int = 3
    EMBEDDING_RETRY_DELAY: float = 1.0  # seconds
    EMBEDDING_CPU_OPTIMIZED: bool = True  # Use CPU-optimized settings
    
    # Retrieval Configuration
    TOP_K: int = 5
    SIMILARITY_THRESHOLD: float = 0.7
    
    # API Keys (optional)
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    COHERE_API_KEY: Optional[str] = None
    
    # File Upload
    UPLOAD_DIR: str = "./uploads"
    MAX_FILE_SIZE: int = 50 * 1024 * 1024  # 50MB
    ALLOWED_EXTENSIONS: List[str] = [
        ".pdf", ".docx", ".txt", ".md", ".html", ".csv", ".json",
        ".epub", ".pptx", ".odt", ".rtf", ".xml"
    ]
    
    @validator("CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v
    
    @validator("ALLOWED_EXTENSIONS", pre=True)
    def assemble_allowed_extensions(cls, v):
        if isinstance(v, str):
            return [ext.strip() for ext in v.split(",")]
        return v
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
