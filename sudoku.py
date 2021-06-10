#!/usr/bin/env python3

import os
import math
import sys
from typing import List, Set, Tuple

### Environment Variables ###
#
# - SIZE:   board side length; must be a square
# - OFFSET: minimum symbol value
#
SIZE = int(os.environ.get('SIZE', 9))
if int(math.sqrt(SIZE)) != math.sqrt(SIZE):
    raise ValueError("SIZE must be a square")
OFFSET = int(os.environ.get('OFFSET', 0))

### Types for annotations ###
Symbol = int
Cell = Set[Symbol]
Board = List[List[Set[Symbol]]]

# Generate the set of valid symbols for this run
SYMBOLS = list(i + OFFSET for i in range(SIZE))

def init_cell() -> Cell:
    return set(SYMBOLS)

def init_board() -> Board:
    board = []
    for _ in range(SIZE):
        row_cells = []
        for _ in range(SIZE):
            row_cells.append(init_cell())
        board.append(row_cells)
    return board

def render_board(board: Board) -> str:
    '''Returns a string representing the provided board.'''
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

def update_cell(board: Board, row: int, col: int, symbols: List[Symbol]):
    '''Updates the available symbols for a cell.'''
    symbols = set(symbols)
    invalid = symbols - set(SYMBOLS)
    if invalid:
        raise ValueError("invalid symbols: {}".format(invalid))
    if row >= SIZE or col >= SIZE:
        raise ValueError("coordinates out of range: ({}, {})".format(row, col))
    board[row][col] = symbols
    print("\nUPDATE: ({}, {}) -> {}".format(row, col, symbols))

def done(board: Board) -> bool:
    '''Returns True if all cells have only one available symbol left'''
    for row in board:
        for cell in row:
            if len(cell) > 1:
                return False
    return True

def parse_update(line: str) -> Tuple[int, int, List[Symbol]]:
    '''Reads a line in the format 'row,col:s1,s2,s3,...' and returns the tuple
    (row, col, symbols).'''
    coords, symbols = line.split(':')
    row, col = list(map(int, coords.split(',')))
    symbols = list(map(int, symbols.split(',')))
    return row, col, symbols

def resolve_board(board):
    '''Performs a single pass of analysis -> updates'''
    # TODO: ADD CODE HERE
    print('Not yet implemented')

def main():
    board = init_board()
    while not done(board):
        print('---')
        print(render_board(board))
        print("Provide a manual update ('row,col:s1,s2,s3,...') or '+' to resolve board")
        for line in sys.stdin:
            line = line.strip()
            if line == 'q':
                return
            elif line == '+':
                resolve_board(board)
                break
            else:
                try:
                    row, col, symbols = parse_update(line.strip())
                    update_cell(board, row, col, symbols)
                    break
                except Exception as e:
                    print("ERROR: failed to apply update: '{}': {}".format(line, e))

main()
