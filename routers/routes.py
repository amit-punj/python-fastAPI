from fastapi import APIRouter, Request, Depends
import controllers.UserController as user_controller;
import controllers.AuthController as auth_controller;
from schemas.userSchema import CreateUserSchema, LoginSchema    

router = APIRouter()

# Public routes (no authentication required)
@router.post("/sign_in")
def auth(request:Request, user:LoginSchema):
    print('user', user)
    return auth_controller.sign_in(request, user)

@router.post("/sign_up")
def auth(request:Request, user:CreateUserSchema):
    return auth_controller.sign_up(request, user)

# Protected routes (authentication required)
@router.get("/profile")
def profile(current_user: dict = Depends(auth_controller.get_current_user)):
    print('current_user in route', current_user)
    return auth_controller.profile(current_user)

@router.get('/users')
def users_route(current_user: dict = Depends(auth_controller.get_current_user)):
    return user_controller.get_users(current_user)

@router.get('/UserbyID')
def users_route(user_id: str, current_user: dict = Depends(auth_controller.get_current_user)):
    return user_controller.UserbyID(user_id)

@router.post('/create_user')
def user_route(request: Request, user: CreateUserSchema, current_user: dict = Depends(auth_controller.get_current_user)):
    return user_controller.create_user(request, user)

@router.put('/update_user')
def user_route(username: str, current_user: dict = Depends(auth_controller.get_current_user)):
    return user_controller.update_user(username)

@router.delete('/delete_user')
def user_route(current_user: dict = Depends(auth_controller.get_current_user)):
    return user_controller.delete_user()