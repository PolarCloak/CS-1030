"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Simultanious Assignment Demo
"""

import math


def compute(values):
    total = 0;
    for val in values:
        total += val
    area = total / 3
    return area


def getInput():
    x, y, z = eval(input("Enter three values seperated by commas : "))
    values = {x, y, z}
    return values


# run my functions starting here
def main(args):
    values = getInput()
    print(compute(values))


main(0)
