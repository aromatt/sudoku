#!/usr/bin/env python3

import os
import math

SIZE = int(os.environ.get('SIZE', 9))
if int(math.sqrt(SIZE)) != math.sqrt(SIZE):
    raise ValueError("SIZE must be a square")

# 1 through 9
SYMBOLS = [i + 1 for i in range(SIZE)]

# A cell is just a mutable set of remaining valid symbols.
# Starts with all symbols.
def init_cell():
    return set(SYMBOLS)

# A board is a cell array of arrays.
def init_board():
    board = []
    for _ in range(SIZE):
        row_cells = []
        for _ in range(SIZE):
            row_cells.append(init_cell())
        board.append(row_cells)
    return board

# Returns a string.
def render_board(board):
    cell_dim = int(math.sqrt(SIZE))
    render_dim = (cell_dim + 1) * SIZE
    lines = [[' '] * render_dim for row in range(render_dim)]
    for board_row in range(SIZE):
        for board_col in range(SIZE):
            for i, symbol in enumerate(SYMBOLS):
                cell_row = i // cell_dim
                cell_col = i % cell_dim
                render_row = board_row * (cell_dim + 1) + cell_row
                render_col = board_col * (cell_dim + 1) + cell_col
                if symbol in board[board_row][board_col]:
                    lines[render_row][render_col] = str(symbol)
    return '\n'.join(''.join(line) for line in lines)

# Update the valid cells for a row and col
def update_cell(board, row, col, valid_symbols):
    board[row][col] = set(valid_symbols)

def main():
    board = init_board()
    print(render_board(board))
    update_cell(board, 0, 2, [3, 4, 5, 6])
    print('---')
    print()
    print(render_board(board))

main()
