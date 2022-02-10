"""
CS10300-20766
ID#700714467
David Guest
Assignment #3.1
Due Date: 2/25/2022

Geometry: Area of a Pentagon
"""
import math


# determines the area of a pentagon by using the length of a side
def get_area(length_of_side):
    area = (3 * math.sqrt(3)) / 2 * length_of_side ** 2
    return area


# determines the length of the side of a pentagon by using the length from the center
def get_side(length_from_center):
    side = (2 * length_from_center) * math.sin(math.pi / 5)
    return side


# run my methods starting here
def main(args):
    length_in = eval(input(f"Please input a value for the length from the center of the pentagon: "))
    result = get_area(get_side(length_in))
    print(f"The area of the pentagon is {result:.2f}")


main(0)
