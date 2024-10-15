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
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


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
