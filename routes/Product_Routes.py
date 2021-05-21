# =================== SETUP =================== #

from controllers import Product_Controller


# =================== ROUTES =================== #

class Product_Routes ():

    def all_products (app):
        app.route('/products', methods=["GET", "POST"])(Product_Controller.all_products)

    def one_product (app):
        app.route('/products/<int:id>', methods=["GET", "DELETE"])(Product_Controller.one_product)