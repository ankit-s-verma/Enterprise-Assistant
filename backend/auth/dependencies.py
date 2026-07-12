from fastapi import Depends
from jose import JWTError
from sqlalchemy.orm import Session
from backend.auth.exceptions import UnauthorizedException
from backend.database.database import get_db
from backend.auth.security import oauth2_scheme
from backend.models.user import User
from backend.repositories.user_repo import UserRepository
from backend.auth.jwt_handler import decode_access_token

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = decode_access_token(token)

        user_id = payload.get("user_id")

        if user_id is None:
            raise UnauthorizedException()
        
    except JWTError:
        raise UnauthorizedException()
    
    user = UserRepository.get_by_id(db=db, user_id= user_id)

    if user is None:
        raise UnauthorizedException()
    
    if not user.is_active:
        raise UnauthorizedException()
    
    return user
