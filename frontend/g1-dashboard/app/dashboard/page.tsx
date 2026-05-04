"use client";

import Link from "next/link";
import { useState, useEffect } from "react";

function cn(...classes: (string | undefined | null | false)[]) {
  return classes.filter(Boolean).join(" ");
}

const mockStats = {
  totalDocuments: 12,
  indexedChunks: 2847,
  activeModels: 2,
  queriesToday: 48,
  storageUsed: "156 MB",
  storageTotal: "2 GB",
  lastIndexed: "2 hours ago",
};

const mockRecentDocs = [
  { id: 1, name: "Project_Requirements.pdf", size: "2.4 MB", date: "2 hours ago", status: "indexed" },
  { id: 2, name: "Research_Paper.docx", size: "1.1 MB", date: "5 hours ago", status: "indexed" },
  { id: 3, name: "Meeting_Notes.txt", size: "12 KB", date: "1 day ago", status: "indexed" },
  { id: 4, name: "Technical_Specs.md", size: "45 KB", date: "2 days ago", status: "processing" },
];

const mockActivity = [
  { id: 1, action: "Document indexed", target: "Project_Requirements.pdf", time: "2 hours ago", type: "success" },
  { id: 2, action: "Query executed", target: "What are the key features?", time: "3 hours ago", type: "info" },
  { id: 3, action: "Document uploaded", target: "Research_Paper.docx", time: "5 hours ago", type: "success" },
  { id: 4, action: "Chat session", target: "Technical discussion", time: "1 day ago", type: "info" },
];

const mockModelStatus = [
  { name: "llama3.2:latest", type: "LLM", status: "active", lastUsed: "5 min ago" },
  { name: "nomic-embed-text", type: "Embedding", status: "active", lastUsed: "2 hours ago" },
];

export default function Dashboard() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <div className="flex-1 p-6 bg-background">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold text-foreground">Dashboard</h1>
            <p className="text-muted-foreground mt-1">Overview of your RAG system</p>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-sm text-muted-foreground">System Status:</span>
            <span className="flex items-center gap-1.5 px-3 py-1 bg-green-500/10 text-green-600 rounded-full text-sm font-medium">
              <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
              Operational
            </span>
          </div>
        </div>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
          <div className="bg-card border border-border rounded-xl p-5 hover:shadow-md transition-all">
            <div className="flex items-start justify-between">
              <div>
                <p className="text-muted-foreground text-sm">Total Documents</p>
                <p className="text-3xl font-bold text-card-foreground mt-2">{mockStats.totalDocuments}</p>
              </div>
              <div className="w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center">
                <svg className="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
              </div>
            </div>
            <p className="text-sm text-green-600 mt-3">+2 this week</p>
          </div>

          <div className="bg-card border border-border rounded-xl p-5 hover:shadow-md transition-all">
            <div className="flex items-start justify-between">
              <div>
                <p className="text-muted-foreground text-sm">Indexed Chunks</p>
                <p className="text-3xl font-bold text-card-foreground mt-2">{mockStats.indexedChunks.toLocaleString()}</p>
              </div>
              <div className="w-10 h-10 rounded-lg bg-purple-500/10 flex items-center justify-center">
                <svg className="w-5 h-5 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                </svg>
              </div>
            </div>
            <p className="text-sm text-muted-foreground mt-3">Last indexed {mockStats.lastIndexed}</p>
          </div>

          <div className="bg-card border border-border rounded-xl p-5 hover:shadow-md transition-all">
            <div className="flex items-start justify-between">
              <div>
                <p className="text-muted-foreground text-sm">Active Models</p>
                <p className="text-3xl font-bold text-card-foreground mt-2">{mockStats.activeModels}</p>
              </div>
              <div className="w-10 h-10 rounded-lg bg-orange-500/10 flex items-center justify-center">
                <svg className="w-5 h-5 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
              </div>
            </div>
            <p className="text-sm text-muted-foreground mt-3">LLM + Embedding</p>
          </div>

          <div className="bg-card border border-border rounded-xl p-5 hover:shadow-md transition-all">
            <div className="flex items-start justify-between">
              <div>
                <p className="text-muted-foreground text-sm">Queries Today</p>
                <p className="text-3xl font-bold text-card-foreground mt-2">{mockStats.queriesToday}</p>
              </div>
              <div className="w-10 h-10 rounded-lg bg-green-500/10 flex items-center justify-center">
                <svg className="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
              </div>
            </div>
            <p className="text-sm text-green-600 mt-3">+12% from yesterday</p>
          </div>
        </div>

        {/* Main Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Quick Actions */}
          <div className="lg:col-span-2">
            <h2 className="text-lg font-semibold text-foreground mb-4">Quick Actions</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <Link href="/library" className="group bg-card border border-border rounded-xl p-5 hover:border-primary transition-all hover:shadow-md">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-xl bg-blue-500/10 flex items-center justify-center shrink-0">
                    <svg className="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                    </svg>
                  </div>
                  <div>
                    <h3 className="font-semibold text-card-foreground group-hover:text-primary transition-colors">Upload Document</h3>
                    <p className="text-sm text-muted-foreground mt-1">Add new documents to your knowledge base</p>
                  </div>
                </div>
              </Link>

              <Link href="/chat" className="group bg-card border border-border rounded-xl p-5 hover:border-primary transition-all hover:shadow-md">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-xl bg-green-500/10 flex items-center justify-center shrink-0">
                    <svg className="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                    </svg>
                  </div>
                  <div>
                    <h3 className="font-semibold text-card-foreground group-hover:text-primary transition-colors">Start Chat</h3>
                    <p className="text-sm text-muted-foreground mt-1">Ask questions about your documents</p>
                  </div>
                </div>
              </Link>

              <Link href="/settings" className="group bg-card border border-border rounded-xl p-5 hover:border-primary transition-all hover:shadow-md">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-xl bg-orange-500/10 flex items-center justify-center shrink-0">
                    <svg className="w-6 h-6 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                  </div>
                  <div>
                    <h3 className="font-semibold text-card-foreground group-hover:text-primary transition-colors">Configure Models</h3>
                    <p className="text-sm text-muted-foreground mt-1">Update LLM and embedding settings</p>
                  </div>
                </div>
              </Link>

              <Link href="/library" className="group bg-card border border-border rounded-xl p-5 hover:border-primary transition-all hover:shadow-md">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 rounded-xl bg-purple-500/10 flex items-center justify-center shrink-0">
                    <svg className="w-6 h-6 text-purple-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                    </svg>
                  </div>
                  <div>
                    <h3 className="font-semibold text-card-foreground group-hover:text-primary transition-colors">Re-index All</h3>
                    <p className="text-sm text-muted-foreground mt-1">Refresh document embeddings</p>
                  </div>
                </div>
              </Link>
            </div>

            {/* Recent Documents */}
            <div className="mt-6 bg-card border border-border rounded-xl overflow-hidden">
              <div className="p-5 border-b border-border flex items-center justify-between">
                <h2 className="text-lg font-semibold text-card-foreground">Recent Documents</h2>
                <Link href="/library" className="text-sm text-primary hover:underline">View All</Link>
              </div>
              <div className="divide-y divide-border">
                {mockRecentDocs.map((doc) => (
                  <div key={doc.id} className="p-4 flex items-center justify-between hover:bg-accent/50 transition-colors">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center">
                        <svg className="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
                        </svg>
                      </div>
                      <div>
                        <p className="font-medium text-card-foreground">{doc.name}</p>
                        <p className="text-sm text-muted-foreground">{doc.size} • {doc.date}</p>
                      </div>
                    </div>
                    <span className={cn(
                      "px-2.5 py-1 rounded-full text-xs font-medium",
                      doc.status === "indexed" ? "bg-green-500/10 text-green-600" : "bg-yellow-500/10 text-yellow-600"
                    )}>
                      {doc.status}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Right Sidebar */}
          <div className="space-y-6">
            {/* Model Status */}
            <div className="bg-card border border-border rounded-xl overflow-hidden">
              <div className="p-5 border-b border-border">
                <h2 className="text-lg font-semibold text-card-foreground">Model Status</h2>
              </div>
              <div className="p-4 space-y-3">
                {mockModelStatus.map((model, idx) => (
                  <div key={idx} className="flex items-center justify-between p-3 bg-accent/30 rounded-lg">
                    <div>
                      <p className="font-medium text-card-foreground text-sm">{model.name}</p>
                      <p className="text-xs text-muted-foreground">{model.type}</p>
                    </div>
                    <div className="text-right">
                      <span className="flex items-center gap-1.5 text-xs font-medium text-green-600">
                        <span className="w-1.5 h-1.5 rounded-full bg-green-500" />
                        {model.status}
                      </span>
                      <p className="text-xs text-muted-foreground mt-0.5">{model.lastUsed}</p>
                    </div>
                  </div>
                ))}
              </div>
              <div className="p-4 border-t border-border">
                <Link href="/settings" className="text-sm text-primary hover:underline">Manage Models</Link>
              </div>
            </div>

            {/* Storage Usage */}
            <div className="bg-card border border-border rounded-xl p-5">
              <h2 className="text-lg font-semibold text-card-foreground mb-4">Storage Usage</h2>
              <div className="space-y-3">
                <div className="flex items-center justify-between text-sm">
                  <span className="text-muted-foreground">Documents</span>
                  <span className="font-medium text-card-foreground">{mockStats.storageUsed}</span>
                </div>
                <div className="w-full h-2 bg-accent rounded-full overflow-hidden">
                  <div className="h-full bg-blue-500 rounded-full" style={{ width: "7.8%" }} />
                </div>
                <p className="text-xs text-muted-foreground">
                  Using {mockStats.storageUsed} of {mockStats.storageTotal} ({Math.round((156/2048)*100)}%)
                </p>
              </div>
            </div>

            {/* Recent Activity */}
            <div className="bg-card border border-border rounded-xl overflow-hidden">
              <div className="p-5 border-b border-border">
                <h2 className="text-lg font-semibold text-card-foreground">Recent Activity</h2>
              </div>
              <div className="p-4 space-y-4">
                {mockActivity.map((activity) => (
                  <div key={activity.id} className="flex gap-3">
                    <div className={cn(
                      "w-8 h-8 rounded-full flex items-center justify-center shrink-0",
                      activity.type === "success" ? "bg-green-500/10" : "bg-blue-500/10"
                    )}>
                      <svg className={cn(
                        "w-4 h-4",
                        activity.type === "success" ? "text-green-500" : "text-blue-500"
                      )} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        {activity.type === "success" ? (
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                        ) : (
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        )}
                      </svg>
                    </div>
                    <div className="min-w-0">
                      <p className="text-sm font-medium text-card-foreground">{activity.action}</p>
                      <p className="text-xs text-muted-foreground truncate">{activity.target}</p>
                      <p className="text-xs text-muted-foreground mt-0.5">{activity.time}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
