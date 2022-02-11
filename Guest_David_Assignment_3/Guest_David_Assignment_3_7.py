"""
CS10300-20766
ID#700714467
David Guest
Assignment #3.7
Due Date: 2/25/2022

Random Character (Using time)
"""
import time


# Simply converts the asci value provided into a character
def asci_to_char(asci_value):
    return chr(asci_value)


# uses time.time() to get a random number that ends up between 65-90
def get_random_value():
    l_value = time.time() * 100
    capped_val = l_value % 26
    return int(capped_val + 65)


# run my methods starting here
def main(args):
    random_char = asci_to_char(get_random_value())
    print(f"Your random character is {random_char}")


main(0)
