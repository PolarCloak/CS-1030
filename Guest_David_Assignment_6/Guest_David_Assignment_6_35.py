"""
CS10300-20766
ID#700714467
David Guest
Assignment #6.35
Due Date: 4/22/22

Compute the probability
"""
# imports
import random as r


# returns a random capital character from ascii
def get_random_char():
    value = r.randrange(65, 91, 1)
    return chr(value)


# takes in the character specified to check for, and the number of chars to generate.
# Returns the number of occurrences
def count_data(character_to_count, total_chars):
    counted = 0
    check_char = character_to_count.upper()
    for i in range(total_chars):
        new_random_char = get_random_char()
        if new_random_char == check_char:
            print('\033[92m' + new_random_char + '\033[0m', end="")
            counted += 1
        else:
            print(new_random_char, end="")
    return counted


# run my methods starting here
def main():
    char_in = input(f"What character would you like to track?: ")
    max_value = 10000
    counted = count_data(char_in, max_value)
    print(f"The total number of occurrences of the letter {char_in} is {counted}/{max_value}")
    print(f"The percentage of {char_in}'s is {counted/max_value:.2%}")
    return


main()
