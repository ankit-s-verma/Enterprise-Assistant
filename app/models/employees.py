from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

class Employee(Base):
   
    __tablename__ = 'employees'
    employee_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    employee_name: Mapped[str] = mapped_column(String(100), nullable=False)
    designation: Mapped[str] = mapped_column(String(100), nullable=False)
    department: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True,
    )
    phone_no: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    def to_dict(self) -> dict:
        return {
            "employee_id" : self.employee_id,
            "employee_name" : self.employee_name,
            "designation" : self.designation,
            "department" : self.department,
            "email" : self.email,
            "phone_no" : self.phone_no
        }
