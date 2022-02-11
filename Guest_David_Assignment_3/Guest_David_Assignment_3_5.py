"""
CS10300-20766
ID#700714467
David Guest
Assignment #3.5
Due Date: 2/25/2022

Geometry: Area of a regular polygon
"""
import math


# calculates the area of a regular polygon using number of sides and the sides length
def calculate_area(num_sides, side_length):
    area = (num_sides * (side_length ** 2)) / (4 * (math.tan(math.pi / num_sides)))
    return area


# run my methods starting here
def main(args):
    num_sides = eval(input(f"Enter the number of sides: "))
    side_length = eval(input(f"Enter the side length: "))
    area = calculate_area(num_sides, side_length)
    print(f"The area of the polygon is {area}")


main(0)
