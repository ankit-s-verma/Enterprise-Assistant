from sqlalchemy.orm import Session
from app.memory.context_builder import build_context
from app.models.conversation import Conversation
from app.repositories.convo_repo import ConvoRepo
from app.utils.common import ConversationRole
from app.utils.entity_extractor import find_employee_reference, find_ticket_reference

DEFAULT_CONTEXT_WINDOW = 10

class MemoryService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = ConvoRepo(db)

    def get_or_create_convo(self, user_id: int, conversation_id : int | None = None) -> Conversation:
        if conversation_id:
            conversation = self.repository.get_user_convo(user_id=user_id, conversation_id=conversation_id)
            if conversation:
                return conversation
            
        return self.repository.create_convo(user_id=user_id)
    
    def add_user_message(self, conversation_id: int, message: int):
        message = self.repository.add_message(conversation_id=conversation_id, role=ConversationRole.USER.value, message=message)
        self.repository.commit()
        return message
    
    def add_assistant_message(self, conversation_id: int,message: str):
        message = self.repository.add_message(conversation_id=conversation_id, role=ConversationRole.ASSISTANT.value, message=message)
        self.repository.commit()
        return message
    
    def get_recent_context(self, conversation_id: int, limit: int = DEFAULT_CONTEXT_WINDOW) -> list[dict[str, str]]:
        message = self.repository.get_recent_msg(conversation_id=conversation_id, limit=limit)
        return build_context(message)
    
    def get_conversation(self, user_id: int, conversation_id: int) -> Conversation | None:
        return self.repository.get_user_convo(user_id=user_id, conversation_id=conversation_id)

    def get_last_employee_reference(self, conversation_id: int, limit: int = DEFAULT_CONTEXT_WINDOW) -> str | None:
        messages = self.repository.get_recent_msg(conversation_id=conversation_id, limit=limit)

        for message in reversed(messages):            
            if message.role != ConversationRole.ASSISTANT.value:
                continue

            emp_id = find_employee_reference(message.message)
            if emp_id:
                return emp_id
            
        return None
    
    def get_last_ticket_reference(self, conversation_id: int, limit: int = DEFAULT_CONTEXT_WINDOW) -> str | None:
        messages = self.repository.get_recent_msg(conversation_id=conversation_id, limit=limit)

        for message in reversed(messages):
            if message.role != ConversationRole.ASSISTANT.value:
                continue

            ticket = find_ticket_reference(message.message)
            if ticket:
                return ticket
            
        return None

