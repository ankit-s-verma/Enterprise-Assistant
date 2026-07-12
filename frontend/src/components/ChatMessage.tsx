import { Bot, User } from "lucide-react";
import type { Message } from "../types";
import EmployeeCard from "./EmployeeCard";
import TicketCard from "./TicketCard";

export default function ChatMessage({ message }: { message: Message }) {
  const isUser = message.role === "user";
  return (
    <div className="flex gap-3 py-4">
      <div
        className="w-8 h-8 rounded-lg flex items-center justify-center shrink-0"
        style={{ backgroundColor: isUser ? "#334155" : "#3B82F6" }}
      >
        {isUser ? (
          <User className="w-4 h-4 text-white" />
        ) : (
          <Bot className="w-4 h-4 text-white" />
        )}
      </div>
      <div className="flex-1 min-w-0">
        <div className="text-xs mb-1" style={{ color: "#CBD5E1" }}>
          {isUser ? "You" : "HR Assistant"}
        </div>
        <div className="text-white leading-relaxed whitespace-pre-wrap">
          {message.content}
        </div>
        {message.employee && (
          <div className="mt-3">
            <EmployeeCard employee={message.employee} />
          </div>
        )}
        {message.ticket && (
          <div className="mt-3">
            <TicketCard ticket={message.ticket} />
          </div>
        )}
      </div>
    </div>
  );
}
