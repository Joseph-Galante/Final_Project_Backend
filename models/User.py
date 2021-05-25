import os
import jwt

from .db import db

class User (db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    user_reviews = db.relationship('User_Review', backref='user')
    reviews = db.relationship('Review', backref='user')
    cart_items = db.relationship('Cart_Item', backref='user')
    products = db.relationship('Product', backref='user')
    orders = db.relationship('Order', backref='user')

    def to_json (self, include_orders=False):
        encrypted_id = jwt.encode({ 'user_id': self.id }, os.environ.get('JWT_SECRET'), algorithm='HS256')

        if include_orders:
            return {
                "id": encrypted_id,
                "name": self.name,
                "email": self.email,
                "orders": [o.to_json() for o in self.orders]
            }
        else:
            return {
                "id": encrypted_id,
                "name": self.name,
                "email": self.email
            }