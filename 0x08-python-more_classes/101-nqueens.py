#!/usr/bin/python3
"""
This is the  N queens puzzle.
"""


import sys


def is_safe(board, row, col):
    # Checking if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Checking if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Checking if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

    backtrack(0)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        print('\n'.join(solution))
        print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
