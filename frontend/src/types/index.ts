export type Role = "user" | "assistant";

export interface Message {
  id: string;
  role: Role;
  content: string;
  timestamp: string;
  employee?: Employee;
  ticket?: Ticket;
}

export interface Conversation {
  id: string;
  title: string;
  updatedAt: string;
}

export interface Employee {
  id: string;
  name: string;
  designation: string;
  department: string;
  email: string;
  phone: string;
}

export interface Ticket {
  id: string;
  issue: string;
  status: "Open" | "In Progress" | "Resolved" | "Closed";
}
