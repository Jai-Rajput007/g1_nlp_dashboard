import Link from "next/link";

export default function Dashboard() {
  return (
    <div className="flex-1 p-6 bg-background">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-2xl font-semibold text-foreground mb-6">
          RAG Dashboard
        </h1>

        {/* Stats Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
          <div className="bg-card border border-border rounded-lg p-4">
            <p className="text-muted-foreground text-sm">Total Documents</p>
            <p className="text-2xl font-bold text-card-foreground mt-1">0</p>
          </div>
          <div className="bg-card border border-border rounded-lg p-4">
            <p className="text-muted-foreground text-sm">Indexed Chunks</p>
            <p className="text-2xl font-bold text-card-foreground mt-1">0</p>
          </div>
          <div className="bg-card border border-border rounded-lg p-4">
            <p className="text-muted-foreground text-sm">Active Models</p>
            <p className="text-2xl font-bold text-card-foreground mt-1">0</p>
          </div>
          <div className="bg-card border border-border rounded-lg p-4">
            <p className="text-muted-foreground text-sm">Queries Today</p>
            <p className="text-2xl font-bold text-card-foreground mt-1">0</p>
          </div>
        </div>

        {/* Quick Actions */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Link
            href="/documents"
            className="group bg-card border border-border rounded-lg p-6 hover:border-primary transition-colors"
          >
            <div className="flex items-center gap-3 mb-3">
              <div className="w-10 h-10 rounded-md bg-accent flex items-center justify-center">
                <svg
                  className="w-5 h-5 text-accent-foreground"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                  />
                </svg>
              </div>
              <h3 className="font-semibold text-card-foreground">Documents</h3>
            </div>
            <p className="text-muted-foreground text-sm">
              Manage uploaded documents, view metadata, and re-index content.
            </p>
          </Link>

          <Link
            href="/chat"
            className="group bg-card border border-border rounded-lg p-6 hover:border-primary transition-colors"
          >
            <div className="flex items-center gap-3 mb-3">
              <div className="w-10 h-10 rounded-md bg-accent flex items-center justify-center">
                <svg
                  className="w-5 h-5 text-accent-foreground"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
                  />
                </svg>
              </div>
              <h3 className="font-semibold text-card-foreground">Chat</h3>
            </div>
            <p className="text-muted-foreground text-sm">
              Ask questions and get answers based on your document knowledge base.
            </p>
          </Link>

          <Link
            href="/upload"
            className="group bg-card border border-border rounded-lg p-6 hover:border-primary transition-colors"
          >
            <div className="flex items-center gap-3 mb-3">
              <div className="w-10 h-10 rounded-md bg-accent flex items-center justify-center">
                <svg
                  className="w-5 h-5 text-accent-foreground"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                  />
                </svg>
              </div>
              <h3 className="font-semibold text-card-foreground">Upload</h3>
            </div>
            <p className="text-muted-foreground text-sm">
              Upload new documents to feed into the RAG knowledge base.
            </p>
          </Link>

          <Link
            href="/settings"
            className="group bg-card border border-border rounded-lg p-6 hover:border-primary transition-colors"
          >
            <div className="flex items-center gap-3 mb-3">
              <div className="w-10 h-10 rounded-md bg-accent flex items-center justify-center">
                <svg
                  className="w-5 h-5 text-accent-foreground"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
                  />
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
              </div>
              <h3 className="font-semibold text-card-foreground">Settings</h3>
            </div>
            <p className="text-muted-foreground text-sm">
              Configure LLM models, embedding models, and system preferences.
            </p>
          </Link>
        </div>
      </div>
    </div>
  );
}
