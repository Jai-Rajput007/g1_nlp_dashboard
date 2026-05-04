"""Document API endpoints."""

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Query
from sqlalchemy.orm import Session
import os
import shutil
from pathlib import Path

from app.db.database import get_db
from app.models.document import Document, DocumentStatus
from app.schemas.document import DocumentResponse, DocumentCreate, DocumentStats
from app.core.config import settings
from app.core.logging import logger
from app.core.exceptions import FileUploadError, NotFoundError

router = APIRouter()


@router.get("/", response_model=List[DocumentResponse])
async def list_documents(
    status: Optional[str] = Query(None, description="Filter by status"),
    search: Optional[str] = Query(None, description="Search by name"),
    db: Session = Depends(get_db)
):
    """List all documents with optional filtering."""
    query = db.query(Document)
    
    if status:
        query = query.filter(Document.status == status)
    
    if search:
        query = query.filter(Document.name.ilike(f"%{search}%"))
    
    documents = query.order_by(Document.created_at.desc()).all()
    return [doc.to_dict() for doc in documents]


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload a new document."""
    
    # Validate file extension
    file_ext = Path(file.filename).suffix.lower()
    if file_ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed: {', '.join(settings.ALLOWED_EXTENSIONS)}"
        )
    
    try:
        # Generate unique filename
        timestamp = int(os.path.getctime(".")) if os.path.exists(".") else 0
        safe_filename = f"{timestamp}_{file.filename}"
        file_path = Path(settings.UPLOAD_DIR) / safe_filename
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Get file size
        file_size = os.path.getsize(file_path)
        
        # Create database record
        doc = Document(
            name=file.filename,
            original_filename=file.filename,
            file_path=str(file_path),
            file_type=file_ext.replace(".", ""),
            file_size=file_size,
            status=DocumentStatus.UPLOADED
        )
        
        db.add(doc)
        db.commit()
        db.refresh(doc)
        
        logger.info(f"Document uploaded: {file.filename} (ID: {doc.id})")
        
        return doc.to_dict()
        
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")


@router.get("/{document_id}", response_model=DocumentResponse)
async def get_document(document_id: int, db: Session = Depends(get_db)):
    """Get document by ID."""
    doc = db.query(Document).filter(Document.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc.to_dict()


@router.delete("/{document_id}")
async def delete_document(document_id: int, db: Session = Depends(get_db)):
    """Delete document."""
    doc = db.query(Document).filter(Document.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    try:
        # Delete file
        if os.path.exists(doc.file_path):
            os.remove(doc.file_path)
        
        # Delete from database
        db.delete(doc)
        db.commit()
        
        logger.info(f"Document deleted: {doc.name} (ID: {document_id})")
        
        return {"message": "Document deleted successfully"}
        
    except Exception as e:
        logger.error(f"Delete failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Delete failed: {str(e)}")


@router.post("/{document_id}/reindex")
async def reindex_document(document_id: int, db: Session = Depends(get_db)):
    """Reindex a document."""
    doc = db.query(Document).filter(Document.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Update status
    doc.status = DocumentStatus.PROCESSING
    db.commit()
    
    # TODO: Trigger background processing
    
    return {"message": "Document queued for reindexing"}


@router.get("/stats/summary", response_model=DocumentStats)
async def get_document_stats(db: Session = Depends(get_db)):
    """Get document statistics."""
    total = db.query(Document).count()
    indexed = db.query(Document).filter(Document.status == DocumentStatus.INDEXED).count()
    processing = db.query(Document).filter(Document.status == DocumentStatus.PROCESSING).count()
    error = db.query(Document).filter(Document.status == DocumentStatus.ERROR).count()
    
    # Calculate total size
    total_size = sum(doc.file_size for doc in db.query(Document).all())
    
    return {
        "total": total,
        "indexed": indexed,
        "processing": processing,
        "error": error,
        "totalSize": total_size
    }
