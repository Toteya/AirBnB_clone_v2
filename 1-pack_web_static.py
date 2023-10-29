#!/usr/bin/python3
"""
module 1-pack_web_static
"""
from fabric.api import local, settings, task, runs_once
from datetime import datetime, date
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    folder
    """
    dt = datetime.now()
    # dt = datetime(2017, 3, 14, 23, 33, 57)
    
    to_str = lambda x: str(x) if x >= 10 else f'0{x}'
    timestamp = "".join([str(dt.year),
                         to_str(dt.month),
                         to_str(dt.day),
                         to_str(dt.hour),
                         to_str(dt.minute),
                         to_str(dt.second)])

    dir_path = "versions/"
    file_path = "versions/web_static_{}.tgz".format(timestamp)
    source_path = "web_static"

    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

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
