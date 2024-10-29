import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase():
    # Only initialize if Firebase has not been initialized yet
    if not firebase_admin._apps:
        cred = credentials.Certificate("config/sa-firebase-key.json")
        firebase_admin.initialize_app(cred)
        print("Firebase has been initialized")

# Initialize Firestore client after Firebase app is initialized
def get_firestore_client():
    return firestore.client()

# Ensure Firebase and Firestore are initialized once when this module is imported
initialize_firebase()
db = get_firestore_client()
print("Firestore client has been created:", db)