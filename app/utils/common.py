import uuid

# Generate a unique identifier with a custom prefix. eg - INC-4A82F6B1, CONV-9AB21D33
def generate_identifier(prefix:str, length: int = 8) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:length].upper()}"

#============================================================================================================================================================

from enum import Enum
class UserRole(str, Enum):
    ADMIN = 'admin'
    HR = 'hr'
    EMPLOYEE = 'employee'

#============================================================================================================================================================

class ConversationRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"