from enum import Enum

class TicketStatus(str, Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"


STATUS_MAP = {
    "open": TicketStatus.OPEN,
    "opened": TicketStatus.OPEN,

    "close": TicketStatus.CLOSED,
    "closed": TicketStatus.CLOSED,

    "resolve": TicketStatus.RESOLVED,
    "resolved": TicketStatus.RESOLVED,

    "in progress": TicketStatus.IN_PROGRESS,
    "in_progress": TicketStatus.IN_PROGRESS,
    "progress": TicketStatus.IN_PROGRESS,
}


def parse_ticket_status(status: str | None) -> TicketStatus | None:
    """
    Convert a user/LLM supplied ticket status into a TicketStatus enum.
    """

    if not status:
        return None

    return STATUS_MAP.get(status.strip().lower())