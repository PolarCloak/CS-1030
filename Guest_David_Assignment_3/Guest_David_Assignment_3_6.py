"""
CS10300-20766
ID#700714467
David Guest
Assignment #3.6
Due Date: 2/25/2022

Find the Character of an ASCII Code
"""


# Simply converts the asci value provided into a character
def asci_to_char(asci_value):
    return chr(asci_value)


# run my methods starting here
def main(args):
    asci_in = int(input("Enter an ASCII code: "))
    character = asci_to_char(asci_in)
    print(f"The character is {character}")


main(0)
