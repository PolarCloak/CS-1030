"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.6
Due Date: 2/11/2022

Sum the digits in an integer
"""


# Takes a user-defined int and runs through each digit, adding to a sum. returns the sum.
def convert_and_add(user_input):
    # initialize values used in loop
    sum_of_digits = 0
    value1 = user_input
    # while the value still has at least 2 or more digits
    while (value1 // 10) > 0:
        sum_of_digits += value1 % 10
        value1 = value1 // 10
    # add the last digit to the sum
    sum_of_digits += value1
    return sum_of_digits


# run my methods starting here
def main(args):
    user_input = eval(input("Enter any integer (should work well past 1000): "))
    print("The sum of the digits is {0}".format(convert_and_add(user_input)))


main(0)
