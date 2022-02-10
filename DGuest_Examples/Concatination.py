"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Determining the area of a circle.
"""

first_name, last_name = input("Input first name, last name: ").split(",")

print("Welcome, {0} {1}, to Sword Art Online.".format(first_name, last_name))
print("\n")
print(("         Help, there is a man in my home.            ").strip())
print(format(45.56, "15.3f"))
print(format(45.56, "<15.3f"))
print(format(45.56, "^20.3f"))
print(format(45.56, "10.3e"))
print(format(0.597, "<.1%"))

# d is for decimal, x is for hex, o = octal, b is binary
print(format(87, "d"))
print(format(87, "x"))
print(format(87, "o"))
print(format(87, "b"))

print(format("Welcome to Python", "s"))
print(format("Welcome to Python", ">25"))

# formatting with the string class
s = "School Day"
print(s.ljust(25))
print(s.center(25))
print(s.rjust(25))

# formatting with .format(), used in python 2.6 and later
name = "Joe"
age = 22

print("Hello {0}, your age is {1:.1f}".format(name, age))

# F-string type of formatting, used in python 3

print(f"Hello {name} you are {age:x}\n")

# multi-line options
message = \
    f"Message 1:\n" \
    f"Hi {name}\n" \
    f"Age {age}.\n"
message2 = (
    f"Message 2:\n"
    f"Name: {name}\n"
    f"Binary age: {age:b}.\n"
)

print(message)
print(message2)
