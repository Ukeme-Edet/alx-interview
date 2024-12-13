#!/usr/bin/python3
"""
Prime Game
"""


def checkWinner(num):
    """
    Function that returns the winner of the game

    Args:
        num: an integer

    Returns:
        The winner of the game
    """
    turns = 0
    x = [False for i in range(num + 1)]
    for i in range(2, num + 1):
        if not x[i]:
            turns += 1
            for j in range(i, num + 1, i):
                x[j] = True
    return "Maria" if turns % 2 else "Ben"


def isWinner(x, nums):
    """
    Function that returns the winner of the game

    Args:
        x: the number of rounds
        nums: a list of integers

    Returns:
        The winner of the game
    """
    log = {"Ben": 0, "Maria": 0}
    for num in nums:
        log[checkWinner(num)] += 1
    return (
        "Ben"
        if log["Ben"] > log["Maria"]
        else "Maria" if log["Ben"] < log["Maria"] else None
    )
