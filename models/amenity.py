#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column


class Amenity(BaseModel):
    """Represents the Amenities Table"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    palce_amenities = relationship("Place",
                                   secondary="place_amenity",
                                   viewonly=False)
