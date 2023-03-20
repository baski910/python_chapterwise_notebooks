# # install flask
# pip install flask
# flask templates are rendered using jinja2 templating module

from flask import Flask, render_template, request, jsonify, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY']='thisisarandomgeneratedstring'
app.config['SQLALCHEMY_DATABASE_URI']="postgresql+psycopg2://flaskexampleuser1:password@localhost:5432/flaskexample1"


db = SQLAlchemy(app)
auth = HTTPBasicAuth()


class Book(db.Model):
    __tablename__ = 'books' # the table will be created with the name as set for the variable __tablename__
    id = db.Column(db.Integer, primary_key=True)
    booktitle = db.Column(db.String(50))
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash =  generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

@auth.verify_password
def verfify_password(username_or_token, password):
    user = User.query.filter_by(username = username_or_token).first()
        
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

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

@app.route('/register', methods=['GET','POST'])
def register():
    username = request.json.get('username') 
    password = request.json.get('password')
    # Check for blank requests
    if username is None or password is None:
        abort(400)
    # Check for existing users
    if User.query.filter_by(username = username).first() is not None:
        abort(400)
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'username': user.username}), 201)



@app.route('/getJSON', methods=['GET','POST'])
@auth.login_required
def getjson():
    books = Book.query.all()
    list_of_books = []
    for book in books:
        d1 =  {}
        d1['id'] = book.id
        d1['booktitle'] = book.booktitle
        list_of_books.append(d1)
    return jsonify(list_of_books)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
