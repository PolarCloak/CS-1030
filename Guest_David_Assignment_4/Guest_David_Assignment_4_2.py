"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.2
Due Date: 4/25/22

Game: add three numbers
"""
import random

MAX = 10
MIN = 1


# run my methods starting here
def main(args):
    digits = random.randrange(MIN, MAX, 1), random.randrange(MIN, MAX, 1), random.randrange(MIN, MAX, 1)
    print(f"The random numbers are: {digits[0]}, {digits[1]}, {digits[2]}\n")
    guess = eval(input(f"What is the sum of these numbers?: "))
    total = digits[0] + digits[1] + digits[2]
    if guess == total:
        print(f"You are correct! The answer was {total}.")
    else:
        print(f"Incorrect. The answer is {total}.")
    return


main(0)
