"""
CS10300-20766
ID#700714467
David Guest
Assignment #6.36
Due Date: 4/22/22

Generate random characters
"""
# imports
import random as r


# returns a random capital character from ascii
def get_random_char():
    value = r.randrange(65, 91, 1)
    return chr(value)


# returns a random digit
def get_random_digit():
    return r.randint(0, 9)


# follows the requirements in the textbook for printing 100 chars and then 100 digits
def print_char_then_digit():
    for x in range(10):
        print()
        for y in range(10):
            print(f"{get_random_char()} ", end="")
    for x in range(10):
        print()
        for y in range(10):
            print(f"{get_random_digit()} ", end="")
    return


# run my methods starting here
def main():
    print_char_then_digit()
    return


main()
