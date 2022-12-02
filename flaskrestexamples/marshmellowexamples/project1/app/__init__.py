import os
from flask import Flask,request,render_template
#from flask_restful import Api,Resource
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db =  SQLAlchemy()
ma = Marshmallow()
#api = Api()

def create_app():
    from .models import Book
    from .schemas import BookSchema
    from .resources import BookListResource
    app = Flask(__name__,instance_path=os.getcwd(),instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    ma.init_app(app)
    

    migrate = Migrate(app,db)
    
    #api.add_resource(BookListResource,'/books')

    return app



