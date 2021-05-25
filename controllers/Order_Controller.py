# =================== SETUP =================== #

# flask requests
from flask import request

# package imports
import models
import middleware


# =================== METHODS =================== #

class Order_Controller ():

    def all_orders ():
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            if request.method == 'GET':
                # grab user's orders
                orders = user.orders
                
                return { 'message': 'Orders found', 'orders': [o.to_json() for o in orders] }
            if request.method == 'POST':
                # create new order
                order = models.Order(
                    total = request.json["total"],
                    address = request.json["address"],
                    city = request.json["city"],
                    state = request.json["state"],
                    zip = request.json["zip"],
                    card = request.json["card"]
                )
                # add order to user
                user.orders.append(order)
                # mark order items as complete
                for item in user.cart_items:
                    item.order = order
                    item.complete = True
                    models.db.session.add(item)

                # commit to session
                models.db.session.add_all([order, user])
                models.db.session.commit()

                return { 'message': 'Order created', 'order': order.to_json() }
        # no user
        else:
            return { 'message': 'No user found' }, 401