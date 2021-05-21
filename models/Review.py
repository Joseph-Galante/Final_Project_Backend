from .db import db

class Review (db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user_reviews = db.relationship('User_Review', backref='review')
    product_reviews = db.relationship('Product_Review', backref='review')

    def to_json (self):
        return {
            "description": self.description,
            "rating": self.rating
        }