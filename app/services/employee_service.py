from sqlalchemy.orm import Session
from app.repositories.employee_repo import EmployeeRepository

def get_employee_by_id(db: Session, emp_id:int) -> dict | None:
    employee = EmployeeRepository(db).get_emp_by_id(emp_id)

    if not employee:
        return None

    return {
        "employee_id": employee.employee_id,
        "employee_name": employee.employee_name,
        "department": employee.department,
        "designation": employee.designation,
        "email": employee.email,
        "phone_no": employee.phone_no
    }

def get_employee_by_name(db: Session, emp_name:str) -> dict | None:
    employee = EmployeeRepository(db).get_emp_by_name(emp_name)

    if not employee:
        return None

    return {
        "employee_id": employee.employee_id,
        "employee_name": employee.employee_name,
        "department": employee.department,
        "designation": employee.designation,
        "email": employee.email,
        "phone_no": employee.phone_no
    }