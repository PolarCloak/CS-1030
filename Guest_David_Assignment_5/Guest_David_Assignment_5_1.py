"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.1
Due Date: 4/8/22

Count positive & negative numbers & compute average
"""
# global variables used to access throughout all methods
posCount = 0
posTotal = 0
negCount = 0
negTotal = 0


# after collecting the total counts and total values, we are going to use them and display our output
def displayOutputs():
    global posCount, posTotal, negCount, negTotal
    total = posTotal - negTotal
    totalCount = posCount + negCount
    print(f"\nThe number of positives is {posCount}")
    print(f"The number of negatives is {negCount}")
    print(f"The total is {total}")
    print(f"The average is {total / totalCount}")


# uses a while loop to constantly collect new inputs to be added to global variables until 0 is used
def getInputs():
    global posCount, posTotal, negCount, negTotal
    value = -1
    # always loop, and only leave when you break
    while True:
        value = eval(input(f"Enter an integer, the input ends if it is 0: "))
        # separate the negatives and positives, and the stand-alone 0
        if value == 0:
            break
        elif value < 0:
            negTotal += abs(value)
            negCount += 1
        elif value > 0:
            posTotal += value
            posCount += 1
        else:
            # shouldn't be possible, but catching anything else
            raise ValueError
    return


# runs a check to see if there was no inputs by checking both pos and neg counts, returns True if no input
def noInput():
    global posCount, negCount
    # when there are no count of positives or negatives.
    if posCount == 0 and negCount == 0:
        return True
    else:
        return False


# run my methods starting here
def main():
    getInputs()
    if not noInput():
        displayOutputs()
    else:
        print(f"You didn't enter any number.")
        return


main()
