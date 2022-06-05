import numpy as np
from PIL import Image

UNI = "₩Ŵ@W#ma≠*<;:,.·˙ "
EXTENDED = [c * 2 for c in UNI]

def img_ascii(file, new_file="ascii_image.txt", ASCII=EXTENDED):
    res = ""
    img = np.array(Image.open("images/" + file))
    for line in img:
        for pixel in line:
            res += ASCII[int(sum(pixel)/768*len(UNI))]
        res += "\n"
    
    open("results/" + new_file, "w").write(res)

#img_ascii("gradient-h.jpeg", "gradient.txt")
img_ascii("happy-panda.jpeg", "happy-panda.txt")