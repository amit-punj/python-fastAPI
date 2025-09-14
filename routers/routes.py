from fastapi import APIRouter
from controllers.users_controller import get_users,UserbyID,create_user,update_user,delete_user
# from controllers.products import products

router = APIRouter()


@router.get('/users')
def users_route():
    return get_users()

@router.get('/UserbyID')
def users_route(user_id: int):
    return UserbyID(user_id)

@router.post('/create_user')
def user_route(user: dict):
    return create_user(user)

@router.put('/update_user')
def user_route():
    return update_user()

@router.delete('/delete_user')
def user_route():
    return delete_user()