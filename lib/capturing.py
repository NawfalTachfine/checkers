# FUNCTIONS MANAGING THE CAPTURING MECHANISMS

# ==============================================================================

from helpers import *

# ==============================================================================

def get_captures(square, board):
    """
        Searches for possible capture targets from a given position on the board
        in all possible directions

        Arguments:
        - square: piece performing the capture
        - board: current board

        Return value: a list of squares reachable through a capture move
    """
    piece = board[square.x][square.y]
    if piece in ['W','B']:
        return get_black_captures(square, board) + get_white_captures(square, board)
    if piece == 'w':
        return get_white_captures(square, board)
    if piece == 'b':
        return get_black_captures(square, board)
    return None

# ==============================================================================

def single_capture(square, board, direction, side):
    """
        Searches for a (single) potential capture in a given direction
        (forward/backward) and a given side (left/right)

        Arguments:
        - square: piece performing the capture
        - board: current board
        - direction: either 'forward' or 'backward'
        - side: either 'left' or 'right'

        Return value: the target square when it is reachable through a capture,
        otherwise None

    """
    d = -1 if direction == 'backward' else 1
    s = -1 if side == 'left' else 1
    n = len(board)

    x = square.x
    y = square.y
    color = board[x][y].lower()

    if is_inside(x + 2*d) & is_inside(y + 2*s):
        # still within the board, can check for capture
        if (
            ( board[x + d][y + s].lower() == opposite(color) )
            &
            ( board[x + 2*d][y + 2*s] == '_' )
        ):
            # capture possible
            return Square(x + 2*d, y + 2*s)
        return None
    return None

# ==============================================================================

def get_black_captures(square, board):
    """
        Searches for capture moves available to a black disc

        Arguments:
        - board: current board
        - square: square holding the piece performing the captures

        Return value: a list of squares reachable by a black disc through a
        capture move
    """
    captures = []

    check_left = single_capture(square, board, direction='forward', side='left')
    if check_left:
        captures.append(check_left)

    check_right = single_capture(square, board, direction='forward', side='right')
    if check_right:
        captures.append(check_right)

    return captures

# ==============================================================================

def get_white_captures(square, board):
    """
        Searches for capture moves available to a white disc

        Arguments:
        - board: current board
        - square: current square holding the piece performing the captures

        Return value: a list of squares reachable by a white disc through a
        capture move
    """
    captures = []

    check_left = single_capture(square, board, direction='backward', side='left')
    if check_left:
        captures.append(check_left)

    check_right = single_capture(square, board, direction='backward', side='right')
    if check_right:
        captures.append(check_right)

    return captures

# ==============================================================================

def capture_piece(board, source, destination):
    """
        Performs a given capture move and alters the board accordingly

        Arguments:
        - board: the current board
        - source: the square of the capturing disc
        - destination: the square to be occupied after the capture

        Return value: the board resulting from the capture
    """
    n = len(board)
    color = board[source.x][source.y]

    # getting coordinates of captured piece
    direction = int((destination.x - source.x)/2)
    side = int((destination.y - source.y)/2)
    capture = Square(source.x + direction, source.y + side)

    # checking if capture is possible
    if (
        board[capture.x][capture.y].lower() != opposite(color.lower())
        or
        board[destination.x][destination.y] != '_'
    ):
        print('Impossible to capture! Check coordinates.')
        return ''

    # promoting disc to king if necessary
    promotion = False
    if ((destination.x == 0) & (color == 'w')):
        promotion = True
    if ((destination.x == n-1) & (color == 'b')):
        promotion = True
    piece = color.upper() if promotion else color

    # building updated board
    updated_board = board[:]
    updated_board = replace(updated_board, capture, '_')
    updated_board = replace(updated_board, source, '_')
    updated_board = replace(updated_board, destination, piece)

    return updated_board

# ==============================================================================

def get_capture_paths(square, board):
    """
        Searches for all possible capture paths starting from a given square

        Arguments:
        - board: current board
        - square: starting square

        Return value: a list of potential capture paths, where each path is a
        list of squares for the piece to visit, starting from its current
        position
    """
    active_nodes = [(square, board, [])]
    paths = []
    while active_nodes:
        origin_square, origin_board, origin_history = active_nodes.pop()
        candidates = get_captures(origin_square, origin_board)
        if candidates:
            for destination in candidates:
                new_board = capture_piece(
                    board = origin_board,
                    source = origin_square,
                    destination = destination )

                if is_board_valid(new_board):
                    active_nodes.append( (
                        destination,
                        new_board,
                        origin_history + [origin_square] ) )
        else:
            paths.append( origin_history + [origin_square] )
    return paths

# ==============================================================================

def replace(board, square, new):
    """
        Changes the content of a given square to a new given value

        Arguments:
        - board: current board
        - square: square to be changed
        - new: new value to occupy the square ('b', 'B', 'w', 'W', '_')

        Return value:
    """
    # getting around string immutability by using lists
    row = list(board[square.x]) # string to list
    row[square.y] = new
    updated_board = board[:] # forcing list copy instead of reference
    updated_board[square.x] = ''.join(row) # list to string

    return updated_board

# ==============================================================================
