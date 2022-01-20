"""
CS10300-20766
ID#700714467
David Guest
Assignment #1.8
Due Date: 1/28/2022

Area and perimeter of a circle
"""
# using math for pi
import math


# gets the area of a circle based on the radius
def area(circleRadius):
    circleArea = circleRadius * circleRadius * math.pi
    return circleArea


# gets the perimeter of a circle based on the radius
def perimeter(circleRadius):
    circlePerimeter = 2 * circleRadius * math.pi
    return circlePerimeter


# run my functions starting here
def main(args):
    radius = 5.5
    print("Circle of radius {0} has an area of {1} and a perimeter of {2}".format(radius, area(radius).__round__(2),
                                                                                  perimeter(radius).__round__(2)))


main(0)
