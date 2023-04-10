"""DEPRECATED - use pyrebase4 instead
    """
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin._auth_utils import EmailAlreadyExistsError

cred = credentials.Certificate(
    "src/secret.json")
firebase_admin.initialize_app(cred)


def create_user(email: str, password: str):
    """_summary_

    Args:
        email (str): _description_
        password (str): _description_
    """
    try:
        auth.create_user(email=email, password=password)
        return "Success"
    except EmailAlreadyExistsError as e:
        return e.default_message
    except Exception as e:
        return e

def sign_in(email: str, password: str):
    """_summary_

    Args:
        email (str): _description_
        password (str): _description_
    """
    try:
        auth.
        return "Success"
    except Exception as e:
        return e