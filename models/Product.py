from os import name
from typing import Reversible

from .db import db

class Product (db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    reviews = db.relationship('Product_Review', backref='product')
    cart_items = db.relationship('Cart_Item', backref='product')

    def to_json (self, include_reviews=False):
        if include_reviews:
            return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "price": self.price,
                "image": self.image if self.image else 'No image',
                "seller": self.user.to_json(),
                "reviews": [r.to_json() for r in self.reviews]
            }
        else:
            return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "price": self.price,
                "image": self.image if self.image else 'No image'
            }