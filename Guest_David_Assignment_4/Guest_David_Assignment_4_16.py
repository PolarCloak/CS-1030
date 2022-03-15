"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.16
Due Date: 4/25/22

Random Character
"""
import random


# uses time.time() to get a random number that ends up between 65-90
def get_random_value():
    value = random.randrange(65, 91, 1)
    return value


# run my methods starting here
def main(args):
    random_char = chr(get_random_value())
    print(f"Your random character is {random_char}")


main(0)
