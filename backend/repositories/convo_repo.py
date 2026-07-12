from sqlalchemy import desc
from sqlalchemy.orm import Session
from backend.models.conversation import Conversation
from backend.models.conversation_message import ConversationMessage

class ConvoRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_convo(self, user_id: int, title: str | None = None) -> Conversation:
        conversation = Conversation(user_id=user_id, title=title)
        self.db.add(conversation)
        self.db.flush()
        self.db.refresh(conversation)

        return conversation
    
    def get_convo(self, conversation_id: int) -> Conversation | None:
        return (
            self.db.query(Conversation).filter(Conversation.id == conversation_id).first()
        )
    
    def get_user_convo(self, user_id: int, conversation_id: int) -> Conversation | None:
        return (
            self.db.query(Conversation).filter(Conversation.id == conversation_id, Conversation.user_id == user_id).first()
        )

    def update_timestamp(self, conversation: Conversation) -> None:
        self.db.add(conversation)
        self.db.commit()
        
    def add_message(self, conversation_id: int, role: str, message: str) -> ConversationMessage:
        conversation_message = ConversationMessage(conversation_id=conversation_id, role=role, message=message)
        self.db.add(conversation_message)
        self.db.flush()
        self.db.refresh(conversation_message)

        return conversation_message
    
    def get_recent_msg(self, conversation_id: int, limit: int = 10) -> list[ConversationMessage]:
        messages = (self.db.query(ConversationMessage).filter(ConversationMessage.conversation_id == conversation_id).order_by(desc(ConversationMessage.created_at)).limit(limit).all())

        return list(reversed(messages))
    
    def get_all_msg(self, conversation_id: int) -> list[ConversationMessage]:
        return (
            self.db.query(ConversationMessage).filter(ConversationMessage.conversation_id == conversation_id).order_by(ConversationMessage.created_at).all()
        )
    
    def delete_convo(self, conversation: Conversation) -> None:
        self.db.delete(conversation)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()