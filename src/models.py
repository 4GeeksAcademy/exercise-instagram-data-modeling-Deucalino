import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id=Column(String(250), primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id=Column(String(250), primary_key=True)
    user_from_id = Column(String(250),ForeignKey('user.id'), nullable=False)
    user_to_id = Column(String(250),ForeignKey('user.id'), nullable=False)
   
    class Post(Base):
        __tablename__='post'
        id=Column(Integer, primary_key=True)
        user_id=Column(String(450), ForeignKey('user.id'))

class Media(Base):
   __tablename__='media'
   id = Column(Integer, primary_key=True)
   type=Column(Enum("picture","video",name="media_types"))
   url=Column(String(450))
   post_id=Column(Integer, ForeignKey('post.id'))
        
class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    comment_text=Column(String(450))
    author_id=Column(Integer, ForeignKey('user.id'))
    post_id=Column(Integer, ForeignKey('post.id'))
    
        

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
