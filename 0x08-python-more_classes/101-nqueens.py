#!/usr/bin/python3
"""
This is the  N queens puzzle.
"""


import sys


def is_safe(board, row, col):
    """Checking if the current position is safe for the queen"""

    for c in range(col):
        if board[row][c] == 1:
            return False

    # Checking the upper diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Checking the lower diagonal
    r, c = row, col
    while r < N and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return (True)


def solve_nqueens(board, col):
    # Base case: all queens have been placed
    if col >= N:
        print_solution(board)
        return (True)

    # Recursive case: try placing the queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1

            # Recursively solve for the next column
            solve_nqueens(board, col + 1)

            # Backtrack: remove the queen and try the next row
            board[row][col] = 0

    return (False)


def print_solution(board):
    # Print the current solution
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

# Checking the command-line arguments


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

# Create an empty N x N chessboard
board = [[0] * N for _ in range(N)]

# Solve the N Queens problem
solve_nqueens(board, 0)
