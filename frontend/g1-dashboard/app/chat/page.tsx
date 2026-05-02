"use client";

import { useState } from "react";

export default function Chat() {
  const [messages, setMessages] = useState<{ role: "user" | "assistant"; content: string }[]>([]);
  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages([...messages, { role: "user", content: input }]);
    setInput("");
    // TODO: Send to backend
  };

  return (
    <div className="flex-1 flex flex-col bg-background h-[calc(100vh-7rem)]">
      <div className="max-w-4xl mx-auto w-full flex-1 flex flex-col">
        {/* Header */}
        <div className="p-4 border-b border-border">
          <h1 className="text-xl font-semibold text-foreground">Chat with your Documents</h1>
          <p className="text-muted-foreground text-sm">Ask questions about your uploaded documents</p>
        </div>

        {/* Messages */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-center p-8">
              <div className="w-16 h-16 rounded-xl bg-accent flex items-center justify-center mb-4">
                <svg className="w-8 h-8 text-accent-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-card-foreground mb-2">Start a conversation</h3>
              <p className="text-muted-foreground max-w-sm">
                Ask questions about your documents and get AI-powered answers with source citations
              </p>
              <div className="flex flex-wrap gap-2 mt-6 justify-center">
                <button className="px-3 py-1.5 bg-accent text-accent-foreground rounded-full text-sm hover:opacity-80 transition-all">
                  Summarize my documents
                </button>
                <button className="px-3 py-1.5 bg-accent text-accent-foreground rounded-full text-sm hover:opacity-80 transition-all">
                  What are the key insights?
                </button>
                <button className="px-3 py-1.5 bg-accent text-accent-foreground rounded-full text-sm hover:opacity-80 transition-all">
                  Find related topics
                </button>
              </div>
            </div>
          ) : (
            messages.map((msg, i) => (
              <div
                key={i}
                className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
              >
                <div
                  className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                    msg.role === "user"
                      ? "bg-primary text-primary-foreground rounded-br-md"
                      : "bg-card border border-border text-card-foreground rounded-bl-md"
                  }`}
                >
                  {msg.content}
                </div>
              </div>
            ))
          )}
        </div>

        {/* Input */}
        <div className="p-4 border-t border-border">
          <div className="flex gap-2">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              placeholder="Ask anything about your documents..."
              className="flex-1 px-4 py-3 bg-card border border-border rounded-xl text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary/50"
            />
            <button
              onClick={sendMessage}
              className="px-6 py-3 bg-primary text-primary-foreground rounded-xl font-medium hover:opacity-90 transition-all"
            >
              Send
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
