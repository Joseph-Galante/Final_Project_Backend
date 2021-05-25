# =================== SETUP =================== #

# flask requests
from flask import request

# package imports
import models
import middleware


# =================== METHODS =================== #

class Cart_Controller ():

    def all_items ():
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            if request.method == 'GET':
                # grab user's cart
                cart = models.Cart_Item.query.filter(models.Cart_Item.user_id == user.id and models.Cart_Item.complete == False).all()

                return { 'message': 'Cart found', 'cart': [item.to_json() for item in cart]}
            elif request.method == 'POST':
                # grab product to add
                product = models.Product.query.filter(models.Product.id == request.json["product_id"]).first()
                # check if product exists
                if product:
                    # create cart item
                    item = models.Cart_Item(
                        complete = False
                    )
                    # add item to user and product
                    user.cart_items.append(item)
                    product.cart_items.append(item)
                    # commit to session
                    models.db.session.add_all([user, product, item])
                    models.db.session.commit()

                    return { 'message': 'Item added to cart', 'item': item.to_json() }
                # no product
                else:
                    return { 'message': 'No product found' }, 404                    
        # no user
        else:
            return { 'message': 'No user found' }, 401

    def one_item (id):
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            if request.method == 'DELETE':
                # grab item to be removed
                item = models.Cart_Item.query.filter(models.Cart_Item.id == id).first()
                # check if item is from user's cart
                if middleware.Cart_Utils.verify_owner(item, user):
                    # remove item
                    models.db.session.delete(item)
                    # commit to session
                    models.db.session.commit()

                    return { 'message': 'Item removed from cart', 'item': item.to_json() }
                # user does not own cart item
                else:
                    return { 'message': 'Unauthorized to remove item' }, 401
        # no user
        else:
            return { 'message': 'No user found' }, 401