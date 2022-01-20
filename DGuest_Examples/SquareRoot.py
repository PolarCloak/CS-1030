"""
David Guest
ID#700714467

"""

import cmath


def getSqrt(float_):
    numSqrt = cmath.sqrt(float_)
    return numSqrt


def main(args):
    num = eval(input("Please input a value: "))
    sqrt = getSqrt(num)
    print("The square root of {0} is {1}".format(num, sqrt))
    return sqrt;


main(0)

