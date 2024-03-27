import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def minimax(game, maximizing_player, alpha, beta):
    if game.current_winner is not None:
        if game.current_winner == 'X':
            return -1, None
        elif game.current_winner == 'O':
            return 1, None
        else:
            return 0, None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for move in game.available_moves():
            game.make_move(move, 'O')
            eval, _ = minimax(game, False, alpha, beta)
            game.board[move] = ' '
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move

    else:
        min_eval = math.inf
        best_move = None
        for move in game.available_moves():
            game.make_move(move, 'X')
            eval, _ = minimax(game, True, alpha, beta)
            game.board[move] = ' '
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def play_game():
    game = TicTacToe()
    game.print_board_nums()
    print("Start the game!")
    print("Positions are as follows:")
    game.print_board()
    print("\n")

    while game.empty_squares():
        if game.current_winner is None:
            if game.num_empty_squares() % 2 == 1:
                _, best_move = minimax(game, True, -math.inf, math.inf)
                game.make_move(best_move, 'O')
            else:
                _, best_move = minimax(game, False, -math.inf, math.inf)
                game.make_move(best_move, 'X')
        game.print_board()
        print("\n")

        if game.current_winner is not None:
            print("Player", game.current_winner, "wins!")
            break
        elif not game.empty_squares():
            print("It's a tie!")
            break

play_game()
