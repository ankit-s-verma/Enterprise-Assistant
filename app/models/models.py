from pydantic import BaseModel

class QuestionRequest(BaseModel):
    conversation_id: int | None = None
    question: str