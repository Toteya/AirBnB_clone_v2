#!/usr/bin/python3
"""
module 1-pack_web_static
"""
from fabric.api import local, settings
from datetime import datetime
import os


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

    file_path = "versions/web_static_{}.tgz".format(timestamp)
    source_path = "web_static"

    if not os.path.exists(source_path):
        return None

    dir_size = get_dir_size(source_path)

    print("Packing {} to {}".format(source_path, file_path))
    local('tar -cvzf {} web_static'.format(file_path))
    print("{} packed: {} -> {}Bytes".format(source_path, file_path, dir_size))
    return file_path


def get_dir_size(path):
    """
    Get total size in bytes of a directory
    """
    size = 0
    with os.scandir(path) as iterator:
        for item in iterator:
            if item.is_file():
                size += item.stat().st_size
            elif item.is_dir():
                size += get_dir_size(item.path)
    return size
