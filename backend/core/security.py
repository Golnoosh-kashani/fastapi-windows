from datetime import timedelta,datetime
from typing import Optional
from jose import JWTError,jwt
from core.config import settings


def create_access_token(data:dict,expire_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    if expire_delta:
        expire=datetime.utcnow+expire_delta
    else:
        expire=datetime.utcnow+timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITMS)
    return encoded_jwt        