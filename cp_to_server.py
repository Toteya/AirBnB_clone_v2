#!/usr/bin/python3
"""
module 1-pack_web_static
"""
from __future__ import with_statement
from fabric.api import env, local, put, settings, sudo
import os


env.user = 'ubuntu'
env.hosts = ['156061-web-02']
env.key_filename = '~/.ssh/school'
#env.disable_known_hosts = True

def copy(file_path=None):
    """
    Copies a file to a server
    """
    
    # if not os.path.exists(file_path):
    #    print("{} Path not found!".format(file_path))
    #    return False
    
    results = []
    with settings(warn_only=True):
        results.append(put(file_path, '/tmp/'))
    if any(result.failed for result in results):
        print("It Failed BRA!")
        return False
    else:
        print('Copied successfully!')
