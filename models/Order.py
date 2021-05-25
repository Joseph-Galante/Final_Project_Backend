from .db import db

class Order (db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    total = db.Column(db.Float, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip = db.Column(db.String, nullable=False)
    card = db.Column(db.String, nullable=False)

    def to_json (self):
        return {
            "total": self.total,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "card": self.card,
            "cart_items": [i.to_json() for i in self.cart_items]
        }