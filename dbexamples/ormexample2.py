"""
Object Relational Mapping

Table -   Class in python script

Column  - Attributes of Class

Record - An instance of the class

ORM library for python - sqlalchemy - most widely used orm library

sqlchemy uses external libraries like pymysql to connect to the database

format of connection url = dialect+library://username:password@host:portnumber/dbname

mysql - localhost  root  password - demodb2

mysql+pymysql://root:password@localhost:3306/demodb2

"""

# installing sqlalchemy
# go to cmd
# python -m pip install sqlalchemy

from sqlalchemy import create_engine,Column,String,Integer
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker

Base =  declarative_base()

class Book(Base): # by default the table created with class name in lower case
    __tablename__ = "books" # creates the table with name 'books'

    bookid = Column(Integer, primary_key=True)
    booktitle = Column(String(50))

## the above completes class definition for book table
engine = create_engine("mysql+pymysql://root:admin_12345@localhost:3306/demodb2")

Base.metadata.create_all(engine)

session  = sessionmaker(bind=engine)

dbsession = session()

book = Book(booktitle='programming in ruby')

dbsession.add(book)
dbsession.commit()
