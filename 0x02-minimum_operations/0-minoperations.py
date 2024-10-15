#!/usr/bin/python3
"""
Minimum Operations
"""
from collections import defaultdict


def get_factors(n):
    """
    Get prime factors of a number

    Args:
        n (int): number to get prime factors of

    Returns:
        list: list of prime factors
    """
    factors = []
    for i in range(1, n + 1):
        if not n % i:
            factors.append(i)
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
    dp = defaultdict(lambda: float("inf"))
    dp[1] = 0
    fs = get_factors(n)
    for f in fs:
        dp[f] = min(dp[f], f)
        for i in range(f, n + 1, f):
            dp[i] = min(dp[i], dp[f] + i // f)
    return dp[n]
