import numpy as np
from PIL import Image

NORMAL = ("■","▤","◧","◫","□")
EXTENDED = ("■■","■▤","▤▤","▤◧","◧◧","◧◫","◫◫","◫□","□□","□-","--","- ","  ")
def img_ascii(file, new_file="ascii_image.txt", ASCII=EXTENDED):
    res = ""
    img = np.array(Image.open("images/" + file))
    for line in img:
        for pixel in line:
            for i in range(len(ASCII)):
                if min(pixel) < 255/(len(ASCII)-i):
                    res += ASCII[i]
                    break
        res += "\n"
    
    open("results/" + new_file, "w").write(res)

img_ascii("rabbit-small.jpeg")