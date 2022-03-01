"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A


"""

# prompt user for a year
year = eval(input(f"Enter a year: "))
zodiacYear = year % 12
zodiacName = ""
extraSentence = ""
if zodiacYear == 0:
    zodiacName = "Monkey"
    extraSentence = "That's pretty funky!"
elif zodiacYear == 1:
    zodiacName = "Rooster"
    extraSentence = "What a morale booster!"
elif zodiacYear == 2:
    zodiacName = "Dog"
    extraSentence = "Pogg!"
elif zodiacYear == 3:
    zodiacName = "Pig"
    extraSentence = "That's really big!"
elif zodiacYear == 4:
    zodiacName = "Rat"
    extraSentence = "How cool is that!"
elif zodiacYear == 5:
    zodiacName = "Ox"
    extraSentence = "Fresh out of the box!"
elif zodiacYear == 6:
    zodiacName = "Tiger"
    extraSentence = "Nothing really rhymes with tiger..."
elif zodiacYear == 7:
    zodiacName = "Rabbit"
elif zodiacYear == 8:
    zodiacName = "Dragon"
elif zodiacYear == 9:
    zodiacName = "Snake"
elif zodiacYear == 10:
    zodiacName = "Horse"
else:
    zodiacName = "Sheep"


print(f"You were born in the year of the {zodiacName}! How cool is that?")

