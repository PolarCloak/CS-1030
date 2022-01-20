"""
CS10300-20766
ID#700714467
David Guest
Assignment #1.2
Due Date: 1/28/2022

This code is used to just display the same phrase 5 times in a row.
"""


# print the phrase given 5 times
def printFiveTimes(phrase):
    # for loop to run the code 5 times
    for i in range(0, 5, 1):
        print(phrase)


# run my functions starting here
def main(args):
    printFiveTimes("Welcome to Python")


main(0)
