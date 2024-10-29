from fastapi import APIRouter, HTTPException
from models import TopUpRequest
from utils.db_operations import get_user, top_up_balance

subscription_router = APIRouter()

@subscription_router.get("/check-subscription")
async def check_subscription(user_id: str):
    user_data = get_user(user_id)
    if user_data:
        return {
            "subscription": user_data["subscription"],
            "balance": user_data["balance"],
            "registration_date": user_data["registration_date"],
            "last_login_date": user_data["last_login_date"]
        }
    raise HTTPException(status_code=404, detail="User not found")

@subscription_router.post("/top-up")
async def top_up(data: TopUpRequest):
    new_balance = top_up_balance(data.user_id, data.amount)
    if new_balance is not None:
        return {"message": "Top-up successful", "new_balance": new_balance}
    raise HTTPException(status_code=404, detail="User not found")