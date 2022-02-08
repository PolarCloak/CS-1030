"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.7
Due Date: 2/11/2022

This program converts an input of minutes into a total number of years and the remaining
days towards the next year
"""
# variables used to store the total years and leftover days after calculation
leftoverDays = 0
totalYears = 0


# converts number of days to years, and then stores the leftover days in a global variable
def days_to_years(days):
    global totalYears
    global leftoverDays
    totalYears = days / 365
    leftoverDays = days % 365
    return totalYears


# converts number of minutes to number of days
def minutes_to_days(minutes):
    hours = minutes / 60
    days = hours / 24
    return days


# run my methods starting here
def main(args):
    minutes = eval(input("Enter the number of minutes: "))
    days_to_years(minutes_to_days(minutes))
    print(
        "{0} minutes is approximately {1} years and {2} days.".format(int(minutes), int(totalYears),
                                                                      int(leftoverDays)))


main(0)
