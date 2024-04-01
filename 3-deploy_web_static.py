#!/usr/bin/python3
"""A Fabric script to create .tgz file"""
from fabric.api import local, run, env, put
from datetime import datetime
import os
from os.path import exists


def do_pack():
    """Generate a .tgz archive from
    the contents of the web_static"""
    dt = datetime.now()
    file_name = 'web_static_{}{}{}{}{}{}.tgz'.format(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        local("tar -cvzf versions/{} ./web_static".format(
            file_name))
        return os.path.join("versions", file_name)
    except Exception as e:
        return None


env.hosts = ['54.172.4.252', '54.175.109.84']


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
        run("sudo mkdir -p {}/".format(path))
        run("sudo tar -xzf {} -C {}/".format(tmp, path))
        run("rm {}".format(tmp))
        run("sudo mv {}/web_static/* {}/".format(path, path))
        run("rm -rf /data/web_static_current")
        run("sudo ln -s {}/ /data/web_static/current".format(path))
        return True
    except Exception as e:
        return False


def deploy():
    """excutes do_deploy and do_pack"""
    archive_path = do_pack()
    if exists(archive_path) is False:
        return False
    res = do_deploy(archive_path)
    return res
