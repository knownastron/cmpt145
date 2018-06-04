"""
CMPT 145 Computing with Python Lists
The Sieve of Eratosthenes

How many prime numbers are there between 2 and n?

Algorithm:
    Sift the Two's and Sift the Three's,
    The Sieve of Eratosthenes.
    When the multiples sublime,
    The numbers that remain are Prime.

        -- Anonymous
"""

n = 100000  # end of range of numbers to check for primes

still_is_prime = (n+1)*[True] # assume prime until disproven

for i in range(2, n):
    if still_is_prime[i]:
        # mark multiples of i as not prime
        for j in range(2, n//i + 1):
            still_is_prime[i * j] = False

# now, every possible prime is a definite prime
count = sum([1 for v in still_is_prime[2:] if v])

print("# Prime numbers between 2 and " + str(n) + ":", count)
