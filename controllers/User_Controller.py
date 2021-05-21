from flask import Flask, request
app = Flask(__name__)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import models
import middleware

class User_Controller ():
    def signup ():
        existing_user = models.User.query.filter(models.User.email == request.json["email"]).first()
        if existing_user:
            return { 'message': 'Email must be unique'}, 409

        hashed_pw = bcrypt.generate_password_hash(request.json["password"]).decode('utf-8')
        user = models.User(
            name = request.json["name"],
            email = request.json["email"],
            password = hashed_pw
        )

        models.db.session.add(user)
        models.db.session.commit()

        return { 'message': 'Signup successful', 'user': user.to_json() }

    def login ():
        user = models.User.query.filter(models.User.email == request.json["email"]).first()
        if user:
            if bcrypt.check_password_hash(user.password, request.json["password"]):
                return { 'message': 'Login successful', 'user': user.to_json() }
            else:
                return { 'message': 'Incorrect password' }, 401
        else:
            return { 'message': 'No user found' }, 404

    def verify_user ():
        user = middleware.User_Auth.verify_user(request.headers["Authorization"])
        if user:
            return { 'message': 'User verified', 'user': user.to_json() }
        else:
            return { 'message': 'No user found' }, 404