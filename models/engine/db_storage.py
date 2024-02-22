#!/usr/bin/python3
"""DB storage module"""
from sqlalchemy import create_engine
import os

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """initialization method"""
        HBNB_MYSQL_USER =  os.environ.get("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = os.environ.get("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST =  os.environ.get("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = os.environ.get("HBNB_MYSQL_DB")

        connection_string = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB)
        self.__engine = create_engine(connection_string, pool_pre_ping=True)

    def all(self, cls=None):
        """Query current database session
        for all objects depending on name argument
        cls"""

        if cls is not None:
            pass
        pass
    
    def new(self, obj):
        """Adds object to the current db
        session
        """
        pass

    def save(self):
        """Commit all chagnes of the current sessin"""
        pass

    def delete(self, obj):
        """Delete obj from the current database session"""
        pass

    def reload(self):
        """
        create all tables in the Database
        """
        pass

