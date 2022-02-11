"""
CS10300-20766
ID#700714467
David Guest
Assignment #3.4
Due Date: 2/25/2022

Geometry: Area of a pentagon
"""
import math


# calculates the area of a pentagon using the length of a side
def calculate_pentagon(side_length):
    area = (5 * (side_length ** 2)) / (4 * (math.tan(math.pi / 5)))
    return area


# run my methods starting here
def main(args):
    side_in = eval(input(f"Enter the side: "))
    area = calculate_pentagon(side_in)
    print(f"The area of the pentagon is {area}")


main(0)
