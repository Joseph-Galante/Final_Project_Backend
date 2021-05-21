from .User_Routes import User_Routes

def apply_routes (app):
    User_Routes.signup(app)
    User_Routes.login(app)
    User_Routes.verify_user(app)