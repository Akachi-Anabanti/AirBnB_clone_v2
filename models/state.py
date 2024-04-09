#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns a list of Cities"""
            city_list = [city for city in
                         list(models.storage.all(City).values())
                         if city.state_id == self.id]
            return city_list
