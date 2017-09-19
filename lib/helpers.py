# -*- coding: utf-8 -*-
# ==============================================================================

# GENERAL-PURPOSE HELPER FUNCTIONS AND DATA STRUCTURES

# ==============================================================================

# We use a simple data structure to represent squares on the board through their
# (x,y) coordinates, the origin being at the top left of the board.
from collections import namedtuple
Square = namedtuple('Square', ['x', 'y'])

BOARD_SIZE = 8

# ==============================================================================

def is_board_valid(board):
    """
        Checks if a given board is square-shaped and of the right size

        Arguments:
        - board: board to check

        Return value: True if the board has the right number of rows and
        columns, False otherwise
    """
    n = len(board)
    if n != BOARD_SIZE:
        return False
    for row in board:
        if len(row) != n:
            return False
    return True

# ==============================================================================

def get_player_positions(board, color):
    """
        Searches for all pieces belonging to a given player.

        Arguments:
        - board: board to search
        - color: selected player ('b'/'w')

        Return value: a list of squares containing the selected player's pieces
    """
    positions = []
    n = len(board)
    for i in range(n):
        p = [Square(i,j) for j in range(n) if board[i][j].lower() == color]
        positions.extend(p)
    return positions

# ==============================================================================

def opposite(color):
    """
        Gives the opposite of a given color

        Arguments:
        - color: a color character ('b'/'w')

        Return value: a color character ('b'/'w')
    """
    if color=='b': return 'w'
    return 'b'

# ==============================================================================

def is_inside(z):
    """
        Checks if a given index is within the board

        Arguments:
        - z: index (x or y coordinate)

        Return value:
    """
    if (z >= 0) & (z < BOARD_SIZE):
        return True
    return False

# ==============================================================================
