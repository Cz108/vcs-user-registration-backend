from fastapi import APIRouter, HTTPException
from utils.db_operations import get_user

user_router = APIRouter()

@user_router.get("/profile")
async def get_user_profile(user_id: str):
    user_data = get_user(user_id)
    if user_data:
        return user_data
    raise HTTPException(status_code=404, detail="User not found")
