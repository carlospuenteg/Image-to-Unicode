from colorama import Fore, init; init()
import os

from utils.ctxt import ctxt

def check_path(path:str) -> bool:
    return os.path.isfile(path)

def get_valid_filename(msg:str, exts:list) -> str:
    while True:
        filename = input(msg)
        if "." in filename:
            if filename.split(".")[-1] in exts:
                return filename
            else:
                print(ctxt("Invalid extension", Fore.RED))
        else:
            return f"{filename}.{exts[0]}"

def get_path(folder_path:str, msg:str, exts:list) -> str:
    while True:
        filename = input(msg)
        if "." in filename:
            path = f"{folder_path}/{filename}"
            if check_path(path):
                return filename
            else:
                print(ctxt("Invalid extension", Fore.RED))
        else:
            for ext in exts:
                path = f"{folder_path}/{filename}.{ext}"
                if check_path(path):
                    return path
            print(ctxt("File not found", Fore.RED))