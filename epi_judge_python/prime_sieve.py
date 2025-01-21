from typing import List

from test_framework import generic_test

# Inputs:
# n: int, number up to which to generate primes

# Outputs:
# primes: List[int], list of primes between 1 and n

# Notes / Assumptions:

# Examples:
# n = 18
# primes = [2, 3, 5, 7, 11, 13, 17]

# Given n, return all primes up to and including n.
def generate_primes0(n: int) -> List[int]:
    if n < 2:
        return []

    i = 3
    primes = [2]
    while i <= n:
        is_divisible = False
        for p in primes:
            if i % p == 0:
                is_divisible = True
                break

        if not is_divisible:
            primes.append(i)

        i += 1

    return primes

def generate_primes(n: int) -> List[int]:
    is_prime = [False, False] + [True] * (n - 1)
    primes = []

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)

            # NOTE: Can step by p rather than checking i % p == 0
            for i in range(p, n + 1, p):
                is_prime[i] = False

    return primes

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
