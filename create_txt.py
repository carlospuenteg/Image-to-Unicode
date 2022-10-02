import numpy as np
from constants.constants import UNI, EXTENDED
from utils.progress_bar import progress_bar

def create(img:np.array, UNICODE=EXTENDED) -> str:
    res = ""
    for i,line in enumerate(img):
        progress_bar(i/img.shape[0])
        for pixel in line:
            res += UNICODE[int(sum(pixel)/768*len(UNI))]
        res += "\n"
    return res