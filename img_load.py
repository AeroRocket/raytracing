import numpy as np
from PIL import Image

def img_to_map(name):
    img = Image.open(name)
    img_load = np.asarray(img)

    return img_load
