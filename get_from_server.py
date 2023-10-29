#!/usr/bin/python3
"""
module 1-pack_web_static
"""
from __future__ import with_statement
from fabric.api import env, local, get, settings, sudo
import os


env.user = 'ubuntu'
env.hosts = ['156061-lb-01']
env.key_filename = '~/.ssh/school'
#env.disable_known_hosts = True

def download(remote_path=None):
    """
    Downloaf a file(s) from a server
    """
    
    dest_dir = "/home/toteya/{}_downloads".format(env.hosts[0])
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    #    print("{} Path not found!".format(file_path))
    #    return False
    
    with settings(warn_only=True):
        result = get(remote_path, dest_dir)
    if result.failed:
        print("Operation failed!")
        return False
    else:
        print('Downloaded successfully!')
