#!/usr/bin/python3
"""
module 1-pack_web_static
"""
from __future__ import with_statement
from fabric.api import env, put, run, sudo
from datetime import datetime
import os


env.user = 'ubuntu'
env.hosts = ['ubuntu@156061-web-01', 'ubuntu@156061-web-02']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path=None):
    """
    Deploys an archive to a web server
    """

    if not os.path.exists(archive_path):
        return False

    filename = archive_path.split('/')[-1]
    filename = filename.split('.')[0]
    dest_dir = '/data/web_static/releases/{}'.format(filename)

    put(archive_path, '/tmp/')
    sudo('mkdir -p {}'.format(dest_dir))
    sudo('tar -xzf /tmp/{}.tgz -C {}'.format(filename, dest_dir))
    sudo('rm -rf /tmp/{}'.format(filename))
    sudo('ln -s {} /data/web_static/current'.format(dest_dir))
    print('New version deployed!')
    return True
