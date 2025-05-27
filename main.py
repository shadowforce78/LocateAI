import json
import os


def get_tree(dir, folder):
    for path, dirnames, filenames in os.walk(dir):
        folder.append((path, dirnames, filenames))

    return folder

dirtest = "O:\\"
folder = []

with open('./O.txt', "w") as f:
    f.write(json.dumps(get_tree(dirtest, folder)))