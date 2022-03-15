"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.5
Due Date: 4/25/22

Find future dates
"""


# converts a number code into its corresponding day of the week. (trying to use exceptions as well)
def convertToDay(numberCode):
    if numberCode == 0:
        return "Monday"
    elif numberCode == 1:
        return "Tuesday"
    elif numberCode == 2:
        return "Wednesday"
    elif numberCode == 3:
        return "Thursday"
    elif numberCode == 4:
        return "Friday"
    elif numberCode == 5:
        return "Saturday"
    elif numberCode == 6:
        return "Sunday"
    else:
        # hopefully this will throw a new error if I try to convert a number out of bounds
        raise ValueError


# run my methods starting here
def main(args):
    # modding by 7 on input to avoid putting OutOfBounds values
    today = eval(input(f"Enter today's day: ")) % 7
    offset = eval(input(f"Enter the number of days elapsed since today:"))
    total = today + offset
    future = total % 7
    print(f"Today is {convertToDay(today)} and the future day is {convertToDay(future)}")
    return


main(0)
