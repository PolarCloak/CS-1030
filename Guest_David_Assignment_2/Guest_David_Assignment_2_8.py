"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.8
Due Date: 2/11/2022

Converts an input value of mass, starting temp, and final temp and returns the joules needed to  heat it up
"""


# takes in mass of water used, starting temp and final temp to calculate the joules needed to heat it
def get_joules(mass, start_temp, end_temp):
    joules = mass * (end_temp - start_temp) * 4184
    return joules


# run my methods starting here
def main(args):
    mass = eval(input("Enter the amount of water in kilograms: "))
    start_temp = eval(input("Enter the initial temperature: "))
    end_temp = eval(input("Enter the final temperature: "))
    joules = get_joules(mass, start_temp, end_temp)
    print("The energy needed is {0} joules.".format(joules.__format__(".1f")))


main(0)
