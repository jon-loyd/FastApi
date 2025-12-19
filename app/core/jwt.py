from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status
import jwt
from app.core.config import settings

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.jwt_secret,
        algorithm=settings.encoding_algorithm
    )

def verify_access_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.encoding_algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
            )
        return user_id
    except jwt.PyJWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        ) from e
