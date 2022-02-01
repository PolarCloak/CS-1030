"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.5
Due Date: 2/11/2022

Financial application: Calculate tips
"""


# adds the tip to the subtotal.
def calculate_total(subtotal, tip):
    return subtotal + tip


# take the subtotal and a percent integer and determines the tip value
def calculate_tip(subtotal, percent):
    percent_float = percent * 0.01
    return subtotal * percent_float


# run my methods starting here
def main(args):
    subtotal, percent = eval(input("Enter the subtotal and a gratuity rate: "))
    tip = calculate_tip(subtotal, percent)
    print("The gratuity is ${0} and the total is ${1}".format(tip.__format__(".2f"),
                                                              calculate_total(subtotal, tip).__format__(".2f")))


main(0)
