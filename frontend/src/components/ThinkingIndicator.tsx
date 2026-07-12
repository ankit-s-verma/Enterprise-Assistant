import { Bot } from "lucide-react";

export default function ThinkingIndicator() {
  return (
    <div className="flex gap-3 py-4">
      <div
        className="w-8 h-8 rounded-lg flex items-center justify-center shrink-0"
        style={{ backgroundColor: "#3B82F6" }}
      >
        <Bot className="w-4 h-4 text-white" />
      </div>
      <div className="flex-1">
        <div className="text-xs mb-1" style={{ color: "#CBD5E1" }}>
          HR Assistant
        </div>
        <div className="flex items-center gap-1.5 h-6">
          <span className="w-2 h-2 rounded-full animate-bounce" style={{ backgroundColor: "#CBD5E1", animationDelay: "0ms" }} />
          <span className="w-2 h-2 rounded-full animate-bounce" style={{ backgroundColor: "#CBD5E1", animationDelay: "150ms" }} />
          <span className="w-2 h-2 rounded-full animate-bounce" style={{ backgroundColor: "#CBD5E1", animationDelay: "300ms" }} />
        </div>
      </div>
    </div>
  );
}
