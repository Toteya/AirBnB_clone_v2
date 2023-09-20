#!/usr/bin/python3
"""
db_storage module:
Contains the DBStorage engine
"""

import os
from sqlalchemy import create_engine

class DBStorage:
    """ A database storage engine
    """

    __engine = None
    __session = None

    def __init__(self):

        user = os.environ['HBNB_MYSQL_USER']
        pwd = os.environ['HBNB_MYSQL_PWD']
        host = os.environ['HBNB_MYSQL_HOST']
        database = os.environ['HBNB_MYSQL_DB']

        connection_url = 'mysql+mysqldb://{}:{}@{}/{}'.format(user,
                                                      pwd,
                                                      host,
                                                      database)

        self.engine = create_engine(connection_url, pool_pre_ping=True)

    
