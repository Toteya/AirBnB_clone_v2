#!/usr/bin/python3
"""
module db_storage
Database storage engine
"""
import models
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from urllib.parse import quote


class DBStorage:
    """A database storage engine class"""

    __engine = None
    __session = None
    Session = None

    def __init__(self):
        user = os.environ.get('HBNB_MYSQL_USER')
        password = quote(os.environ.get('HBNB_MYSQL_PWD'))
        database = os.environ.get('HBNB_MYSQL_DB')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db_url = 'mysql+mysqldb://%s:%s@%s/%s' % (user,
                                                  password,
                                                  host,
                                                  database)
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return an dictionary of object from the database of the given
        class. If class is None, returns all a dictionary of all objects
        """
        import models
        classes = {
                'User': models.user.User,
                'State': models.state.State,
                'City': models.city.City,
                # 'Amenity': Amenity,
                'Place': models.place.Place,
                # 'Review': Review
            }
        obj_list = []
        if cls:
            result = self.__session.query(cls).all()
            obj_list.extend(result)
        else:
            for clss in classes:
                result = self.__session.query(classes[clss]).all()
                obj_list.extend(result)

        obj_dict = {}
        for obj in obj_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict.update({key: obj})

        return obj_dict

    def new(self, obj):
        """Adds the given object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commits/saves all changes to the current db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the object from the current db session
        """
        self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database
        """
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.user import User
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """Closes the current session"""
        self.__session.remove()
