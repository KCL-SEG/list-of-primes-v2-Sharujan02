"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isnumprime(x):
    prime = False
    if x > 1:
        # if a factor is found, then returns False
        for i in range (2, x):
            if (x % i) == 0:
                return False
    return True


def primes(number_of_primes):
    # raises and terminates the program if input is not a positive number
    if number_of_primes <= 0:
        raise ValueError(f"x={number_of_primes} should have been a positive number")
    list = []
    # used to track list count
    count = 0
    # prime numbers start with 2
    num = 2

    while count < number_of_primes:
        if isnumprime(num):
            list.append(num)
            count += 1
        num += 1
    return list
