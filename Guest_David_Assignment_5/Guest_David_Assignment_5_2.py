"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.2
Due Date: 4/8/22

Repeat additions
"""
# imports
import random
import time

# variables used to modify the quiz
QUESTION_COUNT = 5
MINIMUM = 1
MAXIMUM = 15


# variables where answer results are stored
correct = 0


# this is the quiz function that runs {question} number of times using max and min
def quiz(questions, minimum, maximum):
    global correct
    for q in range(1, questions + 1, 1):
        print(f"Question {q}:")
        int1 = random.randrange(minimum, maximum, 1)
        int2 = random.randrange(minimum, maximum, 1)
        guess = eval(input(f"What is the sum: {int1} + {int2} ?\n"))
        answer = int1 + int2
        # correct answer
        if guess == answer:
            correct += 1
            print(f"\nCorrect!\n")
        else:
            print(f"\nWrong...\n")


# displays the results of your quiz
def displayResults(timeTaken):
    print(f"Your quiz took {timeTaken:.2f} seconds.")
    print(f"You were able to answer {correct} / {QUESTION_COUNT} correctly\n")
    percent = correct / QUESTION_COUNT
    print(f"Your total grade is: {percent:.2%}")


# run my methods starting here
def main():
    startTime = time.time()
    quiz(QUESTION_COUNT, MINIMUM, MAXIMUM)
    endTime = time.time()
    timeTaken = endTime - startTime
    displayResults(timeTaken)
    return


main()
