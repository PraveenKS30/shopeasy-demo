"""Very simple 'login' check (demo only - not real security)."""
import users


def login(user_id):
    """Return the user if they exist, otherwise None."""
    return users.get_user(user_id)
