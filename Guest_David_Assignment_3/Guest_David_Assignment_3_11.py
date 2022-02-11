"""
CS10300-20766
ID#700714467
David Guest
Assignment #3.11
Due Date: 2/25/2022

Reverse Number
"""


# Takes a user-defined int (anything works) and runs through each digit, reversing its order
def reverse(user_input):
    # initialize values used in loop
    output = ""
    chars = [*user_input]
    # while the value still has at least 2 or more digits
    for i in range(len(chars) - 1, -1, -1):
        output += chars[i]
    # add the last digit to the sum
    return output


# run my methods starting here
def main(args):
    user_input = input(f"Enter a value to reverse: ")
    reversed_input = reverse(user_input)
    print(f"The reverse is: '{reversed_input}'")


main(0)
