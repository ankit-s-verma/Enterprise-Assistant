from sqlalchemy.orm import Session
from backend.models.ticket import Ticket
from backend.repositories.ticket_repo import TicketRepository
from backend.utils.ticket_utils import TicketStatus

def create_ticket(db:Session, ticket_id:str, issue:str, status:TicketStatus.OPEN) -> dict:
    repository = TicketRepository(db)
    ticket = Ticket(ticket_id=ticket_id, issue=issue, status=status)

    ticket = repository.create_ticket(ticket)

    return {
        "ticket_id" : ticket.ticket_id,
        "issue" : ticket.issue,
        "status" : ticket.status.value
    }

def get_ticket_by_id(db:Session, t_id:str) -> dict | str:
    repo = TicketRepository(db)
    
    ticket = repo.get_ticket_by_id(t_id)

    if ticket is None:
        return f'Ticket {t_id} not found'
    
    return {
        "ticket_id" : ticket.ticket_id,
        "issue" : ticket.issue,
        "status" : ticket.status.value
    }

def get_all_ticket(db:Session) -> list[dict]:
    repo = TicketRepository(db)
    tickets = repo.get_all_tickets()

    return [{
        "ticket_id" : ticket.ticket_id,
        "issue" : ticket.issue,
        "status" : ticket.status.value
        }
        for ticket in tickets
    ]

def update_ticket_status(db: Session, ticket_id : str, status: TicketStatus) -> dict | None:
    repo = TicketRepository(db)
    ticket = repo.update_ticket_status(ticket_id=ticket_id, status=status)

    if ticket is None:
        return None
    
    return {
        "ticket_id": ticket.ticket_id,
        "issue": ticket.issue,
        "status": ticket.status.value
    }