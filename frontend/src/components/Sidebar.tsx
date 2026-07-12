import { Building2, Plus, LogOut } from "lucide-react";

interface Props {
  onNew: () => void;
  onLogout: () => void;
}

export default function Sidebar({
  onNew,
  onLogout,
}: Props) {
  return (
    <aside
      className="w-72 flex flex-col h-screen border-r border-slate-800"
      style={{ backgroundColor: "#111827" }}
    >
      {/* Brand */}
      <div className="px-4 py-4 flex items-center gap-3 border-b border-slate-800">
        <div
          className="w-9 h-9 rounded-lg flex items-center justify-center"
          style={{ backgroundColor: "#3B82F6" }}
        >
          <Building2 className="w-5 h-5 text-white" />
        </div>
        <div>
          <div className="text-sm font-semibold text-white leading-tight">
            Enterprise Assistant
          </div>
          <div className="text-xs" style={{ color: "#CBD5E1" }}>
            Assistant
          </div>
        </div>
      </div>

      {/* New conversation */}
      <div className="px-3 pt-3">
        <button
          onClick={onNew}
          className="w-full flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium text-white transition-colors hover:opacity-90"
          style={{ backgroundColor: "#3B82F6" }}
        >
          <Plus className="w-4 h-4" />
          New Conversation
        </button>
      </div>

      <div className="flex-1" />

      {/* Logout */}
      <div className="p-3 border-t border-slate-800">
        <button
          onClick={onLogout}
          className="w-full flex items-center gap-2 px-3 py-2 rounded-lg text-sm transition-colors hover:bg-slate-800"
          style={{ color: "#CBD5E1" }}
        >
          <LogOut className="w-4 h-4" />
          Logout
        </button>
      </div>
    </aside>
  );
}
