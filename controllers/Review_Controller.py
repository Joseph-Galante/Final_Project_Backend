# =================== SETUP =================== #

# flask requests
from flask import request

# package imports
import models
import middleware


# =================== METHODS =================== #

class Review_Controller ():

    def user_reviews (id):
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            if request.method == "POST":
                # grab reviewee using encrypted id
                reviewee = middleware.User_Auth.verify_user(id)
                # check if reviewee exists
                if reviewee:
                    # create review
                    review = models.Review(
                        description = request.json["description"],
                        rating = request.json["rating"]
                    )
                    # add review to user
                    user.reviews.append(review)

                    # create user review
                    user_review = models.User_Review()
                    # add reviewee and review to user_review
                    reviewee.user_reviews.append(user_review)
                    review.user_reviews.append(user_review)

                    # commit to session
                    models.db.session.add_all([review, user, reviewee, user_review])
                    models.db.session.commit()

                    return { 'message': 'User review posted', 'review': review.to_json() }
                # invalid email
                else:
                    return { 'message': 'No user with email found' }, 404
        # no user
        else:
            return { 'message': 'No user found' }, 401

    def product_reviews (id):
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            if request.method == "POST":
                # grab product by id
                product = models.Product.query.filter(models.Product.id == id).first()
                # check if product exists
                if product:
                    # create review
                    review = models.Review(
                        description = request.json["description"],
                        rating = request.json["rating"]
                    )
                    # add review to user
                    user.reviews.append(review)

                    # create product review
                    product_review = models.Product_Review()
                    # add product and review to product_review
                    product.reviews.append(product_review)
                    review.product_reviews.append(product_review)

                    # commit to session
                    models.db.session.add_all([review, user, product, product_review])
                    models.db.session.commit()

                    return { 'message': 'Product review posted', 'review': review.to_json() }
                # invalid email
                else:
                    return { 'message': 'No product found' }, 404
        # no user
        else:
            return { 'message': 'No user found' }, 401
        