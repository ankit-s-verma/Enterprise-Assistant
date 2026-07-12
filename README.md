# Enterprise HR Assistant

<p align="center">
  <img src="screenshots/general-questions.png" alt="Enterprise Assistant" width="900">
</p>

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![LangGraph](https://img.shields.io/badge/LangGraph-AI_Workflow-black?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)

</p>

An AI-powered **Enterprise HR Assistant** that enables employees to search employee information, create and manage IT support tickets, and ask organization-specific questions through natural language conversations. The application combines **LangGraph**, **Retrieval-Augmented Generation (RAG)**, **Groq LLM**, **FastAPI**, **React**, and **PostgreSQL** to deliver a modern enterprise AI experience.

---

# Features

### Authentication

- JWT Authentication
- Protected Routes
- Auto Login
- Logout
- Axios Request & Response Interceptors

### AI Assistant

- General HR conversations
- Company policy Q&A using RAG
- Context-aware follow-up questions
- Conversation memory

### Employee Management

- Employee Search
- Employee Profile Cards
- Context-aware employee follow-ups

### Ticket Management

- Ticket Search
- Ticket Creation
- Ticket Updates
- Ticket Cards
- Ticket conversational memory

### Frontend

- Modern React UI
- Dark enterprise theme
- Responsive layout
- Thinking indicator
- New conversation support

### Deployment

- Dockerized frontend
- Dockerized backend
- PostgreSQL
- Docker Compose

---

# System Architecture

<p align="center">
<img src="screenshots/system-architecture.png" width="900">
</p>

---

# Technology Stack

| Category | Technologies |
|------------|--------------|
| Frontend | React 18, TypeScript, Tailwind CSS, Vite |
| Backend | FastAPI, Python |
| AI | LangGraph, LangChain, Groq |
| Database | PostgreSQL, SQLAlchemy |
| Vector Store | ChromaDB |
| Authentication | JWT |
| Containerization | Docker, Docker Compose |
| Web Server | Nginx |

---

# Project Structure

```text
Enterprise-HR-Assistant/
│
├── alembic/
│
├── backend/
│   ├── auth/
│   ├── chroma_db/
│   ├── core/
│   ├── database/
│   ├── knowledge_base/
│   ├── llm/
│   ├── memory/
│   ├── models/
│   ├── rag/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── types/
│   │   ├── utils/
│   │   └── App.tsx
│   │
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   └── vite.config.ts
│
├── screenshots/
│
├── docker-compose.yml
├── API_Documentation.md
├── README.md
├── LICENSE
└── .env.example
```

---

# Screenshots

## Login

![Login](screenshots/login-ui.png)

---

## Chat Interface

![Chat](screenshots/chat-interface.png)

---

## Employee Search

![Employee](screenshots/employee-search.png)

---

## Ticket Search

![Ticket](screenshots/ticket-search.png)

---

## Ticket Creation & Update

![Ticket Creation & Update](screenshots/ticket-processing.png)

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/ankit-s-verma/Enterprise-HR-Assistant.git

cd Enterprise-HR-Assistant
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=

SECRET_KEY=

GROQ_API_KEY=

MODEL_NAME=

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Run with Docker

The easiest way to run the application.

```bash
docker compose up --build
```

Application URLs:

| Service | URL |
|----------|-----|
| Frontend | http://localhost |
| Backend | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |

---

## Local Development

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# API Documentation

Interactive Swagger documentation is available at:

```
http://localhost:8000/docs
```

Detailed endpoint documentation can be found in:

```
API_Documentation.md
```

---

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

# Author

## Ankit Verma

**AI & Machine Learning Engineer | Python Developer**

GitHub:
https://github.com/ankit-s-verma

LinkedIn:
https://www.linkedin.com/in/ankit-s-verma/