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
        return f"ID:{self.id},User:{self.user_name},GroupID:{self.group_id}"




engine = create_engine('mysql+pymysql://admin:root@123@localhost:3306/demodb_1')
Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)

dbsession = session()

'''

dbsession =session()

g=Group(group_name='developers')
dbsession.add(g)
dbsession.commit()

user = User(user_name='bob')
user.group = g
dbsession.add(user)
dbsession.commit()

user = User(user_name='tom')
user.group = g
dbsession.add(user)
dbsession.commit()
'''
print(dbsession.query(User).limit(1).all())

#exists = session.query(User).filter_by(name='rohit').scalar() is not None

#print(exists)
'''
g=Group(group_name='developer')
session.add(g)
session.commit()

u=session.query(User).filter_by(name='andrew').first()
u.group = g
session.commit()
'''
