"use client";

import { useState } from "react";

export default function Library() {
  const [documents, setDocuments] = useState([]);

  return (
    <div className="flex-1 p-6 bg-background">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1 className="text-2xl font-semibold text-foreground">Library</h1>
            <p className="text-muted-foreground mt-1">Manage your documents and knowledge base</p>
          </div>
          <button className="px-4 py-2 bg-primary text-primary-foreground rounded-lg font-medium hover:opacity-90 transition-all flex items-center gap-2">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
            </svg>
            Upload Document
          </button>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
          <div className="bg-card border border-border rounded-xl p-4">
            <p className="text-muted-foreground text-sm">Total Documents</p>
            <p className="text-3xl font-bold text-card-foreground mt-1">{documents.length}</p>
          </div>
          <div className="bg-card border border-border rounded-xl p-4">
            <p className="text-muted-foreground text-sm">Total Size</p>
            <p className="text-3xl font-bold text-card-foreground mt-1">0 MB</p>
          </div>
          <div className="bg-card border border-border rounded-xl p-4">
            <p className="text-muted-foreground text-sm">Last Upload</p>
            <p className="text-lg font-medium text-card-foreground mt-1">Never</p>
          </div>
        </div>

        {/* Empty State */}
        {documents.length === 0 && (
          <div className="bg-card border border-border border-dashed rounded-2xl p-12 text-center">
            <div className="w-16 h-16 rounded-xl bg-accent flex items-center justify-center mx-auto mb-4">
              <svg className="w-8 h-8 text-accent-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20" />
              </svg>
            </div>
            <h3 className="text-lg font-semibold text-card-foreground mb-2">No documents yet</h3>
            <p className="text-muted-foreground max-w-md mx-auto mb-6">
              Upload your first document to start building your knowledge base. Supported formats: PDF, DOCX, TXT, MD
            </p>
            <button className="px-6 py-3 bg-primary text-primary-foreground rounded-lg font-medium hover:opacity-90 transition-all">
              Upload Your First Document
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
