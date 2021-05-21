from controllers import User_Controller

class User_Routes ():
    def signup (app):
        app.route('/users', methods=["POST"])(User_Controller.signup)
        
    def login (app):
        app.route('/users/login', methods=["POST"])(User_Controller.login)
    
    def verify_user (app):
        app.route('/users/verify', methods=["GET"])(User_Controller.verify_user)
