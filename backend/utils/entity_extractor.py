import re

EMPLOYEE_REF_PATTERN = r"\b\d{6}\b"
TICKET_REF_PATTERN = r"\bINC-[A-Z0-9]+\b"

def find_employee_reference(text: str) -> str | None:
    match = re.search(EMPLOYEE_REF_PATTERN, text)

    if match:
        return match.group()
    
    return None

def find_ticket_reference(text: str) -> str | None:
    match = re.search(TICKET_REF_PATTERN, text)

    if match:
        return match.group()
    
    return None