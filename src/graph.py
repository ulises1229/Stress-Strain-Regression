import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import random
x = Symbol('x')

class Graph:
    def __init__(self):
        self.x = 1

    def addScatter(self, x, y, color):
        plt.scatter(x, y, color = color, alpha = 0.8, label = "Original points")

    def addLineFunction(self, f, minX, maxX):
        color = ['b', 'g', 'r', 'c', 'm', 'y', 'black', 'gold', 'royalblue','lightblue']
        X = np.linspace(minX, maxX, 50)
        Y = [None] * len(X)

        for i in range(0, len(X)):
            if str(f).isdigit():
                Y[i] = f
            else:
                Y[i] = f.evalf(subs = {x: X[i]})
                # Add plot
                plt.plot(X, Y, color[random.randint(0,9)] , label = str(f))

    def displayPlot(self, title, xAxis, yAxis):
        plt.title(title)
        plt.xlabel(xAxis)
        plt.ylabel(yAxis)
        plt.show()
