from typing import Annotated
from pydantic import BaseModel
from app.auth.auth_handler import create_access_token, decode_and_validate_token, Token
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


router = APIRouter(
    prefix="/auth",
    tags=["AUTHENTICATION"],
    responses={404: {"description": "Not found"}},
)

users = []

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    password: str
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "username": "example name",
                "email": "example@example.com",
                "password": "123456"
            }
        }
        
        


# @router.post('/token')
# async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=400, detail='Invalid username or password')
#     return signJWT(user.username)


# @router.post('/signup')
# async def user_signup(user: UserSchema):

#     if check_user(user):
#         raise HTTPException(status_code=400, detail='User already registered')
    
#     user.id = len(users) + 1
#     users.append(user)
#     return signJWT(user.id)

@router.get('/me')
async def profile(token: str = Depends(oauth2_scheme)):
    decoded_token = decode_and_validate_token(token)
    return {'name': 'Your profile page'}


@router.post('/login', response_model=Token)
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    
    user = authenticate_user(users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({"username": form_data.username})
    
    return {"access_token": access_token, "token_type": "bearer", "username": form_data.username}


def check_user(data: UserSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


def authenticate_user(db, username: str, password: str):
    return {'username': username}

