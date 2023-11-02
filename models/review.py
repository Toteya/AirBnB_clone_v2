#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    if models.storage_type == 'db':
        __tablename__ = 'reviews'

        text = Column('text', String(1024), nullable=False)
        place_id = Column('place_id', String(60), ForeignKey('places.id'),
                          nullable=False)
        user_id = Column('user_id', String(60), ForeignKey('users.id'),
                         nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
