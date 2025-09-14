from fastapi import APIRouter, Request
import controllers.users_controller as user_controller;
from schemas.userSchema import CreateUserSchema


router = APIRouter()

@router.get("/api/health")
def read_root():
    return {"message": "Hello, FastAPI Health API is running!"}

@router.get('/users')
def users_route():
    return user_controller.get_users()

@router.get('/UserbyID')
def users_route(user_id: str):
    return user_controller.UserbyID(user_id)

@router.post('/create_user')
def user_route(request: Request, user: CreateUserSchema):
    return user_controller.create_user(request, user)

@router.put('/update_user')
def user_route(username: str):
    return user_controller.update_user(username)

@router.delete('/delete_user')
def user_route():
    return user_controller.delete_user()