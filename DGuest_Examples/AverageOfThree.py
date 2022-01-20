"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Average of 3 numbers
"""

import math


def computeAverage(val1, val2, val3):
    total = val1 + val2 + val3
    average = total / 3
    return average


def getInput():
    value = eval(input("Insert a value : "))
    return value


# run my functions starting here
def main(args):
    val1 = getInput()
    val2 = getInput()
    val3 = getInput()
    print(computeAverage(val1, val2, val3).__round__(2))


main(0)
