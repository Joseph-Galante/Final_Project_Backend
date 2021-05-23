# =================== SETUP =================== #

from controllers import Order_Controller


# =================== ROUTES =================== #

class Order_Routes ():

    def all_orders (app):
        app.route('/orders', methods=["GET", "POST"])(Order_Controller.all_orders)