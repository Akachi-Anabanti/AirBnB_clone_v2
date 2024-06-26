#!/usr/bin/python3
"""DB storage module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """initialization method"""
        HBNB_MYSQL_USER = os.environ.get("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = os.environ.get("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = os.environ.get("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = os.environ.get("HBNB_MYSQL_DB")

        connection_string = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB)
        self.__engine = create_engine(connection_string, pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current database session
        for all objects depending on name argument
        cls"""

        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())

        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj
                for obj in objs}

    def new(self, obj):
        """Adds object to the current db
        session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all chagnes of the current sessin"""
        self.__session.commit()

    def delete(self, obj):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the Database
        """
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.Session = scoped_session(session_factory)
        self.__session = self.Session()

    def close(self):
        """calls remove method on the private session
        attribute"""
        self.Session.close()
