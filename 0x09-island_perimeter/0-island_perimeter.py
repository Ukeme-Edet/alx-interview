#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid

    Args:
        grid: a list of list of integers

    Returns:
        The perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[i]):
                        perimeter += grid[i + dx][j + dy]
    return perimeter
