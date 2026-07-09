from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models.models import QuestionRequest
from app.services.ticket_service import get_all_ticket
from app.database.initialize import initialize_db
from app.database.database import get_db
from app.core.exception_handler import register_exception_handlers
from app.auth.router import router as auth_router
from app.auth.dependencies import get_current_user
from app.models.user import User
from app.services.assistant_service import AssistantService

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