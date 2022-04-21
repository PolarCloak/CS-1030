"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Looking at lists
"""
list1 = [4, 5, 6, 2, 1, 3, 5]

# traversing a for loop
print(f"\nThe full list: ")
for x in list1:
    print(f"{x}", end=" ")

# use the step value to traverse differently
print(f"\nList stepping: ")
for i in range(0, len(list1), 2):
    print(f"{list1[i]}", end=" ")
print("\n")

# the to list must contain the same number of elements
listA = ["red", "green", "blue"]
listB = ["green", "blue", "red"]

# comparison uses lexicographical ordering, the first two elements are compared.
# if they are different, then it changes the outcome of the comparison.
# if they are equal, then the next two elements are compared.

print(listA == listB)
print(listA < listB)
print(listA <= listB)

# we can append lists. Appends go to the end of the list
print(listA)
listA.append("cyan")
listA.append("yellow")
print(listA)

# we can count on lists
# this will count how many times 4 occurs in the list
print(list1)
print(list1.count(4))
list1.append(4)
print(list1.count(4))

# extending lists
list1.extend(listA)
print(list1)

# printing indexes
# returns the index of the first occurrence of the number 4
list1.index(4)

# insert
list1.insert(1, 25)
# inserts the value of 25 into index 1
print(list1)
# everything gets pushed to the right.

# remove method
# removes the first occurrence of the value
list1.remove(25)
print(list1)

# reverse method, flips the list around.
print(list1.reverse())

