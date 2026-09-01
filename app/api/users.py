from fastapi import APIRouter
from app.schemas.user import User
from app.services.database import check_check, table

router = APIRouter()

@router.post("/users")
def create_users(user: User):
    data = check_check()

    user_id = len(data)
    table.insert({"id": user_id, "name": user.name, "age": user.age}).execute()

    return user_id

@router.get("/users")
def get_users():
    data = check_check()

    return data

@router.get("/users/{user_id}")
def get_user(user_id: int):
    data = check_check()

    return data[user_id]

@router.delete("/users/{user_id}")
def del_user(user_id: int):
    table.delete().eq("id", user_id).execute()

    return {"message": f"User {user_id} deleted"}

@router.put("/users/{user_id}")
def put_user(user_id: int, user: User):
    table.update({"name": user.name, "age": user.age}).eq("id", user_id).execute()

    return {"message": f"The user {user_id} changed"}