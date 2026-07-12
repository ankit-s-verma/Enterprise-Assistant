import pandas as pd
from sqlalchemy.orm import Session
from backend.database.database import SessionLocal
from backend.models.employees import Employee
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / 'employees.csv'

def data_insertion() -> None:
    if not CSV_FILE.exists():
        return f"Error: employess.csv not found at {CSV_FILE}"
    
    emp_df = pd.read_csv(CSV_FILE)

    db: Session = SessionLocal()
    try:

        existing_ids = {emp.employee_id for emp in db.query(Employee.employee_id).all()}

        for row in emp_df.itertuples(index=False):

            if row.employee_id in existing_ids:
                continue

            emp = Employee(
                employee_id = row.employee_id,
                employee_name = row.employee_name,
                designation = row.designation,
                department = row.department,
                email = row.email,
                phone_no = row.phone_no
            )

            db.add(emp)

        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error while pushing the employee data: {e}")

    finally:
        db.close()

