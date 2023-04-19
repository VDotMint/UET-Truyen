import pyre_base

class UserWrapper:
    def __init__(self, user):
        self.user = user


    def get_user_info(self):
        return pyre_base.db.child("users").child(user['localId']).get().val()