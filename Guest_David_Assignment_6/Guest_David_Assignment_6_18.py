"""
CS10300-20766
ID#700714467
David Guest
Assignment #6.18
Due Date: 4/22/22

Display matrix of 0’s and 1’s
"""
# imports
import random


# takes a matrix array and prints all of the contents
def printMatrix(matrix):
    for x in range(len(matrix)):
        print()
        for y in range(len(matrix[x])):
            print(f"{matrix[x][y]} ", end="")


# takes a size value and returns a new matrix with lengths: [size][size] and fills randomly with 0 or 1
def createMatrix(size):
    # in case we wanted to allow the row and column to be different numbers
    row, column = (size, size)
    # initializing the matrix with 0's
    matrix = [[0 for x in range(column)] for y in range(row)]
    for x in range(column):
        for y in range(row):
            # assignment line where we set the value of each item
            matrix[x][y] = random.randint(0, 1)
    return matrix


# run my methods starting here
def main():
    printMatrix(createMatrix(40))
    return


main()
