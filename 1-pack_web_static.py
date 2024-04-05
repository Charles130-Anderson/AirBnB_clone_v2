#!/usr/bin/python3
"""A module designed for a Fabric script aimed at creating a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    date_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date_time.year,
        date_time.month,
        date_time.day,
        date_time.hour,
        date_time.minute,
        date_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output
