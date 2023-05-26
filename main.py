import matplotlib.pyplot as plt
from PIL import Image

from light import Light
from sphere import Sphere
from size import size
from img_gen import img_render
from img_mod import img_regen
from img_load import img_to_map
from img_finder import img_import

if __name__ == "__main__":
    cat = img_to_map(img_import("cat.png"))
    new_picture = img_regen(cat)

    plt.imshow(new_picture)
    plt.show()