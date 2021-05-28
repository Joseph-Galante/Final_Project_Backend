from .db import db
import models

class User_Review (db.Model):
    __tablename__ = 'user_reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))

    def to_json (self):
        review = models.Review.query.filter(models.Review.id == self.review_id).first()
        return {
            "id": self.id,
            "review": review.to_json(include_orders=False)
        }