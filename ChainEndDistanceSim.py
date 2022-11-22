"""Chain End Distance Simulator for a molecule with 1 nm bonds in Random Configuations"""
"""11/22/2022"""
__author__ = "Nick Bainbridge"
import random
import math

if __name__ == "__main__":

    for i in range(100):

        xpos = 0
        ypos = 0

        for i in range(100):
            delta = math.pi -(random.random() * 2 * math.pi)
            dx = math.cos(delta)
            dy = math.sin(delta)

            xpos += dx
            ypos += dy

        CED = (xpos**2 + ypos**2)**0.5
        print(CED)

