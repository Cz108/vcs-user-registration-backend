from fastapi import APIRouter, HTTPException
from models import RegisterRequest, LoginRequest
from utils.db_operations import add_user, update_last_login
from utils.firebase_setup import db 
from firebase_admin import auth

auth_router = APIRouter()

@auth_router.post("/register")
async def register_user(data: RegisterRequest):
    try:
        # Attempt to create the user in Firebase
        user = auth.create_user(email=data.email, password=data.password)
        
        # Add user information to Firestore or your database
        add_user(data.email, user.uid)
        
        # Return success response
        return {"message": "User registered successfully", "user_id": user.uid}
    except Exception as e:
        # Log the exception and include it in the response for troubleshooting
        print(f"Registration error: {e}")
        raise HTTPException(status_code=400, detail=f"Registration failed: {e}")

@auth_router.post("/login")
async def login_user(data: LoginRequest):
    try:
        user = auth.get_user_by_email(data.email)
        update_last_login(user.uid)
        return {"message": "Login successful", "user_id": user.uid}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")
