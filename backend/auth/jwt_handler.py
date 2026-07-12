from datetime import datetime, timedelta, timezone
from typing import Any
from jose import jwt
from backend.core.configure import settings

def create_access_token(data: dict[str: Any]) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc)+ timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"expire": expire.timestamp()})

    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encode_jwt

def decode_access_token(token: str) -> dict[str, Any]:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
    return payload