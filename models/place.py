#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models import storage
from models.amenities import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy import Table


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"),
                     nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """gets the list of review"""
        review_list = [review for review in
                       list(storage.all(Review).values())
                       if review.place_id == self.id]
        return review_list

        @property
        def amenities(self):
            """gets the list of review"""
        amenities_list = [amenity for amenity in
                          list(storage.all(Amenity).values())
                          if amenity.id in self.amenity_ids]
        return amenities_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
