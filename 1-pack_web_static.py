#!/usr/bin/python3
"""
module 1-pack_web_static
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    folder
    """
    time = datetime.now()
    timestamp = "".join([str(time.year),
                         str(time.month),
                         str(time.day),
                         str(time.hour),
                         str(time.minute),
                         str(time.second)])
    # print(timestamp)
    filename = "web_static_{}.tgz".format(timestamp)
    local('tar -cvzf {} ./web_static'.format(filename))
