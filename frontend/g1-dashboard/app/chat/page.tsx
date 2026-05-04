"use client";

import { useState, useRef, useEffect } from "react";

function cn(...classes: (string | undefined | null | false)[]) {
  return classes.filter(Boolean).join(" ");
}

interface Source {
  id: string;
  document: string;
  page?: number;
  excerpt: string;
  score: number;
}

interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  sources?: Source[];
  isStreaming?: boolean;
  timestamp: Date;
}

const suggestedPrompts = [
  "Summarize my documents",
  "What are the key insights?",
  "Find related topics",
  "Explain the technical architecture",
  "Compare different approaches",
];

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [showSources, setShowSources] = useState<string | null>(null);
  const [selectedModel, setSelectedModel] = useState("llama3.2:latest");
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async (promptText?: string) => {
    const text = promptText || input;
    if (!text.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      role: "user",
      content: text,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    // TODO: Connect to backend API for RAG response
    const assistantId = (Date.now() + 1).toString();
    const assistantMessage: Message = {
      id: assistantId,
      role: "assistant",
      content: "",
      isStreaming: true,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, assistantMessage]);

    // Simulate streaming until backend is ready
    const response = "This is a placeholder response. Backend integration needed for actual RAG responses with document sources.";
    
    let currentContent = "";
    for (let i = 0; i < response.length; i += 3) {
      await new Promise((resolve) => setTimeout(resolve, 30));
      currentContent += response.slice(i, i + 3);
      setMessages((prev) =>
        prev.map((msg) =>
          msg.id === assistantId
            ? { ...msg, content: currentContent }
            : msg
        )
      );
    }

    setMessages((prev) =>
      prev.map((msg) =>
        msg.id === assistantId ? { ...msg, isStreaming: false } : msg
      )
    );
    setIsLoading(false);
  };

  const clearChat = () => {
    setMessages([]);
    setShowSources(null);
  };

  return (
    <div className="flex-1 flex bg-background h-[calc(100vh-7rem)]">
      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col max-w-4xl mx-auto w-full">
        {/* Header */}
        <div className="p-4 border-b border-border flex items-center justify-between">
          <div>
            <h1 className="text-xl font-semibold text-foreground">Chat with your Documents</h1>
            <p className="text-muted-foreground text-sm">Ask questions about your uploaded documents</p>
          </div>
          <div className="flex items-center gap-3">
            <select
              value={selectedModel}
              onChange={(e) => setSelectedModel(e.target.value)}
              className="px-3 py-1.5 bg-card border border-border rounded-lg text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-primary/20"
            >
              <option value="llama3.2:latest">llama3.2:latest</option>
              <option value="mistral:latest">mistral:latest</option>
              <option value="gemma:2b">gemma:2b</option>
            </select>
            {messages.length > 0 && (
              <button
                onClick={clearChat}
                className="p-2 text-muted-foreground hover:text-red-500 hover:bg-red-500/10 rounded-lg transition-colors"
                title="Clear chat"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            )}
          </div>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-6">
          {messages.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-center p-8">
              <div className="w-16 h-16 rounded-xl bg-accent flex items-center justify-center mb-4">
                <svg className="w-8 h-8 text-accent-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-card-foreground mb-2">Start a conversation</h3>
              <p className="text-muted-foreground max-w-sm">
                Ask questions about your documents and get AI-powered answers with source citations
              </p>
              <div className="flex flex-wrap gap-2 mt-6 justify-center max-w-md">
                {suggestedPrompts.map((prompt, idx) => (
                  <button
                    key={idx}
                    onClick={() => sendMessage(prompt)}
                    className="px-4 py-2 bg-accent text-accent-foreground rounded-full text-sm hover:opacity-80 transition-all"
                  >
                    {prompt}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            messages.map((msg) => (
              <div key={msg.id} className={cn("flex", msg.role === "user" ? "justify-end" : "justify-start")}>
                <div className={cn(
                  "max-w-[85%] space-y-3",
                  msg.role === "user" ? "items-end" : "items-start"
                )}>
                  {/* Message Bubble */}
                  <div className={cn(
                    "rounded-2xl px-4 py-3",
                    msg.role === "user"
                      ? "bg-primary text-primary-foreground rounded-br-md"
                      : "bg-card border border-border text-card-foreground rounded-bl-md"
                  )}>
                    <p className="whitespace-pre-wrap leading-relaxed">{msg.content}</p>
                    {msg.isStreaming && (
                      <span className="inline-block w-2 h-4 bg-current ml-1 animate-pulse" />
                    )}
                  </div>

                  {/* Sources for Assistant Messages */}
                  {msg.role === "assistant" && msg.sources && !msg.isStreaming && (
                    <div className="flex items-center gap-2">
                      <button
                        onClick={() => setShowSources(showSources === msg.id ? null : msg.id)}
                        className="flex items-center gap-1.5 px-3 py-1.5 bg-accent rounded-full text-xs text-accent-foreground hover:opacity-80 transition-all"
                      >
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                        {msg.sources.length} Sources
                        <svg className={cn("w-3 h-3 transition-transform", showSources === msg.id && "rotate-180")} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                        </svg>
                      </button>
                      <span className="text-xs text-muted-foreground">
                        {msg.timestamp.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
                      </span>
                    </div>
                  )}

                  {/* Expanded Sources */}
                  {showSources === msg.id && msg.sources && (
                    <div className="mt-2 space-y-2">
                      {msg.sources.map((source) => (
                        <div key={source.id} className="bg-accent/50 rounded-xl p-3 border border-border">
                          <div className="flex items-center justify-between mb-1">
                            <span className="text-sm font-medium text-card-foreground flex items-center gap-2">
                              <svg className="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                              </svg>
                              {source.document}
                              {source.page && <span className="text-muted-foreground">• Page {source.page}</span>}
                            </span>
                            <span className="text-xs text-green-600 font-medium">{(source.score * 100).toFixed(0)}% match</span>
                          </div>
                          <p className="text-sm text-muted-foreground line-clamp-2">{source.excerpt}</p>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input */}
        <div className="p-4 border-t border-border">
          <div className="relative">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  sendMessage();
                }
              }}
              placeholder="Ask anything about your documents... (Shift+Enter for new line)"
              rows={1}
              className="w-full px-4 py-3 pr-24 bg-card border border-border rounded-xl text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary/50 resize-none"
              style={{ minHeight: "56px", maxHeight: "200px" }}
            />
            <div className="absolute right-2 bottom-2 flex items-center gap-2">
              <span className="text-xs text-muted-foreground hidden sm:block">{input.length} chars</span>
              <button
                onClick={() => sendMessage()}
                disabled={!input.trim() || isLoading}
                className={cn(
                  "px-4 py-2 rounded-lg font-medium transition-all",
                  input.trim() && !isLoading
                    ? "bg-primary text-primary-foreground hover:opacity-90"
                    : "bg-muted text-muted-foreground cursor-not-allowed"
                )}
              >
                {isLoading ? (
                  <svg className="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                  </svg>
                ) : (
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                  </svg>
                )}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
