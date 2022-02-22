"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

This is a low level math quiz testing on subtraction only. Customizable number of questions in the quiz.
"""
import random

questionCount = 10


def question():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    while a == b:
        b = random.randint(0, 9)
    if a < b:
        a, b = b, a

    print(f"A: {a} , B: {b}")

    answer = eval(input("What is A - B? : \n"))
    print(f"Subtraction:  {a} - {b} = {a - b}")
    if answer == a - b:
        print(f"You are correct!\n")
        return True
    else:
        print(f"Incorrect! Better luck next time...\n")
        return False


def quiz():
    results = []
    for x in range(questionCount):
        results.append(question())
    print(f"Your results are in...")
    print(f"Correct:{results.count(True)} , Wrong:{results.count(False)} ")
    print(f"Your grade:{(results.count(True) / len(results)) * 100}%")


quiz()
