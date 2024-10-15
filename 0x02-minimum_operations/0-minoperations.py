#!/usr/bin/python3
"""
Minimum Operations
"""


def get_prime_factors(n):
    """
    Get prime factors of a number

    Args:
        n (int): number to get prime factors of

    Returns:
        list: list of prime factors
    """
    fac = [True] * (n + 1)
    fac[0] = fac[1] = False
    for i in range(2, int(n**0.5) + 1):
        if fac[i]:
            for j in range(i * i, n + 1, i):
                fac[j] = False
    facs = [i for i in range(2, n + 1) if fac[i] and not n % i]
    factors = []
    for i in facs:
        while not n % i:
            factors.append(i)
            n //= i
    return factors if factors else [n]


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H\
        characters in the file

    Args:
        n (int): number of H characters

    Returns:
        int: fewest number of operations needed
    """
    if n <= 1:
        return 0
    return sum(get_prime_factors(n))
