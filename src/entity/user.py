import time
from pyre_base import db


class UserWrapper:
    '''User wrapper class
    user: fb_user object from pyre_base'''

    def __init__(self, fb_user):
        self.user = fb_user

    def get_user_info(self):
        '''Get user info from database'''
        return db.child("self.users").child(self.user['localId']).get().val()

    def get_following(self):
        '''Get following list from database'''
        return db.child("following").child(self.user['localId']).get().val()

    def get_history(self):
        '''Get history list from database (sorted by time)'''
        return db.child("history").child(self.user['localId']).order_by_value().get().val()

    def follow(self, comic_id):
        '''Add comic to following list
        comic_id: comic id'''
        db.child("following").child(
            self.user['localId']).child(comic_id).set(True, self.user['idToken'])

    def unfollow(self, comic_id):
        '''Remove comic from following list
        comic_id: comic id'''
        db.child("following").child(
            self.user['localId']).child(comic_id).remove()

    def add_history(self, comic_id):
        '''Add comic to history list and set cu
        comic_id: comic id'''
        db.child("history").child(self.user['localId']).child(
            comic_id).set(time.time(), self.user['idToken'])
