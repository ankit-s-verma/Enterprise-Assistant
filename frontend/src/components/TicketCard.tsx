import type { Ticket } from "../types";

const statusColor: Record<Ticket["status"], string> = {
  Open: "#3B82F6",
  "In Progress": "#F59E0B",
  Resolved: "#10B981",
  Closed: "#df5a1d",
};

export default function TicketCard({ ticket }: { ticket: Ticket }) {
  return (
    <div
      className="rounded-xl p-4 max-w-md shadow-sm"
      style={{ backgroundColor: "#1E293B" }}
    >
      <div className="flex items-start justify-between gap-3">
        <div className="min-w-0">
          <div className="text-xs" style={{ color: "#CBD5E1" }}>
            Ticket #{ticket.id}
          </div>
          <div className="text-white font-medium mt-0.5 truncate">
            {ticket.issue}
          </div>
        </div>
        <span
          className="text-xs font-medium px-2 py-1 rounded-md text-white shrink-0"
          style={{ backgroundColor: statusColor[ticket.status] }}
        >
          {ticket.status}
        </span>
      </div>
      <div
        className="mt-3 grid grid-cols-3 gap-2 text-xs"
        style={{ color: "#CBD5E1" }}
      >
      </div>
    </div>
  );
}
