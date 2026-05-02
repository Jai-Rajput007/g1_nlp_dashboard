"use client";

import { useState } from "react";

export default function Settings() {
  const [activeTab, setActiveTab] = useState("general");

  return (
    <div className="flex-1 p-6 bg-background">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-2xl font-semibold text-foreground mb-6">Settings</h1>

        <div className="flex flex-col md:flex-row gap-6">
          {/* Sidebar */}
          <div className="w-full md:w-48 space-y-1">
            {[
              { id: "general", label: "General", icon: "M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z M15 12a3 3 0 11-6 0 3 3 0 016 0z" },
              { id: "models", label: "Models", icon: "M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" },
              { id: "database", label: "Database", icon: "M4 7v10c0 2 1.5 3 3 3h10c1.5 0 3-1 3-3V7c0-2-1.5-3-3-3H7c-1.5 0-3 1-3 3z M9 12h6" },
              { id: "api", label: "API Keys", icon: "M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z" },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`w-full flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm font-medium transition-all ${
                  activeTab === tab.id
                    ? "bg-accent text-accent-foreground"
                    : "text-muted-foreground hover:bg-card hover:text-foreground"
                }`}
              >
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d={tab.icon} />
                </svg>
                {tab.label}
              </button>
            ))}
          </div>

          {/* Content */}
          <div className="flex-1 bg-card border border-border rounded-2xl p-6">
            {activeTab === "general" && (
              <div className="space-y-6">
                <h2 className="text-lg font-semibold text-card-foreground">General Settings</h2>
                
                <div className="space-y-4">
                  <div className="flex items-center justify-between py-4 border-b border-border">
                    <div>
                      <p className="font-medium text-card-foreground">Auto-save conversations</p>
                      <p className="text-sm text-muted-foreground">Save chat history automatically</p>
                    </div>
                    <div className="w-11 h-6 bg-primary rounded-full relative cursor-pointer">
                      <div className="w-5 h-5 bg-white rounded-full absolute right-0.5 top-0.5" />
                    </div>
                  </div>
                  
                  <div className="flex items-center justify-between py-4 border-b border-border">
                    <div>
                      <p className="font-medium text-card-foreground">Show source citations</p>
                      <p className="text-sm text-muted-foreground">Display document references in responses</p>
                    </div>
                    <div className="w-11 h-6 bg-primary rounded-full relative cursor-pointer">
                      <div className="w-5 h-5 bg-white rounded-full absolute right-0.5 top-0.5" />
                    </div>
                  </div>
                </div>
              </div>
            )}

            {activeTab === "models" && (
              <div className="space-y-6">
                <h2 className="text-lg font-semibold text-card-foreground">Model Configuration</h2>
                <p className="text-muted-foreground">Configure LLM and embedding models</p>
              </div>
            )}

            {activeTab === "database" && (
              <div className="space-y-6">
                <h2 className="text-lg font-semibold text-card-foreground">Database Settings</h2>
                <p className="text-muted-foreground">Vector database and storage configuration</p>
              </div>
            )}

            {activeTab === "api" && (
              <div className="space-y-6">
                <h2 className="text-lg font-semibold text-card-foreground">API Keys</h2>
                <p className="text-muted-foreground">Manage your API keys and tokens</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
