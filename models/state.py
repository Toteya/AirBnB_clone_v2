#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column('name', String(128), nullable=False)
    cities = relationship("City", back_populates="state")

    # when State instance is deleted, all linked city instances must be deleted
