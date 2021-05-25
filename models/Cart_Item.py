from models import User
from sqlalchemy.orm import backref
from .db import db
import models

class Cart_Item (db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    complete = db.Column(db.Boolean, nullable=False)
    
    order = db.relationship('Order', backref='cart_items')

    def to_json (self):
        product = models.Product.query.filter(models.Product.id == self.product_id).first()
        return {
            "id": self.id,
            "complete": self.complete,
            "product": product.to_json()
        }