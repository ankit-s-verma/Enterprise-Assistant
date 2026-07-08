from sqlalchemy.orm import Session
from app.llm.ai_agent import perform_actions, answer_general_questions
from app.memory.memory_service import MemoryService
from app.models.models import QuestionRequest
from app.models.user import User
from app.services.employee_service import get_employee_by_id
from app.services.ticket_service import create_ticket, get_ticket_by_id, update_ticket_status
from app.utils.common import generate_identifier
from app.utils.ticket_utils import TicketStatus, parse_ticket_status
from app.utils.entity_extractor import find_employee_reference, find_ticket_reference


class AssistantService:

    def __init__(self, db: Session):
        self.db = db
        self.memory = MemoryService(db)


    def process(self, request: QuestionRequest, current_user: User):
        conversation = self.memory.get_or_create_convo(user_id=current_user.id, conversation_id=request.conversation_id)
        self.memory.add_user_message(conversation_id=conversation.id, message=request.question)
        context = self.memory.get_recent_context(conversation.id)

        action_data = perform_actions(question=request.question, conversation_history=context)
        intent = action_data.get("action")

        print(f"Action for the ask is : {intent}")

        if intent == "EMPLOYEE_LOOKUP":
            return self._handle_employee_lookup(request, action_data, conversation.id)

        elif intent == "CREATE_TICKET":
            return self._handle_create_ticket(action_data, conversation.id)

        elif intent == "TICKET_SEARCH":
            return self._handle_ticket_search(request, action_data, conversation.id)
        
        elif intent == "UPDATE_TICKET":
            return self._handle_ticket_update(request, action_data, conversation.id)

        return self._handle_general_query(request, context, conversation.id)

    def _filter_employee_response(self, employee: dict, field: str) -> dict:

        if field == "name":
            return {
                "name": employee["employee_name"]
            }

        elif field == "email":
            return {
                "email": employee["email"]
            }

        elif field == "department":
            return {
                "department": employee["department"]
            }

        elif field == "designation":
            return {
                "designation": employee["designation"]
            }

        elif field == "phone":
            return {
                "phone": employee["phone_no"]
            }

        return employee

    def _handle_employee_lookup(self, request: QuestionRequest, action_data: dict, conversation_id: int):
        employee_id = self._resolve_employee(request.question, conversation_id)

        if employee_id is None:
            return {
                "success": False,
                "message": "I couldn't determine which employee you're referring to."
            }

        employee = get_employee_by_id(self.db, employee_id)
        if employee is None:
            return {
                "success": False,
                "message": "Employee not found."
            }
        
        field = action_data.get("field", "all")
        response = self._filter_employee_response(employee, field)
        
        self._store_assistant_response(conversation_id, str(employee))

        return {
            "success": True,
            "conversation_id": conversation_id,
            "task": "employee_lookup",
            "data": response
        }


    def _handle_create_ticket(self, action_data: dict, conversation_id: int):
        issue = action_data.get("issue")
        if not issue:
            return {
                "success": False,
                "message": "Issue description missing."
            }

        ticket = create_ticket(db=self.db, ticket_id=generate_identifier("INC"), issue=issue, status=TicketStatus.OPEN)
        self._store_assistant_response(conversation_id, str(ticket))

        return {
            "success": True,
            "conversation_id": conversation_id,
            "task": "create_ticket",
            "data": ticket
        }


    def _handle_ticket_search(self, request: QuestionRequest, action_data: dict, conversation_id: int):
        ticket_id = self._resolve_ticket(request.question, conversation_id)

        if ticket_id is None:
            return {
                "success": False,
                "message": "I couldn't determine which ticket you're referring to."
            }

        ticket = get_ticket_by_id(self.db, ticket_id)
        if isinstance(ticket, str):
            return {
                "success": False,
                "message": ticket
            }
        
        field = action_data.get("field", "all")
        response = self._build_ticket_response(ticket, field)
        self._store_assistant_response(conversation_id, str(ticket))

        return {
            "success": True,
            "conversation_id": conversation_id,
            "task": "ticket_search",
            "data": response
        }
    
    def _handle_ticket_update(self, request: QuestionRequest, action_data: dict, conversation_id: int):
        ticket_id = self._resolve_ticket(request.question, conversation_id)

        if ticket_id is None:
            return {
                "success" : False,
                "message" : "I couldn't determin which ticket you're referring to."
            }
        
        status = action_data.get('status')
        if status is None:
            return {
                "success" : False,
                "message" : "Ticket status missing."
            }
        
        try:
            ticket_status = parse_ticket_status(action_data.get("status"))
        except ValueError:
            return {
                "success" : False,
                "message" : f"Unsupported ticket status!"
            }
        
        ticket = update_ticket_status(self.db, ticket_id, ticket_status)

        if ticket is None:
            return {
                "success" : False,
                "message" : "Ticket not found."
            }
        
        self._store_assistant_response(conversation_id, str(ticket))

        return {
            "success": True,
            "conversation_id": conversation_id,
            "task": "update_ticket",
            "data": ticket
        }

    
    def _build_ticket_response(self, ticket: dict, field: str) -> dict:

        if field == "ticket_id":
            return {
                "ticket_id": ticket["ticket_id"]
            }

        elif field == "status":
            return {
                "status": ticket["status"]
            }

        elif field == "issue":
            return {
                "issue": ticket["issue"]
            }

        return ticket


    def _handle_general_query(self, request: QuestionRequest, context: list, conversation_id: int):
        answer = answer_general_questions(question=request.question, conversation_history=context)
        self._store_assistant_response(conversation_id, str(answer))

        return {
            "success": True,
            "conversation_id": conversation_id,
            "task": "general_query",
            "answer": answer
        }


    def _resolve_employee(self, question: str, conversation_id: int) -> str | None:
        employee_id = find_employee_reference(question)

        if employee_id:
            return employee_id

        return self.memory.get_last_employee_reference(conversation_id)
    
    
    def _resolve_ticket(self, question: str, conversation_id: int) -> str | None:
        ticket_id = find_ticket_reference(question)


        if ticket_id:
            return ticket_id

        ticket = self.memory.get_last_ticket_reference(conversation_id)
        return ticket   


    def _store_assistant_response( self, conversation_id: int, message: str):
        self.memory.add_assistant_message(conversation_id=conversation_id, message=message)