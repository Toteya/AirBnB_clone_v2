#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

if models.storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == 'db':
        __tablename__ = 'places'

        city_id = Column('city_id', String(60), ForeignKey('cities.id'),
                         nullable=False)
        user_id = Column('user_id', String(60), ForeignKey('users.id'),
                         nullable=False)
        name = Column('name', String(128), nullable=False)
        description = Column('description', String(1024))
        number_rooms = Column('number_rooms', Integer, nullable=False,
                              default=0)
        number_bathrooms = Column('number_bathrooms', Integer, nullable=False,
                                  default=0)
        max_guest = Column('max_guest', Integer, nullable=False, default=0)
        price_by_night = Column('price_by_night', Integer, nullable=False,
                                default=0)
        latitude = Column('latitude', Float)
        longitude = Column('longitude', Float)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """Returns a list of amenity_ids related to this place"""
            amenities_list = []
            for obj in storage.all(Amenity).values():
                if obj.id in amenity_ids:
                    amenities_list.append(obj)
            return amenities_list

        @amenities.setter
        def amenities(self, obj=None):
            if isinstance(obj, models.amenity.Amenity):
                amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """Returns a list of reviews linked to this place
            """
            review_list = []
            for obj in models.storage.all(models.review.Reviews).values():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list
