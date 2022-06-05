import numpy as np
from PIL import Image

#------------------------------------------------------------------------------
# Progress bar
GREEN = '\u001b[32m'
MAGENTA = '\u001b[35m'
RESET = '\u001b[0m'

def progress_bar(percent, text="", bar_len=30):
    SYMBOL = "━"
    done = round(percent*bar_len)
    left = bar_len - done

    print(f"   {GREEN}{SYMBOL*done}{RESET}{SYMBOL*left} {f'[{round(percent*100,2)}%]'.ljust(8)} {MAGENTA}{text}{RESET}", end='\r')

    if percent == 1: print("✅")

#------------------------------------------------------------------------------
# Image creator

UNI = "₩Ŵ@W#ma≠*<;:,.·˙ "
EXTENDED = [c * 2 for c in UNI]

def create(file, new_file=None, ASCII=EXTENDED):
    res = ""
    img = np.array(Image.open("images/" + file))
    for i,line in enumerate(img):
        progress_bar(i/img.shape[0])
        for pixel in line:
            res += ASCII[int(sum(pixel)/768*len(UNI))]
        res += "\n"
    
    fileName = new_file if new_file else file.split(".")[0]
    open(f"results/{fileName}", "w").write(res)

#------------------------------------------------------------------------------

create("elephant-hd.jpg", "elephant.txt")