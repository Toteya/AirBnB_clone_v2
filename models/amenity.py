#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    if models.storage_type == 'db':
        __tablename__ = 'amenities'

        name = Column('name', String(128), nullable=False)
    else:
        name = ""
