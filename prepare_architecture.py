import os
from datetime import datetime


def prepare_architecture():
    temp_folder_id = datetime.now().strftime("%d%m%Y%H%M%S")
    path = f"temp_{temp_folder_id}"

    try:
        os.mkdir(path)
    except OSError as e:
        print("Creation of the directory %s failed" % path)
        return False
    else:
        print("Successfully created the directory %s " % path)
        return True
