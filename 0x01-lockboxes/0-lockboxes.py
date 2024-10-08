#!/usr/bin/python3
"""
Lockboxes
"""
from queue import Queue


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list[list[int]]): a list of lists of integers

    Returns:
        bool: True if all boxes can be opened, False otherwise
    """
    stat = [False] * len(boxes)
    stat[0] = True
    to_visit = Queue()
    to_visit.put(0)
    while not to_visit.empty():
        box = to_visit.get()
        for key in boxes[box]:
            if key < len(boxes) and not stat[key]:
                stat[key] = True
                to_visit.put(key)
    return all(stat)
