from fastapi import FastAPI
from utils.firebase_setup import initialize_firebase, get_firestore_client
from endpoints.auth import auth_router
from endpoints.subscription import subscription_router
from endpoints.user import user_router

app = FastAPI()

# Initialize Firebase
initialize_firebase()

# Get the Firestore client (only after initializing Firebase)
db = get_firestore_client()

# Register routes
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(subscription_router, prefix="/subscription", tags=["subscription"])
app.include_router(user_router, prefix="/user", tags=["user"])
