from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash_pwd(password: str) -> str:
    return pwd_context.hash(password)

def verify_pwd(plain_pwd: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(plain_pwd, hashed_pwd)