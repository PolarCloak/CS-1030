"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.4
Due Date: 4/8/22

Conversion from miles to kilometers
"""
# static variables
MI_TO_KM = 1.609


# prints the top part of the table
def tableTop():
    print(f"{'Miles':<10} {'Kilometers':>20}")


# displays the table starting from 1 to 10
def tableLoop():
    for miles in range(1, 11, 1):
        print(f"{miles:<10}           {miles * MI_TO_KM:<1.3f}")


# run my methods starting here
def main():
    tableTop()
    tableLoop()
    return


main()
