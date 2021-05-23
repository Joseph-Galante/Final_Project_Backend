# =================== SETUP =================== #

from controllers import Cart_Controller


# =================== ROUTES =================== #

class Cart_Routes ():

    def all_items (app):
        app.route('/cart', methods=["GET", "POST"])(Cart_Controller.all_items)

    def one_item (app):
        app.route('/cart/<int:id>', methods=["DELETE"])(Cart_Controller.one_item)