# =================== SETUP =================== #

# flask
from flask import Flask, request
app = Flask(__name__)

# hashing passwords
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# package imports
import models
import middleware


# =================== METHODS =================== #

class User_Controller ():

    # create user
    def signup ():
        # check for existing user with email
        existing_user = models.User.query.filter(models.User.email == request.json["email"]).first()
        if existing_user:
            return { 'message': 'Email must be unique'}, 409

        # hash password
        hashed_pw = bcrypt.generate_password_hash(request.json["password"]).decode('utf-8')
        # create user
        user = models.User(
            name = request.json["name"],
            email = request.json["email"],
            password = hashed_pw
        )
        # commit to session
        models.db.session.add(user)
        models.db.session.commit()

        return { 'message': 'Signup successful', 'user': user.to_json() }

    # login user
    def login ():
        # grab user by email
        user = models.User.query.filter(models.User.email == request.json["email"]).first()
        # check if user exists
        if user:
            # check if passwords match
            if bcrypt.check_password_hash(user.password, request.json["password"]):
                return { 'message': 'Login successful', 'user': user.to_json() }
            else:
                return { 'message': 'Incorrect password' }, 401
        # no user
        else:
            return { 'message': 'No user found' }, 404

    # verify logged in user
    def verify ():
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            return { 'message': 'User verified', 'user': user.to_json() }
        # no user
        else:
            return { 'message': 'No user found' }, 401

    # edit user's info
    def update ():
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])

        # check if user exists
        if user:
           # check for existing user with email
            if user.email != request.json["email"]:
                existing_user = models.User.query.filter(models.User.email == request.json["email"]).first()
                if existing_user:
                    return { 'message': 'Duplicate emails'}, 409
            
            # update user info
            user.name = request.json["name"]
            user.email = request.json["email"]
            # commit to session
            models.db.session.add(user)
            models.db.session.commit()
            
            return { 'message': 'User updated successfully', 'user': user.to_json() }
        # no user
        else:
            return { 'message': 'No user found' }, 401

    # get user reviews about user
    def get_reviews ():
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            # grab user reviews
            reviews = user.user_reviews

            return { 'message': 'User reviews found', 'reviews': [r.to_json() for r in reviews] }
        # no user
        else:
            return { 'message': 'No user found' }, 401

    # get user's products
    def get_products ():
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            # grab products
            products = user.products

            return { 'message': 'User products found', 'products': [p.to_json() for p in products] }
        # no user
        else:
            return { 'message': 'No user found' }, 401

    # get user's orders
    def get_orders ():
        # grab user using encrypted id
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        # check if user exists
        if user:
            # grab orders
            orders = user.orders

            return { 'message': 'User orders found', 'orders': [o.to_json() for o in orders] }
        # no user
        else:
            return { 'message': 'No user found' }, 401
