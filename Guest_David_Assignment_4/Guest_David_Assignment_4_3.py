"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.3
Due Date: 4/25/22

Algebra: solve 2 × 2 linear equations
"""


# uses the formula to calculate the y value
def calculateY(a, b, c, d, e, f):
    numerator = a * f - e * c
    denom = denominator(a, b, c, d)
    return numerator / denom


# uses the formula to calculate the x value
def calculateX(a, b, c, d, e, f):
    numerator = e * d - b * f
    denom = denominator(a, b, c, d)
    return numerator / denom


# just calculates the denominator of x and y
def denominator(a, b, c, d):
    return a * d - b * c


# run my methods starting here
def main(args):
    a, b, c, d, e, f = eval(input(f"Enter a, b, c, d, e, f: "))
    if denominator(a, b, c, d) == 0:  # catch case for denominator == 0
        print(f"\nThe equation has no solution.")
        return
    else:
        x = calculateX(a, b, c, d, e, f)
        y = calculateY(a, b, c, d, e, f)
        print(f"\nX is {x} and Y is {y}.")
        return


main(0)
