from PIL import Image
import numpy as np

from utils.files import get_path, get_valid_filename
from utils.folders import create_folders
from create_txt import create

def menu():
    create_folders(["input", "output"])
    path = get_path("input", "Image filename: ", ["jpg","png"])
    new_filename = get_valid_filename("New filename: ", ["txt"])

    image = np.array(Image.open(path))
    image_txt = create(image)

    with open(f"output/{new_filename}", "w") as f:
        f.write(image_txt)