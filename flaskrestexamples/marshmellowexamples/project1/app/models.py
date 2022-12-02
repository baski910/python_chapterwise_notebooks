from app import db

class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
