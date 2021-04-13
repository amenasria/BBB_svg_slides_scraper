import os
import shutil

# Source : https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder


def wipe_dir_content(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            #print('Failed to delete %s. Reason: %s' % (file_path, e))
            print("")
