#!/usr/bin/python3
"""
Lockboxes
"""
from collections import defaultdict


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list[list[int]]): a list of lists of integers

    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    unlocked = defaultdict(bool)
    dfs(boxes, 0, unlocked)
    return all(unlocked[box] for box in range(len(boxes)))


def dfs(boxes, box=0, unlocked=defaultdict(bool)):
    """
    Depth-first search

    Args:
        boxes (list[list[int]]): a list of lists of integers
        box (int): the current box
        unlocked (dict): a dictionary of unlocked boxes
    """
    if unlocked[box]:
        return
    unlocked[box] = True
    for bo in boxes[box]:
        dfs(boxes, bo, unlocked)
