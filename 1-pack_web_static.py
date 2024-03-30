#!/usr/bin/python3

"""A Fabric script to create .tgz file"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generate a .tgz archive from
    the contents of the web_static"""
    dt = datetime.now()
    file_name = 'web_static_{}{}{}{}{}{}.tgz'.format(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        local("tar -cvzf versions/{} web_static".format(
            file_name))
        return os.path.join("versions", file_name)
    except Exception as e:
        return None
