"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.14
Due Date: 4/25/22

Game: heads or tails
"""
import random
import time


# converts a text value of heads or tails to its corresponding integer
def sideToInteger(text):
    if text == "heads" or text == "h":
        return 0
    elif text == "tails" or text == "t":
        return 1
    else:
        raise ValueError


# converts an integer to its corresponding heads or tails
def integerToSide(integer):
    if integer == 0:
        return "Heads"
    elif integer == 1:
        return "Tails"
    else:
        raise ValueError


# run my methods starting here
def main(args):
    rawGuess = input(f"Coin Flip: guess heads or tails (H/T): ")
    guess = rawGuess.lower()
    guessInt = sideToInteger(guess)
    print(f"You guessed {integerToSide(guessInt)}.")
    time.sleep(0.5)
    print(f"Flipping the coin...\n")
    time.sleep(0.5)
    flip = random.randrange(0, 1, 1)
    print(f"It was {integerToSide(flip)}.\n")
    time.sleep(0.5)
    if guessInt == flip:
        print(f"You guessed correctly!")
        return 1
    else:
        print(f"You guessed incorrectly, unlucky.")
        return 0


main(0)
