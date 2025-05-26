import os

dir = "N:\\Download\\parcoursup"

try:
    with os.scandir(dir) as dir:
        for i in dir:
            if i.is_dir():
                with os.scandir(i) as dir2:
                    for j in dir2:
                        print(j.name)
except PermissionError:
    print('Pas de permissions')