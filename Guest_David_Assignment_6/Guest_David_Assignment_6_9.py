"""
CS10300-20766
ID#700714467
David Guest
Assignment #6.9
Due Date: 4/22/22

Conversion between feet and meters
"""


# prints the top part of the table
def tableTop():
    print(f"{'Feet':<}       {'Meters':<}          |      {'Meters':<}           {'Feet':<}")
    print(f"--------------------------------------------------------------")


# prints out the table using the conversions
def displayTable():
    tableTop()
    for i in range(0, 10, 1):
        feet = i + 1
        meter = i * 6 + 20
        print(f"{feet:<10} {footToMeter(feet):<16.1f}|      {meter:<16} {meterToFoot(meter):<.2f}")
    return


# Converts from feet to meters
def footToMeter(foot):
    meter = 0.305 * foot
    return meter


# Converts from meters to feet
def meterToFoot(meter):
    foot = meter / 0.305
    return foot


# run my methods starting here
def main():
    displayTable()
    return


main()
