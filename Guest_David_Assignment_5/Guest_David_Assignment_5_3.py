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
    print(f"Kilograms       Pounds")


# displays the table starting from 1 to 199 using only the odds
def tableLoop():
    for kgs in range(1, 200, 2):
        print(f"{kgs}               {kgs * KG_TO_LB:.1f}")


# run my methods starting here
def main():
    tableTop()
    tableLoop()
    return


main()
