import os
from datetime import datetime


def prepare_architecture():
    temp_folder_id = datetime.now().strftime("%d%m%Y%H%M%S")
    path = f"temp_{temp_folder_id}"
    try:
        os.mkdir(path)
        try:
            os.mkdir(path+"/slides")
            os.mkdir(path + "/files")
        except OSError as e:
            #print("Creation of the directory %s failed" % path)
            return False, ""
        else:
            #print("Successfully created the directories in %s " % path)
            return True, path
    except OSError as e:
        #print("Creation of the directory %s failed" % path)
        return False, ""
