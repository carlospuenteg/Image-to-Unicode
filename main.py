 
import numpy as np
from PIL import Image

def img_ascii(file, new_file="ascii_image.txt"):
    res = ""
    img = np.array(Image.open("images/" + file))
    for line in img:
        for pixel in line:
            if sum(pixel) < 765/5:
                res += "■"
            elif sum(pixel) < 765/4:
                res += "▤"
            elif sum(pixel) < 765/3:
                res += "◧"
            elif sum(pixel) < 765/2:
                res += "◫"
            else:
                res += "□"
        res += "\n"
    
    f = open("results/" + new_file, "w")
    f.write(res)
    f.close()

img_ascii("rabbit.jpeg")