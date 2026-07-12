import { useState } from "react";
import { Send } from "lucide-react";

interface Props {
  onSend: (text: string) => void;
  disabled?: boolean;
}

export default function MessageComposer({ onSend, disabled }: Props) {
  const [text, setText] = useState("");

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const value = text.trim();
    if (!value || disabled) return;
    onSend(value);
    setText("");
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="rounded-xl p-2 flex items-end gap-2 shadow-sm"
      style={{ backgroundColor: "#334155" }}
    >
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        rows={1}
        placeholder="Ask about employees, policies, tickets…"
        className="flex-1 bg-transparent text-white placeholder:text-slate-400 outline-none resize-none px-2 py-2 max-h-40"
      />
      <button
        type="submit"
        disabled={disabled || !text.trim()}
        className="w-10 h-10 rounded-lg flex items-center justify-center text-white transition-opacity disabled:opacity-40"
        style={{ backgroundColor: "#3B82F6" }}
      >
        <Send className="w-4 h-4" />
      </button>
    </form>
  );
}
