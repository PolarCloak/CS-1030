"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.2
Due Date: 2/11/2022

Compute the volume of a cylinder
"""
import math


# the math to convert a radius to an area
def compute_area(radius):
    area = radius * radius * math.pi
    print("The area is {0}".format(area.__round__(4)))
    return area


# method to compute the volume of a cylinder
def compute_volume(radius, length):
    area = compute_area(radius)
    volume = area * length
    return volume


# run my methods starting here
def main(args):
    radius, length = eval(input("Insert values: {radius}, {length} : "))
    print("The volume is {0}.".format(compute_volume(radius, length).__round__(1)))


main(0)
