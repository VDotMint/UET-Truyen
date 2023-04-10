"""_summary_
    """
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin._auth_utils import EmailAlreadyExistsError
from requests.exceptions import HTTPError

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
    except HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except EmailAlreadyExistsError as email_error:
        print(f'Email already exists: {email_error}')
    except Exception as e:
        print(f'An error occurred: {e}')
            

create_user('21021512@vnu.edu.vn', '21021512')