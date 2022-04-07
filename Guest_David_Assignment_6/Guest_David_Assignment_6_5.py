"""
CS10300-20766
ID#700714467
David Guest
Assignment #6.5
Due Date: 4/22/22

Sort three numbers (added a choice for ascending or descending)
"""
# global variables
sortFlag = "a"


# takes in 3 values and returns them in an array sorted. Increasing order.
def displaySortedNumbers(num1, num2, num3):
    items = list()
    items.append(num1)
    items.append(num2)
    items.append(num3)
    # now that they are all in a list, built-in sorts are available
    if sortFlag.lower() == "d" or sortFlag.lower() == "desc":
        items.sort(reverse=True)
    else:
        items.sort()
    return items


# run my methods starting here
def main():
    global sortFlag
    x, y, z = eval(input(f"Enter three numbers: "))
    sortFlag = input(f"What order would you like it sorted? (A/D):")
    print(f"The sorted numbers are: {displaySortedNumbers(x, y, z)}")
    return


main()
