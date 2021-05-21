# =================== SETUP =================== #

# flask requests
from flask import request

# package imports
import models
import middleware


# =================== METHODS =================== #

class Product_Controller ():

    # all products
    def all_products ():
        # get all products
        if request.method == "GET":
            # grab all products
            products = models.Product.query.all()
            
            return { 'message': 'Products found', 'products': [p.to_json() for p in products] }
        # add product
        elif request.method == "POST":
            # grab user using encrypted id
            user = middleware.User_Auth.verify_user(request.headers["Authorization"])
            # check if user exists
            if user:
                # create product
                product = models.Product(
                    name = request.json["name"],
                    desrciption = request.json["desrciption"]
                )

                # add product to user
                user.products.append(product)

                # commit to session
                models.db.session.add_all(user, product)
                models.db.session.commit()

                return { 'message': 'Product created', 'product': product.to_json() }
            # no user
            else:
                return { 'message': 'No user found' }, 401

    def one_product (id):
        # get one product
        if request.method == "GET":
            # grab one product
            product = models.Product.query.filter(models.Product.id == id).first()
            # check if product exists
            if product:
                return { 'message': 'Product found', 'product': product.to_json() }
            # no product
            else:
                return { 'message': 'No product found' }, 404
        # remove product
        elif request.method == "DELETE":
            # grab user using encrypted id
            user = middleware.User_Auth.verify_user(request.headers["Authorization"])
            # check if user exists
            if user:
                # grab one product
                product = models.Product.query.filter(models.Product.id == id).first()
                # check if product exists
                if product:
                    # check if user listed product
                    if middleware.Product_Utils.verify_lister(product, user):
                        # remove product
                        models.db.session.delete(product)
                        models.db.session.commit()

                        return { 'message': 'Product deleted', 'product': product.to_json() }
                # no product
                else:
                    return { 'message': 'No product found' }, 404
            # no user
            else:
                return { 'message': 'No user found' }, 401