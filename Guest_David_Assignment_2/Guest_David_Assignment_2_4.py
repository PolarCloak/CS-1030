"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.4
Due Date: 2/11/2022

Convert pounds into kilograms
"""


# convert value in pounds to kilograms
def lbs_to_kgs(lbs):
    return lbs * 0.454


# run my methods starting here
def main(args):
    lbs = float(input("Enter a value in pounds: "))
    print("{0} pounds is {1} kilograms ".format(lbs, lbs_to_kgs(lbs).__round__(3)))


main(0)
