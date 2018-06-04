"""
CMPT 145 Computing with Python Lists
Naive primes.

How many prime numbers are there between 2 and n?
"""

n = 100000  # end of range of numbers to check for primes

count = 0
for i in range(2, n + 1):
    no_factors_found = True  # assume prime until disproven
    f = 2
    # check if i is prime by checking remainders
    while no_factors_found and f < i:
        if i % f == 0:
            no_factors_found = False
        f += 1

    if no_factors_found:
        count += 1

print("# Prime numbers between 2 and " + str(n) + ":", count)
