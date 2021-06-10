#!/usr/bin/env python3

import os
import math

SIZE = int(os.environ.get('SIZE', 9))
if int(math.sqrt(SIZE)) != math.sqrt(SIZE):
    raise ValueError("SIZE must be a square")

# 1 through 9
SYMBOLS = [str(i + 1) for i in range(SIZE)]

# A square is just a mutable set of remaining valid symbols.
# Starts with all symbols.
def init_square():
    return set(SYMBOLS)

# A board is a square array of arrays.
def init_board():
    board = []
    for _ in range(SIZE):
        row_squares = []
        for _ in range(SIZE):
            row_squares.append(init_square())
        board.append(row_squares)
    return board

# Returns a string.
def render_board(board):
    square_dim = int(math.sqrt(SIZE))
    render_dim = (square_dim + 1) * SIZE
    lines = [[' '] * render_dim for row in range(render_dim)]
    for board_row in range(SIZE):
        for board_col in range(SIZE):
            for i, symbol in enumerate(SYMBOLS):
                square_row = i // square_dim
                square_col = i % square_dim
                render_row = board_row * (square_dim + 1) + square_row
                render_col = board_col * (square_dim + 1) + square_col
                lines[render_row][render_col] = symbol
    return '\n'.join(''.join(line) for line in lines)

def main():
    board = init_board()
    print(render_board(board))

main()
