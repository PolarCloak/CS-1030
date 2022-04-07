"""
CS10300-20766
ID#700714467
David Guest
Assignment #6.8
Due Date: 4/22/22

Conversion between Celsius and Fahrenheit
"""


# prints the top part of the table
def tableTop():
    print(f"{'Celsius':<}    {'Fahrenheit':<}      |      {'Fahrenheit':<}       {'Celsius':<}")
    print(f"--------------------------------------------------------------")


# prints out the table using the conversions
def displayTable():
    tableTop()
    for i in range(10, 0, -1):
        far = i * 10 + 20
        cel = i + 30
        print(f"{cel:<10} {celsiusToFahrenheit(cel):<16.1f}|      {far:<16} {fahrenheitToCelsius(far):<.2f}")
    return


# Converts from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


# Converts from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


# run my methods starting here
def main():
    displayTable()
    return


main()
