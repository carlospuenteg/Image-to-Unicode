import os

def create_folders(folders:list):
    for folder in folders:
        if not os.path.isdir(folder):
            os.mkdir(folder)