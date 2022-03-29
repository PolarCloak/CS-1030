"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.3
Due Date: 4/8/22

Conversion from kilograms to pounds
"""
# static variables
KG_TO_LB = 2.2


# prints the top part of the table
def tableTop():
    print(f"{'Kilograms':<1} {'Pounds':>20}")


# displays the table starting from 1 to 199 using only the odds
def tableLoop():
    for kgs in range(1, 200, 2):
        print(f"{kgs:<5}               {kgs * KG_TO_LB:>10.1f}")


# run my methods starting here
def main():
    tableTop()
    tableLoop()
    return


main()
