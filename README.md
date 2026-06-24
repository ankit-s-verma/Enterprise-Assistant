# AI-Powered Enterprise HR Assistant

## Overview

The AI-Powered Enterprise HR Assistant is a FastAPI-based application that combines Large Language Models (LLMs) with enterprise business actions. The assistant can understand natural language queries, identify user intent, and perform business operations such as employee information retrieval and support ticket creation.

The project demonstrates how AI agents can be integrated with enterprise systems to automate common HR and IT support workflows.

---

## Features

### Employee Information Lookup

Retrieve employee information from a SQLite database using natural language queries.

Examples:

* Show details of employee E105
* Get information about Sarah Johnson
* Find employee E110

### Support Ticket Creation

Create IT support tickets through conversational requests.

Examples:

* Create a ticket for VPN connectivity issues
* My system is broken
* Unable to login to the company portal

### General Business Queries

Answer general HR and enterprise-related questions using an LLM.

Examples:

* What is the onboarding process?
* What is employee onboarding?
* Explain the leave approval workflow

### AI-Powered Intent Routing

The assistant uses an LLM to classify user intent and route requests to the appropriate business tool instead of relying on keyword matching.

---

## Architecture

```text
                    User
                      │
                      ▼
                 POST /ask
                      │
                      ▼
                AI Intent Layer
                      │
         ┌────────────┼────────────┐
         │            │            │
         ▼            ▼            ▼

 EMPLOYEE_LOOKUP  CREATE_TICKET  GENERAL_QUERY
         │            │            │
         ▼            ▼            ▼

 SQLite Query   SQLite Insert   LLM Response
         │            │            │
         └────────────┼────────────┘
                      │
                      ▼
                   Response
```

---

## Technology Stack

### Backend

* FastAPI
* Python 3.11

### Database

* SQLite

### AI Layer

* Google Gemini API
* Structured Intent Extraction

### Validation

* Pydantic

---

## Project Structure

```text
enterprise-hr-assistant/

├── app.py
├── ai_agent.py
├── database.py
├── employee_service.py
├── ticket_service.py
├── models.py
├── company.db
├── employees.csv
├── requirements.txt
├── Systems Architecture.png
└── README.md
```

---

## API Endpoint

### POST /ask

Request:

```json
{
    "question": "Show details of employee E105"
}
```

Employee Lookup Response:

```json
{
    "success": true,
    "action": "employee_lookup",
    "data": {
        "employee_id": "E105",
        "employee_name": "Michael Wilson",
        "designation": "Software Engineer",
        "department": "Engineering",
        "email_id": "michael.wilson@company.com",
        "phone_no": "+91-9876543205"
    }
}
```

Ticket Creation Response:

```json
{
    "success": true,
    "action": "ticket_created",
    "data": {
        "ticket_id": "INC-12345",
        "status": "OPEN"
    }
}
```

---

## Engineering Improvement Implemented

### API Tool Calling with Intent Routing

Instead of generating only text responses, the assistant uses an LLM to extract structured intent from user queries.

Example:

Input:

```text
Create a ticket for VPN connectivity issue
```

Extracted Intent:

```json
{
    "action": "CREATE_TICKET",
    "issue": "VPN connectivity issue"
}
```

The extracted intent is then routed to the appropriate business tool.

Benefits:

* Dynamic business action execution
* Improved extensibility
* Reduced reliance on hardcoded keyword matching
* Better enterprise workflow automation

---

## Error Handling and Validation

The application includes:

* Request validation using Pydantic
* Structured JSON parsing
* Exception handling for AI service failures
* Fallback responses for unavailable models
* Database operation validation

---

## Test Cases

### Normal Business Query

Request:

```json
{
    "question": "Show details of employee E105"
}
```

Expected Result:

Employee information is retrieved from SQLite and returned to the user.

---

### Challenging Query

Request:

```json
{
    "question": "My system is broken"
}
```

Expected Result:

The assistant identifies the issue as a support request and creates a support ticket.

---

## Future Improvements

* PostgreSQL integration
* User authentication and authorization
* Conversation memory
* Document Retrieval (RAG)
* Multi-step agent workflows
* Ticket status tracking
* Employee search by department and location

---

## Tradeoff Discussion

For this implementation, SQLite was chosen over PostgreSQL to reduce setup complexity and accelerate development.

This decision enabled rapid prototyping while still demonstrating database integration, persistence, and business workflows. In a production environment, PostgreSQL and SQLAlchemy would be preferred for scalability, concurrency support, and maintainability.

---

## Author

Ankit Verma

MSc Applied Artificial Intelligence

FastAPI | Machine Learning | AI Engineering | Python Development
