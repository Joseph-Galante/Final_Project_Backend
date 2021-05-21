# =================== IMPORTS =================== #

# routes
from .User_Routes import User_Routes
from .Product_Routes import Product_Routes


# =================== METHODS =================== #

def apply_routes (app):
    User_Routes.signup(app)
    User_Routes.login(app)
    User_Routes.verify(app)
    User_Routes.update(app)
    User_Routes.get_reviews(app)
    User_Routes.get_products(app)
    User_Routes.get_orders(app)