# =================== IMPORTS =================== #

# routes
from models import Product_Review
from .User_Routes import User_Routes
from .Product_Routes import Product_Routes
from .Cart_Routes import Cart_Routes
from .Order_Routes import Order_Routes
from .Review_Routes import Review_Routes


# =================== METHODS =================== #

def apply_routes (app):

    # user routes
    User_Routes.signup(app)
    User_Routes.login(app)
    User_Routes.verify(app)
    User_Routes.update(app)
    User_Routes.get_reviews(app)
    User_Routes.get_products(app)

    # product routes
    Product_Routes.all_products(app)
    Product_Routes.one_product(app)

    # cart routes
    Cart_Routes.all_items(app)
    Cart_Routes.one_item(app)

    # order routes
    Order_Routes.all_orders(app)

    # review routes
    Review_Routes.user_reviews(app)
    Review_Routes.product_reviews(app)