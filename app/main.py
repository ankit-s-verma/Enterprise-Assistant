from fastapi import FastAPI
from app.models.models import QuestionRequest
from app.agents.ai_agent import perform_actions, answer_general_questions
from app.services.employee_data import get_employee_by_id, get_employee_by_name
from app.services.ticket_service import create_ticket, get_all_ticket, get_ticket_info

app = FastAPI(
    title='Fluid Assistant',
    version="1.0"
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
def ask(request: QuestionRequest):

    question = request.question

    action_data = perform_actions(question)
    intent = action_data.get('action')

    if intent == 'EMPLOYEE_LOOKUP':
        employee = None
        emp_id = action_data.get('employee_id')
        emp_name = action_data.get('employee_name')
        

        if emp_id:
            employee = get_employee_by_id(emp_id)

        elif emp_name:
            employee = get_employee_by_name(emp_name)

        elif ticket_id:
            ticket_info = get_ticket_info(ticket_id)

        if employee:

            return {
                "success" : True,
                "task" : "employee_lookup",
                "data" : employee
            }
                
        return {
            "success" : False,
            "message" : "Employee not found"
        }
    
    elif intent == "CREATE_TICKET":
        issue = action_data.get('issue')

        if not issue:
            return {
                "success" : False,
                "message" : "Issue description missing"
            }
        ticket = create_ticket(issue)

        return {
            "success" : True,
            "task" : "create_ticket",
            "data" : ticket
        }
    
    elif intent == "TICKET_SEARCH":
        ticket_id = action_data.get('ticket')
        
        if not ticket_id:
            return{
                "success" : False,
                "message" : "Ticket information missing"
            }
        ticket_info = get_ticket_info(ticket_id)

        return {
                "success" : True,
                "task" : "ticket_search",
                "data" : ticket_info
            } 

    
    else:
        answer = answer_general_questions(
            question
        )

        return {
            "success" : True,
            "task" : "general_query",
            "answer" : answer
        }
    

@app.get("/tickets")
def tickets():
    """
    Get method to return all the existing tickets from the database.
    """
    return get_all_ticket()


