# RAG Robot System - Progress Tracker

## Project Overview
Offline RAG document management system for robot with 128GB Thor AGX. Hybrid architecture (metadata + hierarchical + vector search) using Next.js 16.2, FastAPI, PostgreSQL/pgvector, Ollama.

---

## Architecture Summary

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 16.2 + React 19.2 + TypeScript + Tailwind + Zustand |
| Backend | FastAPI + LangChain |
| Database | PostgreSQL + pgvector |
| LLM | Ollama (configurable) |
| Embeddings | nomic-embed-text (switchable) |
| Document Parser | unstructured[pdf] + pytesseract |

---

## Features Checklist

### Phase 1: Core Infrastructure
- [x] **1.1** Project setup - Next.js 16.2 frontend structure
  - [x] Amber Minimal theme setup (light/dark modes)
  - [x] Theme toggle functionality
  - [x] Dashboard layout with navigation
- [ ] **1.2** FastAPI backend structure with async support
- [ ] **1.3** PostgreSQL + pgvector schema design
- [ ] **1.4** Ollama integration with model registry
- [ ] **1.5** Environment configuration (.env, docker-compose optional)

### Phase 2: Document Processing Pipeline
- [ ] **2.1** Document upload API (streaming for <10MB, async for >10MB)
- [ ] **2.2** Rich metadata extraction (filename, date, author, pages, sections, tags)
- [ ] **2.3** Document parser/loader (PyMuPDF, unstructured, LlamaParse optional)
- [ ] **2.4** Structure-aware chunking (recursive + headings/sections, configurable size/overlap)
- [ ] **2.5** Embedding generation (batch + CPU optimized)
- [ ] **2.6** Vector storage with metadata in pgvector
- [ ] **2.7** Background job processing with progress tracking

### Phase 3: Retrieval & Query
- [ ] **3.1** Query processing (user question + metadata filters)
- [ ] **3.2** Hybrid retrieval (vector + metadata filtering + hierarchy)
- [ ] **3.3** Context builder (top-k chunks + source metadata + page/section info)
- [ ] **3.4** LLM integration with Ollama streaming
- [ ] **3.5** Response formatting with citations

### Phase 4: UI/UX
- [ ] **4.1** Document upload interface with progress
- [ ] **4.2** Document listing with filters (date, type, collection, tags)
- [ ] **4.3** Document details view (preview, metadata, re-index, delete)
- [ ] **4.4** Search interface (filename + content)
- [ ] **4.5** Chat interface with streaming responses
- [ ] **4.6** Model configuration panel (LLM + embedding selection)

### Phase 5: Advanced Features
- [ ] **5.1** OCR for scanned PDFs/images
- [ ] **5.2** Multilingual support (Hindi/English)
- [ ] **5.3** Incremental indexing
- [ ] **5.4** Document re-processing/re-indexing
- [ ] **5.5** Archive old documents
- [ ] **5.6** Graph RAG extension hooks (future)

### Phase 6: Auth & Multi-user (Future)
- [ ] **6.1** Single-user auth (current)
- [ ] **6.2** Role-based access (admin, editor, viewer)
- [ ] **6.3** Private vs shared collections

---

## Database Schema

```sql
-- Documents table
CREATE TABLE documents (
    id UUID PRIMARY KEY,
    filename TEXT,
    file_path TEXT,
    file_size BIGINT,
    upload_date TIMESTAMP,
    author TEXT,
    doc_type TEXT,
    collection TEXT,
    total_pages INT,
    metadata JSONB,
    status VARCHAR(20) -- 'processing', 'completed', 'error'
);

-- Sections (hierarchical indexing)
CREATE TABLE document_sections (
    id UUID PRIMARY KEY,
    document_id UUID REFERENCES documents(id),
    parent_section_id UUID REFERENCES document_sections(id),
    section_title TEXT,
    section_level INT, -- 1=H1, 2=H2, etc.
    page_number INT,
    content TEXT
);

-- Vector chunks with metadata
CREATE TABLE chunks (
    id UUID PRIMARY KEY,
    document_id UUID REFERENCES documents(id),
    section_id UUID REFERENCES document_sections(id),
    chunk_index INT,
    content TEXT,
    page_number INT,
    metadata JSONB,
    embedding vector(768) -- for nomic-embed-text
);
```

---

## Current Status

**Last Updated:** 2026-05-01
**Current Phase:** Planning Complete, Ready for Implementation
**Next Action:** Create project structure

---

## Working Notes

### Key Decisions Log
- **2026-04-30:** Switched from LanceDB to pgvector (better metadata filtering, no migration pain)
- **2026-05-01:** Confirmed Next.js 16.2 with AI features (AGENTS.md, Cache Components, React 19.2)
- **2026-04-30:** Graph RAG deferred - architecture has extension hooks
- **2026-04-30:** Single-user auth for MVP, multi-user later
- **2026-04-30:** Streaming upload (<10MB), async background (>10MB)

### Resource Allocation (128GB Thor AGX)
- RAG System: ~64GB available
- Embedding batch size: 512-1024
- Parallel document processing: 2-4 files
- CPU cores: Use 50% (other processes + NLP tasks)

---

## Verification Checklist

Before marking complete, verify:
- [ ] Feature works as specified
- [ ] Tests pass (if applicable)
- [ ] No dead code or unused imports
- [ ] Code follows existing style
- [ ] Documentation updated

---

## Quick Links
- Original research: `RAG documentation.md`
- Architecture: `Final Arch.txt`
- Guidelines: `SKILL.md`, `CURSOR.md`
