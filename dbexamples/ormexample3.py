from sqlalchemy import *
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
import pymysql

Base = declarative_base()


class Group(Base):
     __tablename__ = 'groups'
     id = Column(Integer, primary_key = True)
     group_name = Column(String(50))
     def __repr__(self):
         return '<Group({},{}>'.format(self.id,self.name)   

class User(Base):
     __tablename__ = 'users'
     id = Column(Integer, primary_key = True)
     user_name = Column(String(50))
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

# fetching related users from group
groups = dbsession.query(Group).all()
for group in groups:
    print(group, group.users) # group.users - returns the relevant records from users table


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
