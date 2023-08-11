from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base): # book
    __tablename__ = 'books' # table will be created with the value assinged to __tablename__
    bookid = Column(Integer, primary_key=True)
    booktitle = Column(String(50))

    def __repr__(self):
        return f"ID:{self.bookid},Title:{self.booktitle}"

engine = create_engine("postgresql+psycopg2://demodbuser_1:password@localhost:5432/demodb_1")

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)
dbsession = session()

# add records
book = Book()
book.bookid = 1
book.booktitle = 'programming in cpp'

dbsession.add(book)
dbsession.commit()

book2 = Book()
book2.bookid = 2
book2.booktitle = 'programming in ruby'

dbsession.add(book2)
dbsession.commit()

# fetch records
records = dbsession.query(Book).all()

for record in records:
    print(record)
