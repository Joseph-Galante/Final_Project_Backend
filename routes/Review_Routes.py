# =================== SETUP =================== #

from controllers import Review_Controller


# =================== ROUTES =================== #

class Review_Routes ():

    def user_reviews (app):
        app.route('/reviews/users/<string:email>', methods=["POST"])(Review_Controller.user_reviews)

    def product_reviews (app):
        app.route('/reviews/products/<int:id>', methods=["POST"])(Review_Controller.product_reviews)