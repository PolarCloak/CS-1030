"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.7
Due Date: 4/8/22

Use trigonometric functions
"""
# imports
import math


# prints the top part of the table
def tableTop():
    print(f"{'Degree':<}       {'Sin':<}          {'Cos':<}")


# displays the table, I decided to separate out each line of the table to that the negative symbol
# doesn't change the layout of the table, I think it just looks cleaner
def tableLoop():
    for degree in range(0, 361, 10):
        sin = math.sin(degree)
        cos = math.cos(degree)
        # all cases are covered for sin and cos values.
        if sin >= 0 and cos >= 0:
            print(f"{degree:<12} {sin:<12.4f} {cos:<.4f}")
        elif sin < 0 and cos >= 0:
            print(f"{degree:<11} {sin:<13.4f} {cos:<.4f}")
        elif sin >= 0 and cos < 0:
            print(f"{degree:<12} {sin:<11.4f} {cos:<.4f}")
        elif sin < 0 and cos < 0:
            print(f"{degree:<11} {sin:<12.4f} {cos:<.4f}")
        # else should not be possible
        else:
            raise TypeError


# run my methods starting here
def main():
    tableTop()
    tableLoop()
    return


main()
