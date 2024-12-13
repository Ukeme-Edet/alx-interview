#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Function that returns the winner of the game

    Args:
        x: the number of rounds
        nums: a list of integers

    Returns:
        The winner of the game
    """
    if x != len(nums):
        return None
    ps = [1] * 10001
    ps[0] = ps[1] = 0
    for i in range(2, 10001):
        if ps[i]:
            for j in range(i * i, 10001, i):
                ps[j] = 0
    primes = [x for x in range(10001) if ps[x]]
    log = {"Ben": 0, "Maria": 0}
    for num in nums:
        i = 0
        while primes[i] <= num:
            i += 1
        log["Maria" if i % 2 else "Ben"] += 1
    return (
        "Ben"
        if log["Ben"] > log["Maria"]
        else "Maria" if log["Ben"] < log["Maria"] else None
    )
