"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.17
Due Date: 4/25/22

Rock, Paper, Scissors
"""
import random
import time


# converts a text value of rock, paper, or scissors to its corresponding integer
def textToInteger(text):
    if text == "rock" or text == "r":
        return 0
    elif text == "paper" or text == "p":
        return 1
    elif text == "scissors" or text == "s":
        return 2
    else:
        raise ValueError


# converts an integer to its corresponding rock, paper, or scissors
def integerToText(integer):
    if integer == 0:
        return "Rock"
    elif integer == 1:
        return "Paper"
    elif integer == 2:
        return "Scissors"
    else:
        raise ValueError


# run my methods starting here
def main(args):
    rawGuess = input(f"Rock, Paper, Scissors: Make your choice (R/P/S): ")
    guess = rawGuess.lower()
    guessInt = textToInteger(guess)
    print(f"You threw {integerToText(guessInt)}.")
    time.sleep(0.5)
    botInt = random.randrange(0, 2, 1)
    print(f"The bot threw {integerToText(botInt)}.\n")
    time.sleep(0.5)
    # all winning conditions
    if (guessInt == 0 and botInt == 2) or (guessInt == 1 and botInt == 0) or (guessInt == 2 and botInt == 1):
        print(f"You threw {integerToText(guessInt)} which beats the bots {integerToText(botInt)}!")
        time.sleep(2)
        print(f"Congrats!")
        return 1
    # all losing conditions
    elif (guessInt == 0 and botInt == 1) or (guessInt == 1 and botInt == 2) or (guessInt == 2 and botInt == 0):
        print(f"The bot threw {integerToText(botInt)} which beats your {integerToText(guessInt)}.")
        time.sleep(2)
        print(f"Unlucky.")
        return -1
    # all other conditions would be a draw.
    else:
        print(f"You and the bot both threw {integerToText(guessInt)}.")
        time.sleep(2)
        print(f"Draw.")
        return 0


main(0)
