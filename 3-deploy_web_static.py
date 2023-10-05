#!/usr/bin/python3
"""
module 3-deploy_web_static
"""

from __future__ import with_statement
from fabric.api import task, runs_once
import os

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.user = 'ubuntu'
env.hosts = ['ubuntu@156061-web-01', 'ubuntu@156061-web-02']
env.key_filename = '~/.ssh/school'


@task
@runs_once
def pack():
    """
    Executes the do_pack task that archive the web_static content
    """
    return do_pack()


@task
def deploy():
    """
    Deploys static content to web servers
    """

    filepath = pack()
    if not filepath:
        return False

    return do_deploy(filepath)
