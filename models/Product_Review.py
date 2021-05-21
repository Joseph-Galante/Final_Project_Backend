from .db import db

class Product_Review (db.Model):
    __tablename__ = 'product_reviews'

    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))