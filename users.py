"""Create and look up users."""
import db
from models import User


def create_user(user_id, name, email):
    user = User(user_id, name, email)
    db.save("users", user_id, user)
    return user


def get_user(user_id):
    return db.get("users", user_id)
