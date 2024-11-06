#!/usr/bin/python3
"""
N-queens problem
"""
import sys


def place_queens(np, n, cols, lrd, rld, cp=[]):
    """
    Place queens on board

    Args:
        np: next position
        n: number of queens
        cols: columns
        lrd: left-right diagonal
        rld: right-left diagonal
        cp: current position
    """
    if n == np:
        solutions.append(cp)
        return
    for i in range(n):
        if cols[i] or lrd[np + i] or rld[n - 1 + np - i]:
            continue
        cols[i] = lrd[np + i] = rld[n - 1 + np - i] = 1
        place_queens(np + 1, n, cols, lrd, rld, cp + [[np, i]])
        cols[i] = lrd[np + i] = rld[n - 1 + np - i] = 0


N = int(sys.argv[1])

columns = [0] * N
lrd = [0] * (2 * N - 1)
rld = [0] * (2 * N - 1)
solutions = []

place_queens(0, N, columns, lrd, rld)

for solution in solutions:
    print(solution)
