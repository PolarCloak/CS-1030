"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Display Hours minutes and seconds, from seconds.
"""


def calc(seconds):
    minutes = seconds // 60
    secondsRemaining = seconds % 60

    hours = minutes // 60
    minutesRemaining = minutes % 60

    days = hours // 24
    hoursRemaining = hours % 24

    years = days // 365
    daysRemaining = days % 365


    print("That is {4} years, {0} days, {1} hours, {2} minutes, and {3} seconds".format(
        daysRemaining, hoursRemaining, minutesRemaining, secondsRemaining, years
    ))


def getInput():
    return eval(input("Enter and integer for seconds : "))

# run my functions starting here
def main(args):
    calc(getInput())



main(0)
