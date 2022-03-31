"""
CS10300-20766
ID#700714467
David Guest
Assignment #5.22
Due Date: 4/8/22

Display prime numbers between 2 and 1,000
(Display prime numbers between 2 and 1,000) Modify Listing 5.13 to
display all the prime numbers between 2 and 1,000, inclusive. Display eight prime numbers per line.
"""
# static variables
MAXIMUM = 1000

# global variables
primes = []


# prints a header for the list
def printHeader():
    print(f"Prime numbers between 2 and {MAXIMUM}:")


# prints the prime numbers found in the 'primes' variable
def printPrimes():
    printHeader()
    counter = 0
    spacing = 4
    while len(primes) > 0:
        # found out that you can use variables in place of parts of a f-string formatting
        print(f"{primes.pop():<{spacing}} ", end='')
        counter += 1
        if counter == 8:
            counter = 0
            print(f"\n")


# a primary method that collects the prime numbers
def getPrimes(maximum):
    global primes
    # loop through all of the number from min to max
    for i in range(2, maximum + 1, 1):
        notPrime = False
        # at each number, we want to check all of the found primes so far.
        for foundPrime in primes:
            # if the number we are on and the prime we are on are divisible, then it is not a prime
            if i % foundPrime == 0:
                notPrime = True
                break
        # once we have checked all of the current primes against this item
        # if notPrime hasn't been changed, then it must be prime
        if not notPrime:
            primes.append(i)
    # reverse the primes so that they can be popped off of the list in correct order
    primes.reverse()
    return


# run my methods starting here
def main():
    getPrimes(MAXIMUM)
    printPrimes()
    return


main()
