from app.models.conversation_message import ConversationMessage

def build_context(messages: list[ConversationMessage]) -> list[dict[str,str]]:
    return [
        {
            "role" : message.role,
            "content" : message.message
        }
        for message in messages
    ]