"""Chat API endpoints."""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.logging import logger

router = APIRouter()


class ChatMessage(BaseModel):
    """Chat message schema."""
    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    """Chat request schema."""
    message: str
    model: Optional[str] = None
    stream: bool = True


class Source(BaseModel):
    """Source citation schema."""
    id: str
    document: str
    page: Optional[int] = None
    excerpt: str
    score: float


class ChatResponse(BaseModel):
    """Chat response schema."""
    message: ChatMessage
    sources: Optional[List[Source]] = None


@router.post("/", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    """Send a chat message and get AI response."""
    
    logger.info(f"Chat message received: {request.message[:50]}...")
    
    try:
        # TODO: Implement actual RAG flow:
        # 1. Retrieve relevant chunks from vector DB
        # 2. Build prompt with context
        # 3. Call LLM
        # 4. Return response with sources
        
        # Placeholder response for now
        response_message = ChatMessage(
            role="assistant",
            content="This is a placeholder response. Backend RAG integration is in progress."
        )
        
        return ChatResponse(
            message=response_message,
            sources=None
        )
        
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Chat processing failed: {str(e)}")


@router.post("/stream")
async def chat_stream(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    """Stream chat response."""
    # TODO: Implement streaming with Server-Sent Events
    raise HTTPException(status_code=501, detail="Streaming not yet implemented")


@router.get("/models")
async def list_models():
    """List available LLM models."""
    # TODO: Get from settings/service
    return [
        {"id": "llama3.2:latest", "name": "Llama 3.2", "provider": "ollama"},
        {"id": "mistral:latest", "name": "Mistral", "provider": "ollama"},
        {"id": "gemma:2b", "name": "Gemma 2B", "provider": "ollama"},
    ]
