from light import Light
from sphere import Sphere
from size import size
import numpy as np
from random import randint
from math import sqrt


def img_render():
    picture = np.full(size, (0,0,0))
    main_light = Light(500, 500, 0)
    for i in range(15):
        color = (randint(0,256), randint(0,256), randint(0,256))
        sphere = Sphere(randint(0,size[0]), randint(0,size[0]), color, randint(0,200))

        for x in range(size[0]):
            for y in range(size[0]):
                if (sphere.x-x)**2 + (sphere.y-y)**2 <= sphere.radius**2:
                    z = sqrt(x**2 + y**2)
                    cos = x / z

                    current_color_list = list(sphere.color)
                    new_color_list = []

                    for i in range(3):
                        new_color_list.append(current_color_list[i]*cos)

                    picture[x][y] = (new_color_list[0], new_color_list[1], new_color_list[2])
            
    return picture