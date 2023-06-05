from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel


router = APIRouter(
    prefix="/users",
    tags=["USERS"],
    responses={404: {"description": "Not found"}},
)

users = [
    {"id": 1, "username": "Rick", "email": "rick@example.com", "password": "123456"},
    {"id": 2, "username": "lel", "email": "lel@example.com", "password": "1234"},
    {"id": 3, "username": "noman", "email": "noman@example.com", "password": "3456"},
]

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
    
    
# Get All Users
@router.get("/")
async def get_users():
    return users

# Get User by id
@router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    for user in users:
        if user['id'] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Create User
@router.post("/")
async def create_user(user: UserSchema):
    users.append(user.dict())
    return users[-1]

# Update User
@router.put("/{user_id}")
async def update_user(user_id: int, user: UserSchema):
    for u in users:
        if u['id'] == user_id:
            u['username'] = user.username
            u['email'] = user.email
            u['password'] = user.password
            return u
    raise HTTPException(status_code=404, detail="User not found")


# Delete User
@router.delete('/{user_id}')
async def delete_user(user_id: int):
    global users
    users = [d for d in users if d['id'] != user_id]
    return {'msg': 'User is removed'}
