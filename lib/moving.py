# FUNCTIONS MANAGING THE MOVING MECHANISMS

# ==============================================================================

from helpers import BOARD_SIZE, is_inside, Square

# ==============================================================================

def get_moves(square, board):
    """
        Searches for all possible non-capturing moves available to a given piece

        Arguments:
        - square: starting position
        - board: current board

        Return value: a list of available moves where each element is itself a
        list containing a source square and a destination square
    """
    piece = board[square.x][square.y]
    if piece in ['W','B']:
        return get_black_moves(square, board) + get_white_moves(square, board)
    if piece == 'w':
        return get_white_moves(square, board)
    if piece == 'b':
        return get_black_moves(square, board)
    return None

# ==============================================================================

def single_move(square, board, direction, side):
    """
        Checks if a piece can perform a non-capturing move in a given side and
        direction

        Arguments:
        - square: starting square
        - board: current board
        - direction: 'forward'/'backward'
        - side: 'left'/'right'

        Return value: a destination square if a move can be performed, otherwise
        None
    """
    d = -1 if direction == 'backward' else 1
    s = -1 if side == 'left' else 1

    color = board[square.x][square.y].lower()

    if is_inside(square.x + d) & is_inside(square.y + s):
        # square is within the board
        if (board[square.x + d][square.y + s] == '_'):
            # square is inside and empty => move possible
            # latest condition is moved because it is evaluated even though
            # previous ones are false
            return Square(square.x + d, square.y + s)
    return None

# ==============================================================================

def get_black_moves(square, board):
    """
        Searches for available non-capturing moves to a black disc

        Arguments:
        - square: starting position
        - board: current board

        Return value: a list available moves, where each element is a list of
        source and destination squares
    """
    moves = []

    check_left = single_move(square, board, direction='forward', side='left')
    if check_left:
        moves.append([square, check_left])

    check_right = single_move(square, board, direction='forward', side='right')
    if check_right:
        moves.append([square, check_right])

    return moves

# ==============================================================================

def get_white_moves(square, board):
    """
        Searches for available non-capturing moves to a white disc

        Arguments:
        - square: starting position
        - board: current board

        Return value: a list available moves, where each element is a list of
        source and destination squares
    """
    moves = []

    check_left = single_move(square, board, direction='backward', side='left')
    if check_left:
        moves.append([square, check_left])

    check_right = single_move(square, board, direction='backward', side='right')
    if check_right:
        moves.append([square, check_right])

    return moves

# ==============================================================================
