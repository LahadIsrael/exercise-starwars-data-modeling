import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_character = relationship('Charactrer', backref='user', uselist=False)
    favorite_planet = relationship('Planet', backref='user', uselist=False)
class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorite_id = Column(Integer, ForeignKey("user.id"))

class Planet(Base):
        __tablename__ = "planet"
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        planet_id = Column(Integer, ForeignKey("favorites.id"))
class Character(Base):
        __tablename__ = "character"
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
        character_id = Column(Integer, ForeignKey("favorites.id"))



#class Person(Base):
   # __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
   
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
