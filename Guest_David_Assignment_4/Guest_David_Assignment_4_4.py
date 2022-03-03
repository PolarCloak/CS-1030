"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.4
Due Date: 4/25/22

Game: Learn addition
"""
import random

MAX = 100
MIN = 1


# run my methods starting here
def main(args):
    # get 2 random numbers
    digits = random.randrange(MIN, MAX, 1), random.randrange(MIN, MAX, 1)
    print(f"The random numbers are: {digits[0]}, {digits[1]}\n")
    # take the users' guess
    guess = eval(input(f"What is the sum of these numbers?: "))
    # get the actual total
    total = digits[0] + digits[1]
    # correct value
    if guess == total:
        print(f"You are correct! The answer was {total}.")
        return True
    # incorrect value
    else:
        print(f"Incorrect. The answer is {total}.")
        return False


main(0)
