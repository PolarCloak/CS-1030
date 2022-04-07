"""
CS10300-20766
ID#700714467
David Guest
Assignment #6.4
Due Date: 4/22/22

Display an integer reversed
"""


# takes a number variable, and returns the reverse of that number.
def reverse(number):
    numString = str(number)
    chars = list(numString)
    # python has a built-in function for reversing a list.
    chars.reverse()
    # and then for putting the chars back together in a variable
    reversedString = "".join(chars)
    return reversedString


# run my methods starting here
def main():
    given = input(f"Type anything and I will display it in reverse: ")
    print(f"Reversed: {reverse(given)}")
    return


main()
