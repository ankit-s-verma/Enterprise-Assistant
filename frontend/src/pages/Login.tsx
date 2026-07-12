import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Lock, Mail, Building2 } from "lucide-react";
import api from "../services/api";
import { useEffect } from "react";
import { isAuthenticated } from "../utils/auth";

export default function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
      if (isAuthenticated()) {
          navigate("/chat", { replace: true });
      }
  }, [navigate]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault(); 
    const formData = new URLSearchParams()

    formData.append('username', username);
    formData.append('password', password);

    try {const response = await api.post(
      "/auth/login",
      formData.toString(),
      {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      }
    );
    localStorage.setItem('token', response.data.access_token);
    navigate("/chat");
    } catch(error) {
    console.error("Login failed:", error);
    alert("Invalid username or password");
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4" style={{ backgroundColor: "#0F172A" }}>
      <div
        className="w-full max-w-md rounded-2xl p-8 shadow-lg"
        style={{ backgroundColor: "#1E293B" }}
      >
        <div className="flex flex-col items-center mb-8">
          <div
            className="w-14 h-14 rounded-xl flex items-center justify-center mb-4"
            style={{ backgroundColor: "#3B82F6" }}
          >
            <Building2 className="w-7 h-7 text-white" />
          </div>
          <h1 className="text-2xl font-semibold text-white">Enterprise Assistant</h1>
          <p className="text-sm mt-1" style={{ color: "#CBD5E1" }}>
            Sign in to continue
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm mb-2" style={{ color: "#CBD5E1" }}>
              Username
            </label>
            <div className="relative">
              <Mail
                className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4"
                style={{ color: "#CBD5E1" }}
              />
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter your username"
                className="w-full pl-10 pr-3 py-2.5 rounded-lg text-white placeholder:text-slate-400 outline-none focus:ring-2"
                style={{ backgroundColor: "#334155" }}
              />
            </div>
          </div>

          <div>
            <label className="block text-sm mb-2" style={{ color: "#CBD5E1" }}>
              Password
            </label>
            <div className="relative">
              <Lock
                className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4"
                style={{ color: "#CBD5E1" }}
              />
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                className="w-full pl-10 pr-3 py-2.5 rounded-lg text-white placeholder:text-slate-400 outline-none focus:ring-2"
                style={{ backgroundColor: "#334155" }}
              />
            </div>
          </div>

          <button
            type="submit"
            className="w-full py-2.5 rounded-lg font-medium text-white transition-colors hover:opacity-90"
            style={{ backgroundColor: "#3B82F6" }}
          >
            Sign in
          </button>
        </form>

        <p className="text-xs text-center mt-6" style={{ color: "#CBD5E1" }}>
          Secure enterprise access &middot; Internal use only
        </p>
      </div>
    </div>
  );
}
