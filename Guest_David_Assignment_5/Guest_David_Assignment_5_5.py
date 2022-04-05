"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.5
Due Date: 4/8/22

Conversion from kilograms to pounds vice-versa
"""
# static variables
KG_TO_LB = 2.2
LB_TO_KG = 0.45


# prints the top part of the table
def tableTop():
    print(f"{'Kilograms':<}      {'Pounds':<}      |      {'Pounds':<}       {'Kilograms':<}")
    print(f"--------------------------------------------------------------")


# displays the table
def tableLoop():
    # loop from 0-99 and uses that number to go to Kg and Lb with multiplying a constant
    for i in range(0, 100, 1):
        kg = i * 2 + 1
        lb = i * 5 + 20
        print(f"{kg:<14} {KG_TO_LB * kg:<12.1f}|      {lb:<12} {LB_TO_KG * lb:<.2f}")


# run my methods starting here
def main():
    tableTop()
    tableLoop()
    return


main()
