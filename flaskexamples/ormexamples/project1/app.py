# install flask-sqlalchemy
# we need to define SQLalchemy connection url
# we need to define a model
from urllib.parse import quote_plus
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisarandomgeneratedstring"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:{}@localhost:3306/demodb_1".format(quote_plus("rps@123"))

db = SQLAlchemy()
db.init_app(app)

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer,primary_key=True)
    customername = db.Column(db.String(50))
    customeremail = db.Column(db.String(50))

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/addcustomer', methods=['GET','POST'])
def addcustomer():
    if request.method == "POST":
        customername = request.form['customername']
        customeremail = request.form['customeremail']
        customer = Customer(customername=customername,customeremail=customeremail)
        db.session.add(customer)
        db.session.commit()
        return jsonify({'message':'customer added successfully'})

if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run()
