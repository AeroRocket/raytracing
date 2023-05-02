import matplotlib.pyplot as plt

figure, axes = plt.subplots()

class Sphere:
    def __init__(self, x, y , color, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        Draw_circle= plt.Circle((self.x, self.y),self.radius , color=self.color)
        axes.add_artist(Draw_circle)