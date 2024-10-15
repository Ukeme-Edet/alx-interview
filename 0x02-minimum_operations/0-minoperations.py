#!/usr/bin/python3
"""
Minimum Operations
"""
from collections import defaultdict


def get_prime_factors(n):
    """
    Get prime factors of a number

    Args:
        n (int): number to get prime factors of

    Returns:
        list: list of prime factors
    """
    pf = [True] * (n + 1)
    pf[0] = False
    for i in range(2, int(n**0.5) + 1):
        if pf[i]:
            for j in range(i * i, n + 1, i):
                pf[j] = False
    return [i for i in range(2, n + 1) if pf[i] and not n % i]


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H\
        characters in the file

    Args:
        n (int): number of H characters

    Returns:
        int: fewest number of operations needed
    """
    dp = defaultdict(lambda: float("inf"))
    dp[1] = 0
    pf = get_prime_factors(n)
    for f in pf:
        dp[f] = min(dp[f], f)
        for i in range(f, n + 1, f):
            dp[i] = min(dp[i], dp[f] + i // f)
    return dp[n]
