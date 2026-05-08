# Graph Report - .  (2026-05-08)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 634 nodes · 1189 edges · 41 communities (32 shown, 9 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 226 edges (avg confidence: 0.56)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `603df12b`
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
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]

## God Nodes (most connected - your core abstractions)
1. `load_from_bytes()` - 40 edges
2. `ContentElement` - 31 edges
3. `ChatService` - 27 edges
4. `DocumentContent` - 26 edges
5. `DocumentProcessingError` - 26 edges
6. `Chat()` - 24 edges
7. `MarkdownLoader` - 22 edges
8. `ApiClient` - 20 edges
9. `load()` - 20 edges
10. `DOCXLoader` - 20 edges

## Surprising Connections (you probably didn't know these)
- `DocumentStatus` --uses--> `IngestionStage`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/services/ingestion_pipeline.py
- `DocumentStatus` --uses--> `IngestionProgress`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/services/ingestion_pipeline.py
- `DocumentStatus` --uses--> `DashboardStats`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/api/v1/endpoints/dashboard.py
- `DocumentStatus` --uses--> `DashboardResponse`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/api/v1/endpoints/dashboard.py
- `Document` --uses--> `IngestionStage`  [INFERRED]
  frontend/g1-dashboard/app/library/page.tsx → backend/app/services/ingestion_pipeline.py

## Communities (41 total, 9 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (44): ContentType, DocumentContent, DocumentMetadata, ElementType, Base document loader interface., Get all image elements., Split document into text chunks., Types of content elements. (+36 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (49): Dashboard(), can_load_file(), get_all_supported_extensions(), get_langchain_extensions(), _get_langchain_loader(), get_loader_for_file(), get_supported_extensions(), Document loader factory for getting appropriate loader. (+41 more)

### Community 2 - "Community 2"
Cohesion: 0.05
Nodes (50): ConfigurationError, DocumentProcessingError, FileUploadError, NotFoundError, RAGSystemException, Custom application exceptions., Raised when document processing fails., Raised when vector database operation fails. (+42 more)

### Community 3 - "Community 3"
Cohesion: 0.11
Nodes (31): ABC, EmbeddingError, LLMError, Raised when LLM operation fails., Raised when embedding generation fails., embed(), embed_query(), EmbeddingProvider (+23 more)

### Community 4 - "Community 4"
Cohesion: 0.09
Nodes (21): Build context using specified strategy., AssembledContext, ContextChunk, ContextStrategy, Context builder service for assembling retrieved chunks into LLM context., Convert retrieval results to context chunks., Strategies for building context., Build context grouped by hierarchy. (+13 more)

### Community 5 - "Community 5"
Cohesion: 0.12
Nodes (18): Chat(), chat_stream(), Stream chat response with RAG., Send a chat message and get AI response with RAG., ChatService, Chat service for RAG-based conversations using Ollama with query processing and, Apply filters extracted from query to request., Build system prompt for RAG. (+10 more)

### Community 6 - "Community 6"
Cohesion: 0.12
Nodes (14): Process user query to extract intent and filters., ExtractedFilter, ProcessedQuery, Query processing service for understanding user questions and extracting filters, Process a user query to extract intent and filters.                  Args:, Clean and normalize query., Detect query intent using pattern matching., Extract important keywords from query. (+6 more)

### Community 7 - "Community 7"
Cohesion: 0.15
Nodes (21): BaseModel, Source, list_models(), Chat API endpoints with RAG using Ollama., List available LLM models from Ollama., Chat request schema with query processing, hierarchy, and context building suppo, ChatMessage, ChatRequest (+13 more)

### Community 8 - "Community 8"
Cohesion: 0.11
Nodes (13): geistMono, geistSans, metadata, defaultNavItems, LimelightNav(), LimelightNavProps, NavItem, Theme (+5 more)

### Community 9 - "Community 9"
Cohesion: 0.12
Nodes (12): Base, Vector database service using pgvector., Fallback method for adding documents when PostgreSQL is not available., Search for similar chunks using cosine similarity., Vector chunk model for pgvector storage., Fallback search using cosine similarity calculation., No-op for pgvector (automatic persistence)., Vector database service using pgvector for PostgreSQL. (+4 more)

### Community 10 - "Community 10"
Cohesion: 0.13
Nodes (10): Retrieval service for hybrid search with metadata filtering and hierarchy., Service for hybrid retrieval with prefiltering, hierarchy, and vector search., Build prefilter dictionary from query filters.         These filters are applied, Apply post-filters that couldn't be applied in prefiltering., Enrich result with hierarchy information from metadata., Perform hybrid retrieval with prefiltering and vector search.                  F, Retrieve using hierarchy-based filtering.                  Args:             que, Retrieve with parent section context for each result.                  This is u (+2 more)

### Community 11 - "Community 11"
Cohesion: 0.14
Nodes (14): load_from_bytes(), CSVLoader, CSV document loader with table structure support., Detect CSV delimiter from sample., Parse CSV text into rows and headers., Calculate basic statistics for numeric columns., Format CSV as readable text., CSV loader with table structure extraction. (+6 more)

### Community 12 - "Community 12"
Cohesion: 0.16
Nodes (13): Extract images from document., Detect if line is a heading., PDFLoader, PDF document loader with support for images, tables, and structured content., Extract content from a single page., Heuristic to detect if a line is a heading., PDF loader with comprehensive content extraction., Detect heading level. (+5 more)

### Community 13 - "Community 13"
Cohesion: 0.15
Nodes (10): DOCXLoader, DOCX document loader with support for images, tables, lists, and formatting., Check if list item is part of ordered list., Extract text from paragraph with run formatting., DOCX loader with comprehensive content extraction., Process a paragraph into a content element., Detect code block by style., Detect quote by style. (+2 more)

### Community 14 - "Community 14"
Cohesion: 0.21
Nodes (7): MarkdownLoader, Markdown document loader with support for all MD elements., Markdown loader with full syntax support., Check if line is part of a table., Check if line is a list item., Parse image reference., Parse Markdown into structured elements.

### Community 15 - "Community 15"
Cohesion: 0.17
Nodes (14): Activity, ModelStatus, ActivityItem, Recent document schema., Activity item schema., RecentDocument, DocumentStatus, ActivityType (+6 more)

### Community 16 - "Community 16"
Cohesion: 0.17
Nodes (10): Check if paragraph is a list item., create_langchain_loader(), LangChainLoaderWrapper, LangChain document loader wrapper for fallback format support., Parse content and try to detect structure., Wrapper for LangChain document loaders to adapt to our format., Detect if line is a list item., Remove list marker from line. (+2 more)

### Community 17 - "Community 17"
Cohesion: 0.18
Nodes (10): Message, suggestedPrompts, Stats, api, ApiResponse, cn(), fileTypeIcons, Library() (+2 more)

### Community 18 - "Community 18"
Cohesion: 0.21
Nodes (8): ContentElement, Abstract base class for document loaders., Check if loader can handle file., Helper to create text element., Helper to create list element., Helper to create image element., Represents a single content element., DocumentLoader

### Community 19 - "Community 19"
Cohesion: 0.15
Nodes (12): BaseSettings, Application settings with environment variable support., Settings, get_settings(), Settings API endpoints., Settings response schema., Settings update schema., Get current settings. (+4 more)

### Community 20 - "Community 20"
Cohesion: 0.2
Nodes (8): Document, Convert to dictionary., Format timestamp for display., Document model for storing uploaded files., Format file size for display., Format date for display., Convert to dictionary for API response., Base document schema.

### Community 21 - "Community 21"
Cohesion: 0.18
Nodes (6): Config, Application configuration management., DocumentCreate, DocumentResponse, Document creation schema., Document response schema.

### Community 22 - "Community 22"
Cohesion: 0.18
Nodes (3): CardItem, ExpandingCards, robotFeatures

### Community 23 - "Community 23"
Cohesion: 0.22
Nodes (6): JSONLoader, JSON document loader with structure preservation., JSON loader with structured content extraction., Flatten JSON to readable text., Parse JSON Lines format., Parse JSON structure into content elements.

### Community 24 - "Community 24"
Cohesion: 0.22
Nodes (9): load(), Load CSV from file path., Load DOCX from file path., Load HTML from file path., Load JSON from file path., Load using LangChain loader., Load Markdown from file path., Load PDF from file path. (+1 more)

### Community 25 - "Community 25"
Cohesion: 0.28
Nodes (7): detailed_health(), HealthResponse, Health check endpoints., Health check response., System status response., Detailed system health check., SystemStatus

### Community 26 - "Community 26"
Cohesion: 0.29
Nodes (5): Build retrieval query with hierarchy and prefiltering., HierarchyQuery, Query for hierarchy-based retrieval., Query for retrieval with prefiltering and hierarchy., RetrievalQuery

### Community 27 - "Community 27"
Cohesion: 0.29
Nodes (5): Extract DOCX metadata., Extract metadata from LangChain documents., Extract YAML frontmatter metadata., Extract PDF metadata., Parse keywords from metadata.

### Community 28 - "Community 28"
Cohesion: 0.29
Nodes (5): get_db(), init_db(), Database connection and session management., Get database session., Initialize database tables.

### Community 29 - "Community 29"
Cohesion: 0.4
Nodes (4): create_application(), FastAPI application factory., Create and configure FastAPI application., Main application entry point.

### Community 30 - "Community 30"
Cohesion: 0.5
Nodes (3): Logging configuration., Configure application logging., setup_logging()

## Knowledge Gaps
- **318 isolated node(s):** `nextConfig`, `ApiResponse`, `geistSans`, `geistMono`, `metadata` (+313 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DocumentProcessingError` connect `Community 2` to `Community 0`, `Community 1`, `Community 11`, `Community 12`, `Community 13`, `Community 14`, `Community 16`, `Community 23`, `Community 24`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Why does `LangChainLoaderWrapper` connect `Community 16` to `Community 0`, `Community 2`, `Community 3`, `Community 11`, `Community 12`, `Community 18`, `Community 24`, `Community 27`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `DocumentContent` connect `Community 0` to `Community 2`, `Community 11`, `Community 12`, `Community 13`, `Community 14`, `Community 16`, `Community 20`, `Community 23`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `load_from_bytes()` (e.g. with `ContentElement` and `DocumentMetadata`) actually correct?**
  _`load_from_bytes()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 22 inferred relationships involving `ContentElement` (e.g. with `structure_aware_chunker.py` and `ChunkBoundaryType`) actually correct?**
  _`ContentElement` has 22 INFERRED edges - model-reasoned connections that need verification._
- **Are the 10 inferred relationships involving `ChatService` (e.g. with `FilterOperator` and `MetadataFilter`) actually correct?**
  _`ChatService` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `DocumentContent` (e.g. with `ingestion_pipeline.py` and `IngestionStage`) actually correct?**
  _`DocumentContent` has 17 INFERRED edges - model-reasoned connections that need verification._