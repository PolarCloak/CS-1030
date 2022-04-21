"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Mutable default argument, values example
every time the function is called, the same list is used, no new list is made
on a new call.
"""

# adds the value x if it doesnt exist yet.
def add(x, lst=[]):
    if x not in lst:
        lst.append(x)
    return lst


def main():
    list1 = add(4)
    add(3)
    add(1)
    add(5)
    list2 = add(4)
    add(4)
    print(list1)
    print(list2)

    return


main()
