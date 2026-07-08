from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.utils.ticket_utils import TicketStatus

class TicketRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_ticket(self, ticket:Ticket) -> Ticket:
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
        pass

    def get_ticket_by_id(self, t_id:str) -> Ticket | None:
        return (
            self.db.query(Ticket).filter(Ticket.ticket_id == t_id).first()
        )

    def get_all_tickets(self) -> list[Ticket]:
        return (
            self.db.query(Ticket).all()
        )

    def update_ticket_status(self, ticket_id: str, status: TicketStatus) -> Ticket | None:
        ticket = self.get_ticket_by_id(t_id=ticket_id)

        if ticket is None:
            return None
        
        ticket.status = status
        self.db.commit()
        self.db.refresh(ticket)

        return ticket
