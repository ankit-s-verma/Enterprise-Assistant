from sqlalchemy.orm import Session
from app.models.employees import Employee

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_emp_by_id(self, emp_id:int) -> Employee | None:
        return (
            self.db.query(Employee).filter(Employee.employee_id == emp_id).first()
        )
    
    def get_emp_by_name(self, emp_name:str) -> Employee | None:
        return (
            self.db.query(Employee).filter(Employee.employee_name == emp_name).first()
        )