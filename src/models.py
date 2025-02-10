import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    name = Column(String(32), unique=False, nullable=True) 
    password = Column(String(80), unique=False, nullable=False)

    fav_planets = relationship("Fav_Planet", back_populates="user",cascade="all, delete-orphan")
    fav_peoples = relationship("Fav_People", back_populates="user",cascade="all, delete-orphan")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name":self.name,
        }
    
class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    diameter = Column(Integer, unique=False, nullable=False)
    rotation_period = Column(Integer, unique=False, nullable=False)
    gravity = Column(Integer, unique=False, nullable=False)
    img = Column(String(250), unique=False, nullable=True)

    fav_planets = relationship("Fav_Planet", back_populates="planet",cascade="all, delete-orphan")

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter":self.diameter,
            "rotation_period":self.rotation_period,
            "gravity": self.gravity,
            "img": self.img,
        }
    
class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    hair_color = Column(String(20), unique=True, nullable=False)
    height = Column(String(20), unique=True, nullable=False)
    skin_color = Column(String(20), unique=True, nullable=False)
    gender = Column(String(20), unique=True, nullable=False)
    img = Column(String(250), unique=False, nullable=True)

    fav_peoples = relationship("Fav_People", back_populates="people",cascade="all, delete-orphan")

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color":self.hair_color,
            "height":self.height,
            "skin_color": self.skin_color,
            "gender": self.gender,
            "img": self.img,
        }
    
class Fav_Planet(Base):
    __tablename__ = 'fav_planet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    user = relationship('User', back_populates="fav_planets", uselist=False, single_parent=True)
    planet = relationship('Planet', back_populates="fav_planets", uselist=False, single_parent=True)



    def __repr__(self):
        return '<Favorites_Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }  
    
class Fav_People(Base):
    __tablename__ = 'fav_people'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.id'))

    user = relationship('User', back_populates="fav_peoples", uselist=False, single_parent=True)
    people = relationship('People', back_populates="fav_peoples", uselist=False, single_parent=True)



    def __repr__(self):
        return '<Favorites_people %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id,
        }  

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
