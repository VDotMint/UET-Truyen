"""_summary_
    """
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate(
    "src/DO_NOT_PUSH.json")
firebase_admin.initialize_app(cred)


def create_user(email: str, password: str):
    """_summary_

    Args:
        email (str): _description_
        password (str): _description_
    """
    # TODO: xử lý exception
    auth.create_user(email=email, password=password)
