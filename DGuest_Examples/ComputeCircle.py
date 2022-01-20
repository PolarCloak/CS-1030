"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Determining the area of a circle.
"""

import math


def computeArea(radius):
    area = radius * radius * math.pi
    return area


def getInput():
    radius = eval(input("What is the radius of the circle? : "))
    return radius


# run my functions starting here
def main(args):
    radius = getInput()
    print(computeArea(radius))


main(0)
