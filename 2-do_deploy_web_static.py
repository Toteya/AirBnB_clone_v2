#!/usr/bin/python3
"""
module 2-do_deploy_web_static
"""
from __future__ import with_statement
from fabric.api import env, put, settings, sudo
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

    results = []
    with settings(warn_only=True):
        results.append(put(archive_path, '/tmp/'))
        results.append(sudo('mkdir -p {}'.format(dest_dir)))
        results.append(sudo('tar -xzf /tmp/{}.tgz -C {}'.format(filename,
                                                                dest_dir)))
        results.append(sudo('cp -r {}/web_static/* {}'.format(dest_dir,
                                                              dest_dir)))
        results.append(sudo('rm -rf {}/web_static/'))
        results.append(sudo('rm -rf /tmp/{}'.format(filename)))
        results.append(sudo('rm -rf /data/web_static/current'))
        results.append(sudo(f'ln -s {dest_dir} /data/web_static/current'))
    if any(result.failed for result in results):
        return False
    print('New version deployed!')
    return True
