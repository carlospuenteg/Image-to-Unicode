import numpy as np
from PIL import Image

UNI = "_,.ˉ˙ "
EXTENDED = [c * 2 for c in UNI]

def img_ascii(file, new_file="ascii_image.txt", ASCII=EXTENDED):
    res = ""
    img = np.array(Image.open("images/" + file))
    for line in img:
        for pixel in line:
            res += ASCII[int(sum(pixel)/768*4)]
        res += "\n"
    
    open("results/" + new_file, "w").write(res)

img_ascii("rabbit.jpeg", "rabbit.txt")