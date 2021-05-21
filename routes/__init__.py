# =================== IMPORTS =================== #

# routes
from models import Product_Review
from .User_Routes import User_Routes
from .Product_Routes import Product_Routes


# =================== METHODS =================== #

def apply_routes (app):

    # user routes
    User_Routes.signup(app)
    User_Routes.login(app)
    User_Routes.verify(app)
    User_Routes.update(app)
    User_Routes.get_reviews(app)
    User_Routes.get_products(app)
    User_Routes.get_orders(app)

    # product routes
    Product_Routes.all_products(app)
    Product_Routes.one_product(app)