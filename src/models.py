import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    username = Column(String(250), primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    f_username = Column(String(250), primary_key=True)
    f_name = Column(String(250), nullable=False)
    f_lastname = Column(String(250), nullable=False)

    class MyProfile(Base):
        __tablename__='myprofile'
        post_id=Column(Integer, primary_key=True)
        post=Column(String(450), ForeignKey('post.username'))
        post=relationship(User)
        comment_id=Column(Integer, primary_key=True)
        comment=Column(String(450), ForeignKey('comment.username'))
        comment=relationship(User)
        stories_id=Column(Integer, primary_key=True)
        stories=Column(String(450), ForeignKey('stories.username'))
    class Favorites(Base):
        best_stories=Column(String(450), ForeignKey('stories.stories_id'))
        best_post=Column(String(450), ForeignKey('post.post_id'))
        user=relationship(User)
        

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
