import { Mail, MapPin, Briefcase } from "lucide-react";
import type { Employee } from "../types";

export default function EmployeeCard({ employee }: { employee: Employee }) {
  const initials = employee.name
    .split(" ")
    .map((n) => n[0])
    .slice(0, 2)
    .join("");

  return (
    <div
      className="rounded-xl p-4 max-w-md shadow-sm"
      style={{ backgroundColor: "#1E293B" }}
    >
      <div className="flex items-center gap-3">
        <div
          className="w-11 h-11 rounded-full flex items-center justify-center font-semibold text-white"
          style={{ backgroundColor: "#3B82F6" }}
        >
          {initials}
        </div>
        <div className="min-w-0">
          <div className="text-white font-medium truncate">{employee.name}</div>
          <div className="text-sm truncate" style={{ color: "#CBD5E1" }}>
            {employee.designation}
          </div>
        </div>
      </div>
      <div className="mt-4 space-y-2 text-sm" style={{ color: "#CBD5E1" }}>
        <div className="flex items-center gap-2">
          <Briefcase className="w-4 h-4" />
          <span>{employee.department}</span>
        </div>
        <div className="flex items-center gap-2">
          <Mail className="w-4 h-4" />
          <span className="truncate">{employee.email}</span>
        </div>
        <div className="flex items-center gap-2">
          <MapPin className="w-4 h-4" />
          <span>{employee.phone}</span>
        </div>
      </div>
    </div>
  );
}
