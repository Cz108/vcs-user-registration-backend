from datetime import datetime
from utils.firebase_setup import get_firestore_client

def add_user(email, user_id):
    db = get_firestore_client()
    user_data = {
        "email": email,
        "subscription": "free",      # Default subscription status
        "balance": 0.0,              # Initial balance
        "registration_date": datetime.now(),
        "last_login_date": datetime.now()
    }
    db.collection("users").document(user_id).set(user_data)

def get_user(user_id):
    db = get_firestore_client()
    user_doc = db.collection("users").document(user_id).get()
    if user_doc.exists:
        return user_doc.to_dict()
    return None

def update_last_login(user_id):
    db = get_firestore_client()
    db.collection("users").document(user_id).update({
        "last_login_date": datetime.now()
    })

def top_up_balance(user_id, amount):
    db = get_firestore_client()
    """
    Increases the balance of a user by the specified amount.
    """
    user_ref = db.collection("users").document(user_id)
    user_doc = user_ref.get()
    if user_doc.exists:
        new_balance = user_doc.get("balance", 0.0) + amount
        user_ref.update({"balance": new_balance})
        return new_balance
    return None
