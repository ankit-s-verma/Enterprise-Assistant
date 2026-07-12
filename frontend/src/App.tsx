import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Chat from "./pages/Chat";
import ProtectedRoute from "../src/components/ProtectedRoute";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/login" element={<Login />} />
      <Route path="/chat" element={ <ProtectedRoute> <Chat /> </ProtectedRoute>}
        />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  );
}
