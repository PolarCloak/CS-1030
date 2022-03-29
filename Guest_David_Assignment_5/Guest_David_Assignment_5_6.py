"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.6
Due Date: 4/8/22

Conversion from miles to kilometers vice-versa
"""
# static variables
MI_TO_KM = 1.609
KM_TO_MI = 0.621


# prints the top part of the table
def tableTop():
    print(f"{'Miles':<}      {'Kilometers':<}      |      {'Kilometers':<}       {'Miles':<}")


# displays the table
def tableLoop():
    print(f"--------------------------------------------------------------")
    for i in range(0, 10, 1):
        mi = i + 1
        km = i * 5 + 20
        print(f"{mi:<10} {MI_TO_KM * mi:<16.3f}|      {km:<16} {KM_TO_MI * km:<.3f}")


# run my methods starting here
def main():
    tableTop()
    tableLoop()
    return


main()
