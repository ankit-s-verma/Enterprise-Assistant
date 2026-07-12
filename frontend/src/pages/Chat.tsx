import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import Sidebar from "../components/Sidebar";
import ChatMessage from "../components/ChatMessage";
import MessageComposer from "../components/MessageComposer";
import ThinkingIndicator from "../components/ThinkingIndicator";
import type {Employee, Message, Ticket } from "../types";
import api from "../services/api";
import { buildEmployee, buildEmployeeResponse } from "@/utils/employee";
import { buildTicket, buildTicketResponse } from "@/utils/ticket";


const welcome: Message = {
  id: "m0",
  role: "assistant",
  content:
    "Hi! I'm your Enterprise Assistant. Ask me about employees, policies, or open tickets.",
  timestamp: new Date().toISOString(),
};

export default function Chat() {
  const navigate = useNavigate();
  const [messages, setMessages] = useState<Message[]>([welcome]);
  const [thinking, setThinking] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const [selectedEmployee, setSelectedEmployee] = useState<Employee | null>(null);
  const [selectedTicket, setSelectedTicket] = useState<Ticket | null>(null);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [messages, thinking]);

  function handleNew() {
    setMessages([welcome]);
    setConversationId(null);
    setSelectedEmployee(null);
    setSelectedTicket(null);
  }

  function handleLogout() {
    localStorage.removeItem("token");
    navigate("/login");
  }

  async function handleSend(text: string) {
  const userMsg: Message = {
    id: "u" + Date.now(),
    role: "user",
    content: text,
    timestamp: new Date().toISOString(),
  };

  setMessages((prev) => [...prev, userMsg]);
  setThinking(true);

  try {
    const response = await api.post("/ask", {
      question: text,
      conversation_id: conversationId,
    });

    const data = response.data;

    if (!data.success) {
      setMessages((prev) => [
        ...prev,
        {
          id: "e" + Date.now(),
          role: "assistant",
          content: data.message || "No results found.",
          timestamp: new Date().toISOString(),
        },
      ]);

      return;
    }

    if (data.conversation_id) {
      setConversationId(data.conversation_id);
    }

    let reply: Message;

    if (data.task === "general_query") {
      reply = {
        id: "a" + Date.now(),
        role: "assistant",
        content: data.answer,
        timestamp: new Date().toISOString(),
      };
    }
    else if (data.task === "employee_lookup") {
      if (data.data.employee_id) {

        const employee = buildEmployee(data.data);

        setSelectedEmployee(employee);

        reply = {
          id: "a" + Date.now(),
          role: "assistant",
          content: "Employee found.",
          timestamp: new Date().toISOString(),
          employee,
        };
      }
      else {
        reply = {
          id: "a" + Date.now(),
          role: "assistant",
          content: buildEmployeeResponse(data.data, selectedEmployee),
          timestamp: new Date().toISOString(),
        };
      }
    }
    else if (data.task === "create_ticket") {
      const ticket = buildTicket(data.data);

      setSelectedTicket(ticket);

      reply = {
        id: "a" + Date.now(),
        role: "assistant",
        content: "Ticket created successfully.",
        timestamp: new Date().toISOString(),
        ticket,
      };
    }
    else if (data.task === "ticket_search") {
      if (data.data.ticket_id) {
        const ticket = buildTicket(data.data);

        setSelectedTicket(ticket);

        reply = {
          id: "a" + Date.now(),
          role: "assistant",
          content: "Ticket found.",
          timestamp: new Date().toISOString(),
          ticket,
        };
      } else {
        reply = {
          id: "a" + Date.now(),
          role: "assistant",
          content: buildTicketResponse(data.data, selectedTicket),
          timestamp: new Date().toISOString(),
        };
      }
    }
    else if (data.task === "update_ticket") {
      const ticket = buildTicket(data.data);

      setSelectedTicket(ticket);

      reply = {
        id: "a" + Date.now(),
        role: "assistant",
        content: `The status of ticket ${ticket.id} has been updated to ${ticket.status}.`,
        timestamp: new Date().toISOString(),
        ticket,
      };
    }
    else {
      reply = {
        id: "a" + Date.now(),
        role: "assistant",
        content: "This response type will be implemented in the next step.",
        timestamp: new Date().toISOString(),
      };
    }

    setMessages((prev) => [...prev, reply]);
    } catch (error: any) {
      console.error(error);
      let errorMessage = "Something went wrong.";

      if (error.response) {
        switch (error.response.status) {
          case 400:
            errorMessage =
              error.response.data?.detail || "Invalid request.";
            break;

          case 401:
            errorMessage = "Your session has expired. Please login again.";
            break;

          case 403:
            errorMessage = "You are not authorized to perform this action.";
            break;

          case 404:
            errorMessage = "Requested resource was not found.";
            break;

          case 500:
            errorMessage = "Internal server error.";
            break;

          default:
            errorMessage =
              error.response.data?.detail ||
              "Unexpected server error.";
        }
      } else if (error.request) {
        errorMessage =
          "Unable to reach the backend. Please check if the server is running.";
      }

      setMessages((prev) => [
        ...prev,
        {
          id: "e" + Date.now(),
          role: "assistant",
          content: errorMessage,
          timestamp: new Date().toISOString(),
        },
      ]);
    } finally {
      setThinking(false);
    }
  }


  return (
    <div className="flex h-screen" style={{ backgroundColor: "#0F172A" }}>
      <Sidebar
        onNew={handleNew}
        onLogout={handleLogout}
      />

      <main className="flex-1 flex flex-col h-screen">
        <header className="px-6 py-4 border-b border-slate-800 flex items-center justify-between">
          <div>
            <h1 className="text-white font-semibold">Enterprise Assistant</h1>
            <p className="text-xs" style={{ color: "#CBD5E1" }}>
              Ask about people, policies, and tickets
            </p>
          </div>
        </header>

        <div ref={scrollRef} className="flex-1 overflow-y-auto">
          <div className="max-w-3xl mx-auto w-full px-6 divide-y divide-slate-800">
            {messages.map((m) => (
              <ChatMessage key={m.id} message={m} />
            ))}
            {thinking && <ThinkingIndicator />}
          </div>
        </div>

        <div className="px-6 pb-6 pt-3">
          <div className="max-w-3xl mx-auto w-full">
            <MessageComposer onSend={handleSend} disabled={thinking} />
            <p className="text-xs text-center mt-2" style={{ color: "#CBD5E1" }}>
              Responses may reference internal company data. Verify sensitive actions.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
}
