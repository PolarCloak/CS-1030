"""
CS10300-20766
ID#700714467
David Guest
Assignment #3.2
Due Date: 2/25/2022

Geometry: Great circle distance
The great circle distance is the distance between two points on the surface of a sphere.
"""
import math


# calculates the distance between the two radian points.
def calculate_distance(radian1_x, radian1_y, radian2_x, radian2_y):
    radius = 6371.01
    distance = radius * math.acos(
        math.sin(radian1_x) * math.sin(radian2_x) + math.cos(radian1_x) * math.cos(radian2_x) * math.cos(
            radian1_y - radian2_y))
    return distance


# just converts a degree into a radian
def rad(degrees):
    return math.radians(degrees)


# run my methods starting here
def main(args):
    point1_x, point1_y = eval(input(f"Enter point 1 (latitude and longitude) in degrees: "))
    point2_x, point2_y = eval(input(f"Enter point 2 (latitude and longitude) in degrees: "))
    distance = calculate_distance(rad(point1_x), rad(point1_y), rad(point2_x), rad(point2_y))
    print(f"The distance between the two points is {distance} km")


main(0)
