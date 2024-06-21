from app import db
class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer,primary_key=True)
    customername = db.Column(db.String(50))
    customeremail = db.Column(db.String(50))
