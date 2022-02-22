"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Working with if statements
"""


def getLetterGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D"
    else:
        return "F"


inp = eval(input(f"Enter the students score: \n"))
print(f"The grade is {getLetterGrade(inp)}")
