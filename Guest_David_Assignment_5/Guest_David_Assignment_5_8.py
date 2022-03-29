"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.8
Due Date: 4/8/22

Use the math.sqrt function
"""
import math


# prints the top part of the table
def tableTop():
    print(f"{'Number':<}       {'Square Root':<}")


# displays the table, only the evens.
def tableLoop():
    for number in range(0, 21, 2):
        print(f"{number:<12} {math.sqrt(number):<.4f}")


# run my methods starting here
def main():
    tableTop()
    tableLoop()
    return


main()
