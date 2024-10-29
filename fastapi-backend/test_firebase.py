from utils.firebase_setup import db
from utils.db_operations import add_user

# Test Firebase and Firestore client initialization
print("Firestore client in test script:", db)

# Test adding a user (replace with test values)
add_user("testuser@example.com", "test_user_id")
print("User added to Firestore.")
