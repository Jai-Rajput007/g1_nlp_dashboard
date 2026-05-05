"""Chat service for RAG-based conversations using Ollama with query processing and enhanced context building."""

from typing import List, Optional, Dict, Any, AsyncGenerator
from dataclasses import dataclass, field
import aiohttp
import json

from app.core.config import settings
from app.core.logging import logger
from app.services.retrieval_service import (
    retrieval_service, RetrievalQuery, RetrievalResult,
    MetadataFilter, FilterOperator, HierarchyQuery
)
from app.services.query_processing_service import (
    query_processing_service, QueryIntent, ProcessedQuery, ExtractedFilter
)
from app.services.context_builder_service import (
    context_builder_service, ContextStrategy, AssembledContext
)


@dataclass
class ChatMessage:
    """Chat message."""
    role: str  # "user" or "assistant"
    content: str
    sources: Optional[List[Dict[str, Any]]] = None


@dataclass
class ChatRequest:
    """Chat request with query processing, hierarchy, and context building support."""
    message: str
    document_ids: Optional[List[str]] = None
    metadata_filters: Optional[Dict[str, Any]] = None
    
    # Query processing
    enable_query_processing: bool = True  # Enable intent detection and filter extraction
    use_extracted_filters: bool = True  # Use filters extracted from query
    
    # Hierarchy retrieval
    section_path: Optional[str] = None
    parent_section: Optional[str] = None
    heading_level: Optional[int] = None
    include_parent_context: bool = True
    
    # Content type filtering
    content_types: Optional[List[str]] = None  # "table", "list", "code", "heading"
    
    # Prefiltering operators
    advanced_filters: List[MetadataFilter] = field(default_factory=list)
    
    # Context building strategy
    context_strategy: str = "hierarchy"  # "standard", "hierarchy", "relevance", "chronological", "compress"
    include_metadata_in_context: bool = True
    include_hierarchy_in_context: bool = True
    
    top_k: int = None
    stream: bool = True
    
    def __post_init__(self):
        if self.top_k is None:
            self.top_k = settings.TOP_K


@dataclass
class ChatResponse:
    """Chat response with answer and sources."""
    response: str
    sources: List[Dict[str, Any]]
    model: str
    tokens_used: Optional[int] = None


class ChatService:
    """Chat service for RAG-based conversations using Ollama with query processing and enhanced context."""
    
    def __init__(self):
        self.ollama_base_url = "http://localhost:11434"
        self.model = settings.LLM_MODEL
        self.retrieval = retrieval_service
        self.query_processor = query_processing_service
        self.context_builder = context_builder_service
    
    def _process_query(self, request: ChatRequest) -> ProcessedQuery:
        """Process user query to extract intent and filters."""
        if not request.enable_query_processing:
            # Return basic processed query without analysis
            return ProcessedQuery(
                original_query=request.message,
                cleaned_query=request.message,
                intent=QueryIntent.SEARCH,
                confidence=0.5
            )
        
        processed = self.query_processor.process_query(request.message)
        logger.info(f"Query intent: {processed.intent.value}, confidence: {processed.confidence:.2f}")
        return processed
    
    def _apply_extracted_filters(self, request: ChatRequest, processed: ProcessedQuery) -> ChatRequest:
        """Apply filters extracted from query to request."""
        if not request.use_extracted_filters or not processed.extracted_filters:
            return request
        
        # Merge extracted filters with explicit filters
        for extracted in processed.extracted_filters:
            if extracted.confidence > 0.7:  # Only high confidence filters
                if extracted.field == "section_path" and not request.section_path:
                    request.section_path = extracted.value
                    logger.info(f"Applied extracted section_path: {extracted.value}")
                elif extracted.field == "content_type" and not request.content_types:
                    request.content_types = [extracted.value]
                    logger.info(f"Applied extracted content_type: {extracted.value}")
        
        # Apply suggested filters from intent analysis
        if processed.suggested_content_types and not request.content_types:
            request.content_types = processed.suggested_content_types
            logger.info(f"Applied suggested content_types: {processed.suggested_content_types}")
        
        return request
    
    def _build_context(self, results: List[RetrievalResult], request: ChatRequest) -> AssembledContext:
        """Build context using specified strategy."""
        strategy_map = {
            "standard": ContextStrategy.STANDARD,
            "hierarchy": ContextStrategy.HIERARCHY,
            "relevance": ContextStrategy.RELEVANCE,
            "chronological": ContextStrategy.CHRONOLOGICAL,
            "compress": ContextStrategy.COMPRESS,
        }
        
        strategy = strategy_map.get(request.context_strategy, ContextStrategy.HIERARCHY)
        
        assembled = self.context_builder.build_context(
            results=results,
            strategy=strategy,
            include_metadata=request.include_metadata_in_context,
            include_hierarchy=request.include_hierarchy_in_context
        )
        
        logger.info(f"Built context with {assembled.total_chunks} chunks, "
                   f"{assembled.total_chars} chars, ~{assembled.estimated_tokens} tokens")
        
        return assembled
    
    def _build_system_prompt(self, has_hierarchy: bool = False) -> str:
        """Build system prompt for RAG."""
        base = settings.LLM_SYSTEM_PROMPT or """You are a helpful AI assistant. Answer questions based on the provided context.

Instructions:
1. Use only the information provided in the context
2. If the context doesn't contain enough information, say so clearly
3. Cite sources using [Source X] format when providing information
4. Be concise but thorough
5. If multiple sources provide conflicting information, mention the discrepancy"""
        
        if has_hierarchy:
            base += """

Document Structure Awareness:
- The context is organized by document and section hierarchy
- Sources show their section path (e.g., "Chapter 1 > Introduction")
- Consider the document structure when synthesizing answers
- Parent sections provide broader context for specific details"""
        
        return base
    
    def _build_user_prompt(self, query: str, context: str) -> str:
        """Build user prompt with context."""
        return f"""Context from retrieved documents:
{context}

---

Question: {query}

Please answer based on the context above. Cite sources using [Source X] format."""
    
    def _build_retrieval_query(self, request: ChatRequest) -> RetrievalQuery:
        """Build retrieval query with hierarchy and prefiltering."""
        
        # Build advanced filters from simple metadata_filters
        advanced_filters = list(request.advanced_filters)
        
        if request.metadata_filters:
            for key, value in request.metadata_filters.items():
                advanced_filters.append(MetadataFilter(
                    field=key,
                    value=value,
                    operator=FilterOperator.EQ
                ))
        
        # Build hierarchy query
        hierarchy = None
        if request.section_path or request.parent_section or request.heading_level:
            hierarchy = HierarchyQuery(
                section_path=request.section_path,
                parent_section=request.parent_section,
                heading_level=request.heading_level,
                include_children=True,
                include_parents=request.include_parent_context,
            )
        
        return RetrievalQuery(
            query=request.message,
            top_k=request.top_k,
            document_ids=request.document_ids,
            metadata_prefilters=advanced_filters,
            hierarchy=hierarchy,
            content_types=request.content_types,
        )
    
    async def chat(
        self,
        request: ChatRequest
    ) -> ChatResponse:
        """
        Process chat request with query processing, RAG, hierarchy, and enhanced context building.
        
        Flow:
        1. Process query to extract intent and filters
        2. Apply extracted filters to request
        3. Retrieve relevant chunks
        4. Build optimized context using strategy
        5. Generate response with Ollama
        
        Args:
            request: ChatRequest with message, hierarchy, and filters
            
        Returns:
            ChatResponse with answer and sources
        """
        logger.info(f"Processing chat request: {request.message[:50]}...")
        
        # Step 1: Process query to understand intent and extract filters
        processed = self._process_query(request)
        
        # Step 2: Apply extracted filters if enabled
        if request.use_extracted_filters:
            request = self._apply_extracted_filters(request, processed)
        
        if request.section_path:
            logger.info(f"Section filter: {request.section_path}")
        
        # Step 3: Build retrieval query and retrieve results
        retrieval_query = self._build_retrieval_query(request)
        
        if request.include_parent_context and (request.section_path or request.parent_section):
            results = await self.retrieval.retrieve_with_parent_context(
                retrieval_query,
                include_parent_summary=True
            )
        else:
            results = await self.retrieval.retrieve(retrieval_query)
        
        # Step 4: Build optimized context
        assembled = self._build_context(results, request)
        
        # Step 5: Build prompts and generate response
        system_prompt = self._build_system_prompt(
            has_hierarchy=bool(request.section_path or request.parent_section)
        )
        user_prompt = self._build_user_prompt(processed.cleaned_query, assembled.context_text)
        
        # Call Ollama
        response_text = await self._call_ollama(system_prompt, user_prompt)
        
        return ChatResponse(
            response=response_text,
            sources=assembled.sources,
            model=self.model,
        )
    
    def _build_system_prompt_with_hierarchy(self, has_hierarchy: bool = False) -> str:
        """Build system prompt with hierarchy awareness."""
        base_prompt = settings.LLM_SYSTEM_PROMPT or """You are a helpful AI assistant. Answer questions based on the provided context.

Instructions:
1. Use only the information provided in the context
2. If the context doesn't contain enough information, say so clearly
3. Cite sources using [Source X] format when providing information
4. Be concise but thorough
5. If multiple sources provide conflicting information, mention the discrepancy"""
        
        if has_hierarchy:
            hierarchy_note = """

Hierarchy Awareness:
- The context includes section paths and parent-child relationships
- Sources may be from specific sections within documents
- Consider the section hierarchy when interpreting context
- Parent section info is provided for broader context
"""
            base_prompt += hierarchy_note
        
        return base_prompt
    
    async def chat_stream(
        self,
        request: ChatRequest
    ) -> AsyncGenerator[str, None]:
        """
        Stream chat response with query processing, RAG, hierarchy, and enhanced context.
        
        Args:
            request: ChatRequest with message, hierarchy, and filters
            
        Yields:
            Chunks of the response
        """
        logger.info(f"Processing streaming chat request: {request.message[:50]}...")
        
        # Step 1: Process query
        processed = self._process_query(request)
        
        # Step 2: Apply extracted filters
        if request.use_extracted_filters:
            request = self._apply_extracted_filters(request, processed)
        
        if request.section_path:
            logger.info(f"Section filter: {request.section_path}")
        
        # Step 3: Retrieve results
        retrieval_query = self._build_retrieval_query(request)
        
        if request.include_parent_context and (request.section_path or request.parent_section):
            results = await self.retrieval.retrieve_with_parent_context(
                retrieval_query,
                include_parent_summary=True
            )
        else:
            results = await self.retrieval.retrieve(retrieval_query)
        
        # Step 4: Build optimized context
        assembled = self._build_context(results, request)
        
        # Step 5: Build prompts and stream
        system_prompt = self._build_system_prompt(
            has_hierarchy=bool(request.section_path or request.parent_section)
        )
        user_prompt = self._build_user_prompt(processed.cleaned_query, assembled.context_text)
        
        async for chunk in self._call_ollama_stream(system_prompt, user_prompt):
            yield chunk
    
    async def _call_ollama(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """Call Ollama API for completion."""
        url = f"{self.ollama_base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": user_prompt,
            "system": system_prompt,
            "stream": False,
            "options": {
                "temperature": settings.LLM_TEMPERATURE,
                "top_p": settings.LLM_TOP_P,
                "num_predict": settings.LLM_MAX_TOKENS,
            }
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise Exception(f"Ollama API error: {error_text}")
                    
                    data = await response.json()
                    return data.get("response", "")
        except Exception as e:
            logger.error(f"Ollama API call failed: {e}")
            return f"Error: Failed to get response from LLM. {str(e)}"
    
    async def _call_ollama_stream(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> AsyncGenerator[str, None]:
        """Stream from Ollama API."""
        url = f"{self.ollama_base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": user_prompt,
            "system": system_prompt,
            "stream": True,
            "options": {
                "temperature": settings.LLM_TEMPERATURE,
                "top_p": settings.LLM_TOP_P,
                "num_predict": settings.LLM_MAX_TOKENS,
            }
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        yield f"Error: Ollama API error: {error_text}"
                        return
                    
                    async for line in response.content:
                        if line:
                            try:
                                data = json.loads(line)
                                if "response" in data:
                                    yield data["response"]
                                if data.get("done", False):
                                    break
                            except json.JSONDecodeError:
                                continue
        except Exception as e:
            logger.error(f"Ollama streaming failed: {e}")
            yield f"Error: Failed to stream from LLM. {str(e)}"
    
    async def get_available_models(self) -> List[Dict[str, str]]:
        """Get list of available models from Ollama."""
        url = f"{self.ollama_base_url}/api/tags"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        return [{"id": self.model, "name": self.model}]
                    
                    data = await response.json()
                    models = data.get("models", [])
                    return [
                        {"id": m["name"], "name": m["name"].replace(":latest", "")}
                        for m in models
                    ]
        except Exception as e:
            logger.error(f"Failed to get models: {e}")
            return [{"id": self.model, "name": self.model}]


# Global instance
chat_service = ChatService()
