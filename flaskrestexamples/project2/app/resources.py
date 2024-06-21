from flask import request
from flask_restful import Resource
from app import db
from .models import Book
from .shcemas import BookSchema

book_schema = BookSchema()
books_schema = BookSchema(many=True)

class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return books_schema.dump(books) 
    
    def post(self):
        new_book = Book(title= request.json['title'])
        db.session.add(new_book)
        db.session.commit()
        return book_schema.dump(new_book)

