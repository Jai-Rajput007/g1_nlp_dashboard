# Graph Report - g1_nlp_dashboard  (2026-05-08)

## Corpus Check
- 76 files · ~55,701 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1110 nodes · 2175 edges · 86 communities (70 shown, 16 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 379 edges (avg confidence: 0.58)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `76df47e7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 68|Community 68]]
- [[_COMMUNITY_Community 69|Community 69]]
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 72|Community 72]]
- [[_COMMUNITY_Community 73|Community 73]]
- [[_COMMUNITY_Community 74|Community 74]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 76|Community 76]]

## God Nodes (most connected - your core abstractions)
1. `DocumentProcessingError` - 49 edges
2. `load_from_bytes()` - 40 edges
3. `DocumentContent` - 37 edges
4. `ContentElement` - 35 edges
5. `ChatService` - 34 edges
6. `LangChainLoaderWrapper` - 28 edges
7. `MarkdownLoader` - 28 edges
8. `DOCXLoader` - 27 edges
9. `EmbeddingError` - 27 edges
10. `Chat()` - 26 edges

## Surprising Connections (you probably didn't know these)
- `DocumentStatus` --uses--> `IngestionStage`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/services/ingestion_pipeline.py
- `DocumentStatus` --uses--> `IngestionProgress`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/services/ingestion_pipeline.py
- `Document` --uses--> `IngestionStage`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/services/ingestion_pipeline.py
- `Document` --uses--> `IngestionProgress`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/services/ingestion_pipeline.py
- `Chat()` --rationale_for--> `Generate chat completion with Ollama.`  [EXTRACTED]
  frontend/g1-dashboard/app/chat/page.tsx → backend/app/services/llm_service.py

## Communities (86 total, 16 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (73): Chat(), Source, chat(), chat_stream(), ChatMessage, ChatRequest, ChatResponse, list_models() (+65 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (48): Load document from bytes., can_load_file(), get_all_supported_extensions(), get_langchain_extensions(), _get_langchain_loader(), get_loader_for_file(), get_supported_extensions(), load_document() (+40 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (60): Base, BaseModel, Activity, Dashboard(), ModelStatus, ActivityItem, DashboardResponse, DashboardStats (+52 more)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (27): ConfigurationError, FileUploadError, NotFoundError, RAGSystemException, Custom application exceptions., Raised when vector database operation fails., Raised when configuration is invalid., Raised when file upload fails. (+19 more)

### Community 4 - "Community 4"
Cohesion: 0.1
Nodes (27): cn(), Message, suggestedPrompts, Document, Stats, api, ApiResponse, cn() (+19 more)

### Community 5 - "Community 5"
Cohesion: 0.11
Nodes (21): DocumentProcessor, DOCXExtractor, extract(), PDFExtractor, Document processing service., Extract text from any supported file., Split text into chunks., Fixed-size chunking with overlap. (+13 more)

### Community 6 - "Community 6"
Cohesion: 0.13
Nodes (16): ChunkMetadata, Structure-aware document chunking service with hierarchy preservation., Advanced chunking that preserves document structure and hierarchy., Stream chunks with progress updates.                  Args:             document, Chunk document synchronously (for non-streaming use).                  Returns:, Rich metadata for a document chunk., Update heading context when encountering a heading., Create a DocumentChunk from elements. (+8 more)

### Community 7 - "Community 7"
Cohesion: 0.14
Nodes (16): Build context using specified strategy., ContextBuilderService, ContextChunk, Context builder service for assembling retrieved chunks into LLM context., Convert retrieval results to context chunks., Build context grouped by hierarchy., Build context sorted by relevance., Context chunk with metadata for assembly. (+8 more)

### Community 8 - "Community 8"
Cohesion: 0.13
Nodes (15): ABC, LLMError, Raised when LLM operation fails., LLMProvider, LLMService, OllamaProvider, OpenAIProvider, LLM service for chat completion. (+7 more)

### Community 9 - "Community 9"
Cohesion: 0.13
Nodes (11): Parse HTML table element., MarkdownLoader, Markdown document loader with support for all MD elements., Markdown loader with full syntax support., Check if line is part of a table., Load Markdown from file path., Check if line is a list item., Parse image reference. (+3 more)

### Community 10 - "Community 10"
Cohesion: 0.21
Nodes (16): EmbeddingError, Raised when embedding generation fails., CohereEmbeddingProvider, embed(), embed_query(), EmbeddingProvider, OllamaEmbeddingProvider, OpenAIEmbeddingProvider (+8 more)

### Community 11 - "Community 11"
Cohesion: 0.12
Nodes (13): DOCXLoader, DOCX document loader with support for images, tables, lists, and formatting., Check if list item is part of ordered list., Extract text from paragraph with run formatting., DOCX loader with comprehensive content extraction., Process a paragraph into a content element., Detect code block by style., Detect quote by style. (+5 more)

### Community 12 - "Community 12"
Cohesion: 0.16
Nodes (18): geistMono, geistSans, metadata, ChatIcon(), DashboardIcon(), defaultNavItems, HomeIcon(), LibraryIcon() (+10 more)

### Community 13 - "Community 13"
Cohesion: 0.12
Nodes (17): BaseSettings, Config, Application configuration management., Application settings with environment variable support., Settings, get_settings(), Settings API endpoints., Settings response schema. (+9 more)

### Community 14 - "Community 14"
Cohesion: 0.09
Nodes (21): Adding a New Feature, API Documentation, code:block1 (backend/), code:bash (python -m venv venv), code:bash (pip install -r requirements.txt), code:bash (cp .env.example .env), code:bash (python main.py), code:bash (pytest) (+13 more)

### Community 15 - "Community 15"
Cohesion: 0.1
Nodes (20): 3.1 Ingestion Pipeline (`ingestion_pipeline.py`), 3.2 Document Loaders (`document_loaders/`), 3.3 Structure-Aware Chunker (`structure_aware_chunker.py`), 3.4 Embedding Service (`embedding_service_optimized.py`), 3.5 Vector Database (`vector_db_service.py`), 3.7 Query Processing Service (`query_processing_service.py`), 3.8 Context Builder Service (`context_builder_service.py`), 3.9 Chat Service (`chat_service.py`) (+12 more)

### Community 16 - "Community 16"
Cohesion: 0.1
Nodes (20): Architecture Summary, code:sql (-- Documents table), Completed, Current Status, Database Schema, Features Checklist, Key Decisions Log, Phase 1: Core Infrastructure (+12 more)

### Community 17 - "Community 17"
Cohesion: 0.12
Nodes (11): EmbeddingProvider, OllamaEmbeddingProvider, OpenAIEmbeddingProvider, Optimized embedding generation service with batch processing and CPU optimizatio, Generate embedding for query., Abstract base class for embedding providers., Ollama embedding provider with batch and retry support., Generate embeddings using Ollama with retry logic. (+3 more)

### Community 18 - "Community 18"
Cohesion: 0.17
Nodes (11): Retrieval service for hybrid search with metadata filtering and hierarchy., Service for hybrid retrieval with prefiltering, hierarchy, and vector search., Build prefilter dictionary from query filters.         These filters are applied, Apply post-filters that couldn't be applied in prefiltering., Enrich result with hierarchy information from metadata., Perform hybrid retrieval with prefiltering and vector search.                  F, Retrieve using hierarchy-based filtering.                  Args:             que, Retrieve with parent section context for each result.                  This is u (+3 more)

### Community 19 - "Community 19"
Cohesion: 0.15
Nodes (11): Parse content and try to detect structure., Detect if line is a heading., PDFLoader, PDF document loader with support for images, tables, and structured content., Extract content from a single page., Heuristic to detect if a line is a heading., PDF loader with comprehensive content extraction., Detect heading level. (+3 more)

### Community 20 - "Community 20"
Cohesion: 0.12
Nodes (11): Check if paragraph is a list item., create_langchain_loader(), LangChainLoaderWrapper, LangChain document loader wrapper for fallback format support., Wrapper for LangChain document loaders to adapt to our format., Load using LangChain loader., Detect heading level., Detect if line is a list item. (+3 more)

### Community 21 - "Community 21"
Cohesion: 0.12
Nodes (9): EmbeddingServiceOptimized, Optimized embedding service with batch processing and CPU optimization., Create embedding provider based on settings., Generate embeddings with batch processing and concurrency control., Stream embeddings as they are generated.                  Yields:             Di, Generate embedding for query (synchronous)., Generate embedding for query (async)., Generate embeddings for documents. (+1 more)

### Community 22 - "Community 22"
Cohesion: 0.21
Nodes (11): ContentElement, DocumentLoader, Abstract base class for document loaders., Check if loader can handle file., Helper to create text element., Helper to create heading element., Helper to create list element., Helper to create table element. (+3 more)

### Community 23 - "Community 23"
Cohesion: 0.17
Nodes (11): Document ingestion pipeline with progress tracking and async processing., Chunk document with structure awareness and streaming progress., Generate embeddings with batch processing and progress tracking., Finalize document processing., Handle ingestion failure., Register callback for progress updates., Unregister progress callback., Update progress and notify callbacks. (+3 more)

### Community 24 - "Community 24"
Cohesion: 0.16
Nodes (9): DocumentContent, Get all image elements., Split document into text chunks., Convert element to plain text., Complete document content with structure., Convert all content to plain text., Get all heading elements., Get all table elements. (+1 more)

### Community 25 - "Community 25"
Cohesion: 0.22
Nodes (9): load_from_bytes(), JSONLoader, JSON document loader with structure preservation., JSON loader with structured content extraction., Flatten JSON to readable text., Load JSON from file path., Load JSON from bytes., Parse JSON Lines format. (+1 more)

### Community 26 - "Community 26"
Cohesion: 0.19
Nodes (8): CSVLoader, CSV document loader with table structure support., Detect CSV delimiter from sample., Parse CSV text into rows and headers., Calculate basic statistics for numeric columns., Format CSV as readable text., CSV loader with table structure extraction., Load CSV from file path.

### Community 27 - "Community 27"
Cohesion: 0.21
Nodes (9): DocumentProcessingError, Raised when document processing fails., load(), Load PDF from file path., Plain text document loader., Detect heading level., Load text from file path., Load text from bytes. (+1 more)

### Community 28 - "Community 28"
Cohesion: 0.22
Nodes (8): HTMLLoader, HTML document loader with support for structured content extraction., Parse HTML with regex fallback., HTML loader with content structure extraction., Load HTML from file path., Extract plain text from HTML., Load HTML from bytes., Parse HTML with BeautifulSoup.

### Community 29 - "Community 29"
Cohesion: 0.14
Nodes (14): 1. Navigate to backend directory, 2. Create Python virtual environment, 3. Install Python dependencies, 4. Configure environment variables, 5. Initialize database, 6. Test backend startup, ⚙️ Backend Setup, code:bash (pip install --upgrade pip) (+6 more)

### Community 30 - "Community 30"
Cohesion: 0.14
Nodes (13): **1. Normal RAG (Traditional Document RAG)**, **2. Vectorless RAG (PageIndex)**, **3. Graph RAG**, **4. Knowledge Augmented Generation (KAG)**, code:block1 (┌───────────────────────────────────────────────────────────), code:block2 (┌───────────────────────────────────────────────────────────), code:block3 (┌───────────────────────────────────────────────────────────), code:block4 (┌───────────────────────────────────────────────────────────) (+5 more)

### Community 31 - "Community 31"
Cohesion: 0.18
Nodes (9): Convert to dictionary for API response., IngestionProgress, IngestionStage, Stages of document ingestion., Index document in vector database with rich metadata., Track ingestion progress., DocumentChunk, A document chunk with rich metadata. (+1 more)

### Community 32 - "Community 32"
Cohesion: 0.24
Nodes (6): DocumentMetadata, Extract DOCX metadata., Extract metadata from LangChain documents., Convert LangChain Document list to our DocumentContent format., Extract PDF metadata., Parse keywords from metadata.

### Community 33 - "Community 33"
Cohesion: 0.18
Nodes (11): 1. Install Docker & Docker Compose, 2. Install Ollama (for local LLM), 3. Install Node.js & npm, 4. Install Python 3.11+, 5. Install system dependencies, code:bash (# Ubuntu/Debian), code:bash (curl -fsSL https://ollama.com/install.sh | sh), code:bash (# Using NodeSource (Ubuntu/Debian)) (+3 more)

### Community 34 - "Community 34"
Cohesion: 0.2
Nodes (10): 1. Navigate to frontend directory, 2. Install dependencies, 3. Configure frontend environment, 4. Build and start frontend, code:bash (cd /path/to/project/frontend/g1-dashboard), code:bash (# Using npm), code:bash (# Create .env.local), code:env (NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1) (+2 more)

### Community 35 - "Community 35"
Cohesion: 0.2
Nodes (9): 10. KEY TECHNICAL DECISIONS, 12. FILES TO CHECK FOR ERRORS, 1. PROJECT OVERVIEW, 2. PROJECT STRUCTURE, 8. PENDING FEATURES, code:block1 (Implementation/), Phase 5: Advanced Features, Phase 6: Auth & Multi-user (+1 more)

### Community 36 - "Community 36"
Cohesion: 0.31
Nodes (8): ContentType, ElementType, Base document loader interface., Types of content elements., Element types for structured content., Enum, ChunkBoundaryType, Types of chunk boundaries.

### Community 37 - "Community 37"
Cohesion: 0.22
Nodes (9): 1. Create `docker-compose.yml` in project root, 2. Create `Dockerfile` for backend, 3. Create `Dockerfile` for frontend, 4. Run with Docker Compose, code:yaml (version: '3.8'), code:dockerfile (# backend/Dockerfile), code:dockerfile (# frontend/g1-dashboard/Dockerfile), code:bash (# Build and start all services) (+1 more)

### Community 38 - "Community 38"
Cohesion: 0.22
Nodes (9): code:bash (# Check if PostgreSQL is running), code:bash (# Check if Ollama is running), code:bash (# Ensure virtual environment is activated), code:bash (# Find and kill process using port 8000), Issue: "Cannot connect to PostgreSQL", Issue: "Module not found" in Python, Issue: "Ollama connection refused", Issue: "Port already in use" (+1 more)

### Community 39 - "Community 39"
Cohesion: 0.22
Nodes (9): 9. COMMON ISSUES & SOLUTIONS, code:bash (# Check if running), code:bash (# Check Ollama), code:bash (cd backend), Issue: "Cannot connect to PostgreSQL", Issue: Embedding service slow, Issue: Frontend can't connect to backend, Issue: "Module not found" in Python (+1 more)

### Community 40 - "Community 40"
Cohesion: 0.22
Nodes (5): 5. DATABASE SCHEMA, Activities Table, Chunks Table (PostgreSQL with pgvector), Documents Table, Settings Table

### Community 41 - "Community 41"
Cohesion: 0.25
Nodes (7): Backend (.env), code:block35 (project-root/), 📝 Environment Variables Reference, Frontend (.env.local), Linux Setup Guide - RAG Document Processing System, 📁 Project Structure, 🎉 You're Ready!

### Community 42 - "Community 42"
Cohesion: 0.33
Nodes (4): EmbeddingService, Main embedding service., Create embedding provider based on settings., Generate embedding for query.

### Community 43 - "Community 43"
Cohesion: 0.29
Nodes (5): get_db(), init_db(), Database connection and session management., Get database session., Initialize database tables.

### Community 44 - "Community 44"
Cohesion: 0.29
Nodes (7): Access the Application, code:bash (sudo systemctl start postgresql), code:bash (ollama serve), code:bash (cd /path/to/project/backend), code:bash (cd /path/to/project/frontend/g1-dashboard), Manual Start (Development), 🚀 Running the Application

### Community 45 - "Community 45"
Cohesion: 0.29
Nodes (7): 1. Test Ollama, 2. Test Backend API, 3. Test Chat, code:bash (curl http://localhost:11434/api/tags), code:bash (# Health check), code:bash (# Send chat message), 🧪 Testing the Setup

### Community 46 - "Community 46"
Cohesion: 0.29
Nodes (7): 4.1 Chat (`/api/v1/chat/`), 4.2 Documents (`/api/v1/documents/`), 4.3 Dashboard (`/api/v1/dashboard/`), 4.4 Settings (`/api/v1/settings/`), 4. API ENDPOINTS, code:json ({), code:json ({)

### Community 47 - "Community 47"
Cohesion: 0.29
Nodes (7): 11. DEBUGGING TIPS, Check Service Logs, code:bash (# Backend logs (if using uvicorn)), code:bash (# Test embedding), code:bash (# PostgreSQL), Database Inspection, Test Individual Components

### Community 48 - "Community 48"
Cohesion: 0.29
Nodes (6): Claude Code vs Cursor, For contributors, In this repository, Optional: personal Agent Skills, Use the same guidelines in another project, Using this repo with Cursor

### Community 49 - "Community 49"
Cohesion: 0.29
Nodes (6): 1. Think Before Coding, 2. Simplicity First, 3. Surgical Changes, 4. Goal-Driven Execution, code:block1 (1. [Step] → verify: [check]), Karpathy Guidelines

### Community 50 - "Community 50"
Cohesion: 0.4
Nodes (4): create_application(), FastAPI application factory., Create and configure FastAPI application., Main application entry point.

### Community 51 - "Community 51"
Cohesion: 0.33
Nodes (3): Generate embedding for query., Generate embedding for query., Generate embeddings using Cohere.

### Community 52 - "Community 52"
Cohesion: 0.4
Nodes (5): code:bash (# Create docker-compose for database services), code:bash (# Ubuntu/Debian), 🗄️ Database Setup (PostgreSQL + pgvector), Option A: Using Docker (Recommended), Option B: Install PostgreSQL locally

### Community 53 - "Community 53"
Cohesion: 0.4
Nodes (5): 6. ENVIRONMENT CONFIGURATION, Backend (.env), code:bash (# Database), code:bash (NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1), Frontend (.env.local)

### Community 54 - "Community 54"
Cohesion: 0.4
Nodes (5): 13. QUICK START (After Setup), code:bash (docker start rag-postgres), code:bash (ollama serve), code:bash (cd backend), code:bash (cd frontend/g1-dashboard)

### Community 55 - "Community 55"
Cohesion: 0.4
Nodes (5): 7. COMPLETED FEATURES, Phase 1: Core Infrastructure ✅, Phase 2: Document Processing ✅, Phase 3: Retrieval & Query ✅, Phase 4: Frontend-Backend Integration ✅

### Community 56 - "Community 56"
Cohesion: 0.4
Nodes (4): code:bash (npm run dev), Deploy on Vercel, Getting Started, Learn More

### Community 59 - "Community 59"
Cohesion: 0.5
Nodes (3): Logging configuration., Configure application logging., setup_logging()

### Community 60 - "Community 60"
Cohesion: 0.67
Nodes (3): 3.6 Retrieval Service (`retrieval_service.py`), code:python (retrieve_by_hierarchy(section_path="Chapter 1")), code:python (@dataclass)

## Knowledge Gaps
- **383 isolated node(s):** `config`, `eslintConfig`, `nextConfig`, `ApiResponse`, `geistSans` (+378 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DocumentProcessingError` connect `Community 27` to `Community 1`, `Community 2`, `Community 3`, `Community 5`, `Community 9`, `Community 11`, `Community 19`, `Community 20`, `Community 23`, `Community 25`, `Community 26`, `Community 28`, `Community 31`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Why does `DocumentContent` connect `Community 24` to `Community 32`, `Community 2`, `Community 36`, `Community 6`, `Community 9`, `Community 11`, `Community 19`, `Community 20`, `Community 23`, `Community 57`, `Community 26`, `Community 27`, `Community 28`, `Community 25`, `Community 31`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Why does `ChatService` connect `Community 0` to `Community 1`, `Community 10`, `Community 7`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Are the 45 inferred relationships involving `DocumentProcessingError` (e.g. with `IngestionStage` and `IngestionProgress`) actually correct?**
  _`DocumentProcessingError` has 45 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `load_from_bytes()` (e.g. with `ContentElement` and `DocumentMetadata`) actually correct?**
  _`load_from_bytes()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 26 inferred relationships involving `DocumentContent` (e.g. with `IngestionStage` and `IngestionProgress`) actually correct?**
  _`DocumentContent` has 26 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `ContentElement` (e.g. with `ChunkBoundaryType` and `ChunkMetadata`) actually correct?**
  _`ContentElement` has 25 INFERRED edges - model-reasoned connections that need verification._