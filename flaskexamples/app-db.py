# install flask
# pip install flask
# flask templates are rendered using jinja2 templating module

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']='thisisarandomgeneratedstring'
app.config['SQLALCHEMY_DATABASE_URI']="postgresql+psycopg2://flaskexampleuser1:password@localhost:5432/flaskexample1"


db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books' # the table will be created with the name as set for the variable __tablename__
    id = db.Column(db.Integer, primary_key=True)
    booktitle = db.Column(db.String(50))

@app.route('/')                               # / - http://localhost:5000
def books():
    books = Book.query.all()
    return render_template("home.html",books = books)
    #return "My First Web page from flask"     # /playVideo - http://localhost:5000/playVideo

@app.route('/addBook', methods=['GET','POST'])
def addBook():
    if request.method == "POST":
        title = request.form['booktitle']
        book = Book(booktitle=title)
        db.session.add(book)
        db.session.commit()
    return redirect(url_for('books'))

@app.route('/getJSON')
def getjson():
    return jsonify({'message': 'welcome to flask'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
