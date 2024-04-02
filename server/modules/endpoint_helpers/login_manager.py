from flask import session

class LoginManager:
    def __init__(self, app):
        self.app = app

    def login(self, user_id):
        session['user_id'] = user_id

    def logout(self):
        session.pop('user_id', None)

    def is_logged_in(self):
        return 'user_id' in session

    def get_current_user_id(self):
        return session.get('user_id')
