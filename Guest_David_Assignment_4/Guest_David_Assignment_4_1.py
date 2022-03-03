"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.1
Due Date: 4/25/22

Algebra: solve quadratic equations
"""
import math


# uses equation 2 and returns the root
def getRoot2(a, b, c):
    dis = getDiscriminant(a, b, c)
    root = (-b - math.sqrt(dis)) / 2 * a
    return root


# uses equation 1 and returns the root
def getRoot1(a, b, c):
    dis = getDiscriminant(a, b, c)
    root = (-b + math.sqrt(dis)) / 2 * a
    return root


# calculates the discriminant using a, b, and c
def getDiscriminant(a, b, c):
    dis = (b ** 2) - (4 * a * c)
    return dis


# uses the discriminant and determines how many roots there are going to be
def countRoots(a, b, c):
    dis = getDiscriminant(a, b, c)
    if dis < 0:
        return 0
    elif dis == 0:
        return 1
    else:
        return 2


# run my methods starting here
def main():
    a, b, c = eval(input(f"Enter a, b, c: "))
    roots = countRoots(a, b, c)
    if roots == 0:
        print(f"The equation has no real roots.")
        return
    elif roots == 1:
        root1 = getRoot1(a, b, c)
        print(f"The root is {root1:.5f}")
        return
    else:  # 2 roots
        root1 = getRoot1(a, b, c)
        root2 = getRoot2(a, b, c)
        print(f"The roots are {root1:.5f} and {root2:.5f}")
        return


main()
