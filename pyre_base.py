import pyrebase
from requests import HTTPError

config = {"apiKey": "AIzaSyCxdRG6EeSOUEH6J-SJwUgHqzGziHou1CE",
          "authDomain": "uet-truyen.firebaseapp.com",
          "databaseURL": "https://uet-truyen-default-rtdb.asia-southeast1.firebasedatabase.app",
          "projectId": "uet-truyen",
          "storageBucket": "uet-truyen.appspot.com",
          "messagingSenderId": "307799266904",
          "appId": "1:307799266904:web:caa1a7206fea03b0051c2d",
          "measurementId": "G-3VTSM0WPYG"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def sign_in(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print('Signed in as: {0}'.format(user['email']))
        return user
    except HTTPError as http_error:
        print(http_error.strerror)


def sign_up(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print('Signed up as: {0}'.format(user['email']))
        return user
    except HTTPError as http_error:
        print(http_error.strerror)