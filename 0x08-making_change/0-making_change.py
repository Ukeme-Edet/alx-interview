#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.

    Arguments:
    - coins: a list of the values of the coins in your possession
    - total: an integer total to meet

    Returns:
    - the fewest number of coins needed to meet the total
    """
    if total < 0:
        return 0
    dp = [0] + [float("inf")] * total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float("inf") else -1
