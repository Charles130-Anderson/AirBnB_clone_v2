#!/usr/bin/env python3
"""A module for Fabric script that generates a .tgz archive."""

import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Making an archive on web_static folder.
    """
    local('sudo mkdir -p versions')

    time = datetime.now()
    time_string = time.strftime('%Y%m%d%H%M%S')

    output_path = 'versions/web_static_{}.tgz'.format(time_string)

    try:
        print("Packing web_static to {}".format(output_path))
        local('tar -cvzf {} web_static'.format(output_path))
        file_size = os.path.getsize(output_path)
        print("web_static packed: {} -> {} Bytes".format(output_path, file_size))
        return output_path
    except Exception as e:
        print("Error occurred during packing: {}".format(str(e)))
        return None
