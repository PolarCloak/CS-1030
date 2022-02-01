"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.1
Due Date: 2/11/2022

We are converting degree values from Celsius into Fahrenheit
"""


# converts a celsius value into fahrenheit
def convert_to_f(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


# run my methods starting here
def main(args):
    celsius = float(input("Please type a value in Celsius: "))
    print("{0} degrees Celsius is {1} degrees Fahrenheit.".format(celsius, convert_to_f(celsius).__format__(".2f")))


main(0)
