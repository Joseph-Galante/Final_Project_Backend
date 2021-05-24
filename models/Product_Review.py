from .db import db
import models

class Product_Review (db.Model):
    __tablename__ = 'product_reviews'

    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def to_json (self):
        review = models.Review.query.filter(models.Review.id == self.review_id).first()
        return {
            "review": review.to_json()
        }