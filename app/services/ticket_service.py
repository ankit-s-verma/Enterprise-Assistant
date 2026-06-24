import uuid
from datetime import datetime
from app.database.database import get_connection

def create_ticket(issue) -> dict:
    """
    Creates a new ticket in the ticket database.
    """
    conn = get_connection()
    ticket_id = f"INC-{str(uuid.uuid4())[:8]}"

    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO ticket VALUES (?,?,?)""",
            (
                ticket_id,
                issue,
                datetime.now().isoformat()
            ))
    conn.commit()
    conn.close()

    return {
        "ticket_id" : ticket_id,
        "issue" : issue
    }

def get_all_ticket() -> dict:
    """
    Returns all the tickets from the ticket database in a JSON format. eg - {'ticket_id' : '1234'}
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""select * from ticket""")

    rows = cursor.fetchall()

    return [dict(row) for row in rows]

def get_ticket_info(ticket_id) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""select * from ticket where ticket_id = ?""", (ticket_id,))

    ticket_info = cursor.fetchone()

    conn.close()

    return dict(ticket_info) if  ticket_info else None

if __name__ == "__main__":
    pass
    # print(get_all_ticket())
    # print(create_ticket('System broken'))