from sqlalchemy import *
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
import pymysql

Base = declarative_base()


class Group(Base):
     __tablename__ = 'groups'
     id = Column(Integer, primary_key = True)
     name = Column(String(50))
     def __repr__(self):
         return '<Group({},{}>'.format(self.id,self.name)   

class User(Base):
     __tablename__ = 'users'
     id = Column(Integer, primary_key = True)
     name = Column(String(50))
     group_id = Column(Integer,ForeignKey('groups.id'),index=True)
     group = relationship('Group',lazy = False, backref = 'users')

     def __init__(self,name):
         self.name = name

     def __repr__(self):
         return '<User({},{}>'.format(self.id,self.name)




engine = create_engine('mysql+pymysql://admin:root@123@localhost:3306/demodb_1')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

'''
user = User(name='andrew')
session.add(user)
session.commit()
'''
print(session.query(User).limit(1).all())

exists = session.query(User).filter_by(name='rohit').scalar() is not None

print(exists)

g=Group(name='developer')
session.add(g)
session.commit()

u=session.query(User).filter_by(name='andrew').first()
u.group = g
session.commit()
