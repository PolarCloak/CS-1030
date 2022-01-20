"""
CS10300-20766
ID#700714467
David Guest
Assignment #1.4
Due Date: 1/28/2022

Main purpose of this is to display a table of values and their corresponding square and cube.
"""


# prints the value, squared, and cubed of the given value.
def printPowers(value):
    print("{0}\t\t{1}\t\t{2}".format(value, value ** 2, value ** 3))


# display the top row a - a^3, top of the table.
def displayTopRow():
    print("a\t\ta^2\t\ta^3")


# run my functions starting here
def main(args):
    displayTopRow()
    for i in range(1, 5, 1):
        printPowers(i)


main(0)
