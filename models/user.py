#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128))
    last_name = Column('last_name', String(128))
    places = relationship('Place', backref='user',
                          cascade="all, delete")
    reviews = relationship('Review', backref='user',
                           cascade="all, delete")
