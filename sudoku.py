#!/usr/bin/env python3

import os
import math
import sys

SIZE = int(os.environ.get('SIZE', 9))
if int(math.sqrt(SIZE)) != math.sqrt(SIZE):
    raise ValueError("SIZE must be a square")
OFFSET = int(os.environ.get('OFFSET', 0))

# 1 through 9
SYMBOLS = [i + OFFSET for i in range(SIZE)]

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

# Update the available symbols for a cell
def update_cell(board, row, col, symbols):
    symbols = set(symbols)
    invalid = symbols - set(SYMBOLS)
    if invalid:
        raise ValueError("invalid symbols: {}".format(invalid))
    if row >= SIZE or col >= SIZE:
        raise ValueError("coordinates out of range: ({}, {})".format(row, col))
    board[row][col] = symbols

def done(board):
    for row in board:
        for cell in row:
            if len(cell) > 1:
                return False
    return True

def parse_update(line):
    coords, symbols = line.split(':')
    row, col = list(map(int, coords.split(',')))
    symbols = list(map(int, symbols.split(',')))
    return row, col, symbols

def main():
    board = init_board()
    while not done(board):
        print('---')
        print(render_board(board))
        print("Provide an update in the format 'row,col:s1,s2,s3,...'")
        for line in sys.stdin:
            line = line.strip()
            if line == 'q':
                return
            try:
                row, col, symbols = parse_update(line.strip())
                break
            except:
                print("Failed to parse update: '{}'".format(line))
        print()
        try:
            update_cell(board, row, col, symbols)
            print("Applied update ({}, {}) -> {}".format(row, col, symbols))
        except Exception as e:
            print("Failed to apply update: '{}': {}".format(line, e))


main()
