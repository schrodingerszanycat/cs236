import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    if board == initial_state():
        return X
    if terminal(board):
        return EMPTY
    x_count = 0
    o_count = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == X:
                x_count += 1
            if board[x][y] == O:
                o_count += 1

    if (isOdd(x_count) and isEven(o_count)) or (isEven(x_count) and isOdd(o_count)):
        return O
    else:
        return X

def actions(board):
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions

def result(board, action):
    new_board = deepcopy(board)
    i, j = action

    if (new_board[i][j] == EMPTY):
        new_board[i][j] = player(new_board)
    else:
        raise Exception
    return new_board

def winner(board):
    for row in board:
        if row == [O]*3:
            return O
        elif row == [X]*3:
            return X
    
    for i in range(3):
        column = [board[x][i] for x in range(3)]
        if column == [O]*3:
            return O
        elif column == [X]*3:
            return X

    d1 = [board[i][i] for i in range(3)]
    if d1 == [O]*3:
        return O
    elif d1 == [X]*3:
        return X
    
    d2 = [board[i][2-i] for i in range(3)]           
    if d2 == [O]*3:
        return O
    elif d2 == [X]*3:
        return X
    
    return None

def terminal(board):
    won = winner(board)
    if won is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True

def utility(board):
    won = winner(board)
    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0
    
def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    current_player = player(board)
    if terminal(board):
        return None
    
    if current_player == X:
        moves = []
        for action in actions(board):
            moves.append([min_value(result(board, action)), action])
        return sorted(moves, key=lambda x: x[0], reverse=True)[0][1] # returns the action
    else:
        moves = []
        for action in actions(board):
            moves.append([max_value(result(board, action)), action])
        return sorted(moves, key=lambda x: x[0])[0][1] # returns the action

def isOdd(num):
    return num % 2 != 0

def isEven(num):
    return num % 2 == 0