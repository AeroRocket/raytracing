import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from math import pi
import random
import math

figure, axes = plt.subplots()
size = (1000,1000,3)
size_int = 1000

class Sphere:
    def __init__(self, x, y , color, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        Draw_circle= plt.Circle((self.x, self.y ),self.radius , color=self.color)
        axes.add_artist(Draw_circle)


class Light:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


def img_render():
    picture = np.full(size, (0,0,0))
    main_light = Light(500,500, 0)
    for i in range(15):
        color = (random.randint(0,256), random.randint(0,256), random.randint(0,256))
        sphere = Sphere(random.randint(0,size_int), random.randint(0,size_int), color, random.randint(0,200))

        for x in range(size_int):
            for y in range(size_int):
                if (sphere.x-x)**2 + (sphere.y-y)**2 <= sphere.radius**2:
                    z = math.sqrt(x**2 + y**2)
                    cos = x / z

                    current_color_list = list(sphere.color)
                    new_color_list = []

                    for i in range(3):
                        new_color_list.append(current_color_list[i]*cos)

                    picture[x][y] = (new_color_list[0], new_color_list[1], new_color_list[2])
            
    return picture
img2 = img_render()
plt.imshow(img2)
plt.show()
