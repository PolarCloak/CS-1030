"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

lists in the form of arguments
"""

# the contents of a list may change after being sent into a function
# anonymously | anonymous list
list1 = [1, 2, 5, 46, 3, 2, 123, 4, 5, 57, 75, 5, 43]


def printList(lst):
    for item in lst:
        print(item, end=" ")


def m(num, nums):
    num = 1001
    nums[0] = 5555
    return


def revrs(lst):
    result = []
    for x in lst:
        result.insert(0, x)
    return result


# mutable vs immutable
# mutable is something changeable or has the ability to change.
# lists are mutable objects, which means contents of a list may change in a function
# also, other mutable objects are set; dictionaries.

# immutable would be the opposite.
# does not allow any changes in the object once it has been created.
# numbers, strings, tuples

def main():
    printList([1, 2, 3, 4, 5])
    print("\n\n")
    x = 1
    # x represents an integer object which is immutable.
    y = [1, 2, 3]
    # y represents a list object which is mutable

    m(x, y)
    print(f"x is {x}")
    print(f"y is {y}")

    list2 = [1, 2, 3, 5, 6, 7, 9]
    print(revrs(list2))
    list2.reverse()
    print(list2)
    list2.reverse()
    print(list2)



main()
