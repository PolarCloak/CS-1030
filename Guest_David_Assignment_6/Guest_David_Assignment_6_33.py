"""
CS10300-20766
ID#700714467
David Guest
Assignment #6.33
Due Date: 4/22/22

Geometry: area of a pentagon

already did this in 3.4, nothing really to change as we already used methods
"""
# imports
import math


# calculates the area of a pentagon using the length of a side
def area(s):
    area_ = (5 * (s ** 2)) / (4 * (math.tan(math.pi / 5)))
    return area_


# run my methods starting here
def main():
    side_in = eval(input(f"Enter the length of a side: "))
    pentagon_area = area(side_in)
    print(f"The area of the pentagon with side length {side_in} is {pentagon_area}")


main()
