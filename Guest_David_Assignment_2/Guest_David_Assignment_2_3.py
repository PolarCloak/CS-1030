"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.3
Due Date: 2/11/2022

Convert feet into meters
"""


# convert a value in feet to meters
def feet_to_meters(feet):
    return 0.305 * feet


# run my methods starting here
def main(args):
    feet = float(input("Enter a value for feet: "))
    print("{0} feet is {1} meters ".format(feet, feet_to_meters(feet).__format__(".4f")))


main(0)
