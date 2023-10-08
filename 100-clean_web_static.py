#!/usr/bin/python3
"""
module 2-do_deploy_web_static
"""
from __future__ import with_statement
from fabric.api import env, local, run, sudo, task, runs_once
from fabric.contrib import files
import os
import re

env.user = 'ubuntu'
env.hosts = ['ubuntu@156061-web-01', 'ubuntu@156061-web-02']
env.key_filename = '~/.ssh/school'


@task
def do_clean(number=0):
    """
    Cleans up outdated archives
    """
    number = int(number)

    if number < 2:
        number = 1

    clean_up_versions(number)
    clean_up_releases(number)


@task
@runs_once
def clean_up_versions(number):
    """
    Cleans up the versions directory on the local machine
    """
    dir_path = 'versions'
    clean_up(dir_path, number, 'local')


@task
def clean_up_releases(number):
    """
    Cleans up the releases directory on the webservers
    """
    dir_path = '/data/web_static/releases'
    clean_up(dir_path, number, 'remote')


def clean_up(dir_path, number, server):
    """
    Cleans up the scecified directory
    """

    archives = []

    if server == 'local':
        pattern = '^web_static_[0-9]{14}.tgz$'
        entries = os.scandir(dir_path)
        for entry in entries:
            if re.match(pattern, entry.name):
                archives.append(entry.name)
    elif server == 'remote':
        pattern = '^web_static_[0-9]{14}$'
        filelist = sudo('ls {}'.format(dir_path))
        entries = filelist.split()
        for entry in entries:
            if re.match(pattern, entry):
                archives.append(entry)

    archives = sorted(archives, reverse=True)[number:]
    for item in archives:
        item_path = '{}/{}'.format(dir_path, item)
        if server == 'local':
            local('rm {}'.format(item_path))
        elif server == 'remote':
            sudo('rm -rf {}'.format(item_path))
