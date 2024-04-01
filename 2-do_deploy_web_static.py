#!/usr/bin/python3

"""A Fabric script to create .tgz file"""
from fabric.api import local, run, env, put
from datetime import datetime
import os
from os.path import exists

env.hosts = ['54.172.4.252', '54.175.109.84']
env.user = "ubuntu"


def do_deploy(archive_path):
    """copies an archive to remote servers"""
    if not exists(archive_path):
        return False
    filename = archive_path.split("/")[-1]
    name = filename.split(".")[0]
    path = '/data/web_static/releases/' + '{}'.format(name)
    tmp = "/tmp/" + filename

    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}/".format(path))
        run("tar -xzf {} -C {}/".format(tmp, path))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf /data/web_static_current")
        run("ln -s {}/ /data/web_static/current".format(path))
        return True
    except Exception as e:
        return False
