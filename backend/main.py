from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.models.models import QuestionRequest
from backend.services.ticket_service import get_all_ticket
from backend.database.initialize import initialize_db
from backend.database.database import get_db
from backend.core.exception_handler import register_exception_handlers
from backend.auth.router import router as auth_router
from backend.auth.dependencies import get_current_user
from backend.models.user import User
from backend.services.assistant_service import AssistantService
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_db()
    yield

app = FastAPI(
    title='Enterprise Assistant',
    version="2.0",
    lifespan=lifespan
)
register_exception_handlers(app)

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite
        "https://id-preview-b2e09f50-191c-476c-b263-6b0372893f91.lovable.app",
        "http://localhost:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def server_checkup():
    """
    Server health checkup if the FastAPI is working.
    """
    return {
        "status" : "working"
    }

@app.post("/ask")
def ask(request: QuestionRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    assistant = AssistantService(db)
    return assistant.process(request=request, current_user=current_user)
    

@app.get("/tickets")
def tickets(db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    """
    Get method to return all the existing tickets from the database.
    """
    return get_all_ticket(db)