#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column('name', String(128), nullable=False)
    if models.storage_type == 'db':
        cities = relationship('City', back_populates="state",
                              cascade="all, delete")

    @property
    def cities(self):
        """ Returns list of cities whose state_id matches the
        current State instance's id
        """
        city_list = []
        for obj in models.storage.all().values():
            if isinstance(obj, models.city.City) and obj.state_id == self.id:
                city_list.append(obj)
        return city_list
