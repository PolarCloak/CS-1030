"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.1
Due Date: 4/8/22

Count positive & negative numbers & compute average
"""
posCount = 0
posTotal = 0
negCount = 0
negTotal = 0


def displayOutputs():
    global posCount, posTotal, negCount, negTotal
    total = posTotal - negTotal
    totalCount = posCount + negCount
    print(f"\nThe number of positives is {posCount}")
    print(f"The number of negatives is {negCount}")
    print(f"The total is {total}")
    print(f"The average is {total / totalCount}")


def getInputs():
    global posCount, posTotal, negCount, negTotal
    value = -1
    while value != 0:
        value = eval(input(f"Enter an integer, the input ends if it is 0: "))
        if value == 0:
            break
        elif value < 0:
            negTotal += abs(value)
            negCount += 1
        elif value > 0:
            posTotal += value
            posCount += 1
        else:
            raise ValueError
    return


def noInput():
    global posCount, negCount
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
