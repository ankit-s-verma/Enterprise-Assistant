from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from backend.auth.auth_service import AuthService, TokenResponse, UserResponse, RegisterRequest
from backend.database.database import get_db
from backend.models.user import User
from backend.auth.dependencies import get_current_user


router = APIRouter(prefix='/auth', tags=["Authentication"])

@router.post("/login", response_model=TokenResponse, summary="Authenticate a user")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return AuthService.auth_user(db=db, username=form_data.username, password=form_data.password)

@router.post("/register", response_model=UserResponse, summary="Register a new user")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    return AuthService.register_user(db=db, request=request)

@router.get("/me", response_model=UserResponse, summary="Get current authenticated user")
def get_authed_user(current_user: User = Depends(get_current_user)):
    return UserResponse.model_validate(current_user)