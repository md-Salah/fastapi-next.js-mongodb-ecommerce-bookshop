from jose import JWTError, jwt, ExpiredSignatureError
from decouple import config
from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi import status, HTTPException


JWT_SECRET = config('JWT_SECRET')
JWT_ALGORITHM = config('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str

# Create token with user info
def create_access_token(data: dict, ACCESS_TOKEN_EXPIRE_MINUTES: float = ACCESS_TOKEN_EXPIRE_MINUTES):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"expire": expire.__str__()})
    
    encoded_jwt = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM) # type: ignore
    return encoded_jwt
 
 
# Decode token & validate
def decode_and_validate_token(token:str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM]) # type: ignore
        format = '%Y-%m-%d %H:%M:%S.%f'
        if datetime.utcnow() <= datetime.strptime(decoded_token['expire'], format):
            return decoded_token 
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token has been expired. Login again.")

    except JWTError:
        raise credentials_exception
    
    