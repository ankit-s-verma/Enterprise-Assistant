from sqlalchemy import String, ForeignKey, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database.database import Base
from backend.utils.common import UserRole

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(150),unique=True, nullable=False, index=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole),default=UserRole.EMPLOYEE, nullable=False)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employees.employee_id"), nullable=False, index=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    conversations = relationship("Conversation", back_populates="user", cascade="all, delete-orphan")