# =================== SETUP =================== #

# controller
from controllers import User_Controller


# =================== ROUTES =================== #

class User_Routes ():
    
    def signup (app):
        app.route('/users', methods=["POST"])(User_Controller.signup)
        
    def login (app):
        app.route('/users/login', methods=["POST"])(User_Controller.login)
    
    def verify (app):
        app.route('/users/verify', methods=["GET"])(User_Controller.verify)

    def update (app):
        app.route('/users/update', methods=["PUT"])(User_Controller.update)

    def get_reviews (app):
        app.route('/users/reviews', methods=["GET"])(User_Controller.get_reviews)

    def get_products (app):
        app.route('/users/products', methods=["GET"])(User_Controller.get_products)

    def get_orders (app):
        app.route('/users/orders', methods=["GET"])(User_Controller.get_orders)
