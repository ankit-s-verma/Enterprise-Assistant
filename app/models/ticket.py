from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.utils.ticket_utils import TicketStatus

from app.database.database import Base

class Ticket(Base):
    __tablename__ = 'tickets'
    ticket_id: Mapped[str] = mapped_column(String(20), primary_key=True, index=True)
    issue: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[TicketStatus] = mapped_column(
        Enum(TicketStatus, name='ticketstatus', create_type=False),
        default=TicketStatus.OPEN,
        nullable=False
        )