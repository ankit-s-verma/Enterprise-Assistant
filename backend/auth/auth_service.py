from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict, EmailStr
from backend.utils.common import UserRole
from backend.auth.jwt_handler import create_access_token
from backend.auth.security import verify_pwd
from backend.repositories.user_repo import UserRepository
from backend.auth.exceptions import *
from backend.models.user import User
from backend.auth.security import hash_pwd, verify_pwd

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id : int
    username : str
    email : EmailStr
    role : UserRole
    employee_id : int
    is_active : bool

    model_config = ConfigDict(from_attributes=True)

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    employee_id: int
    role: UserRole = UserRole.EMPLOYEE

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: UserRole
    employee_id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class AuthService:
    @staticmethod
    def auth_user(db: Session, username: str, password: str) -> TokenResponse | None:
        user = UserRepository.get_by_username(db, username)
        if not user:
            raise InvalidCredentialsException()
        if not verify_pwd(password, user.hashed_password):
            raise InvalidCredentialsException()
        
        if not user.is_active:
            raise InactiveUserException()
        
        token = create_access_token(
            {
                "sub" : user.username,
                "user_id" : user.id,
                "role" : user.role.value
            }
        )

        return TokenResponse(
            access_token=token,
            token_type="bearer"
        )
    
    def register_user(db: Session, request: RegisterRequest) -> UserResponse:
        if UserRepository.get_by_username(db, request.username):
            raise UserAlreadyExistsException()
        
        if UserRepository.get_by_emp_id(db, request.employee_id):
            raise UserAlreadyExistsException()
        
        if UserRepository.get_by_email(db, request.email):
            raise UserAlreadyExistsException()

        user = User(
            username = request.username,
            email = request.email,
            hashed_password = hash_pwd(request.password),
            employee_id = request.employee_id,
            role = request.role
        )

        created_user = UserRepository.create(db, user)

        return UserResponse.model_validate(created_user)
        

    
