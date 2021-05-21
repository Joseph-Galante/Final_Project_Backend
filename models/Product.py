from os import name

from sqlalchemy.orm import backref
from .db import db

class Product (db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    reviews = db.relationship('Product_Review', backref='review')
    cart_items = db.relationship('Cart_Item', backref='product')

    def to_json (self):
        return {
            "name": self.name,
            "description": self.description
        }