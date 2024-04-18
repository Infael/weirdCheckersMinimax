from checkers import Checkers, WHITE_PIECE, BLACK_PIECE


class AlphaBetaMinimax:
    def __init__(self):
       self.minimax_runs = 0

    def minimax(self, position: Checkers, depth, alpha, beta, maximizing_player):
        self.minimax_runs += 1
        if depth == 0 or position.game_over:
            return self.evaluate_position(position), None
        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in position.get_valid_moves():
                new_position = position.deep_copy()
                new_position.move(move[0], move[1])
                evaluation = self.minimax(new_position, depth - 1, alpha, beta, False)[0]
                if max_eval < evaluation:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in position.get_valid_moves():
                new_position = position.deep_copy()
                new_position.move(move[0], move[1])
                evaluation = self.minimax(new_position, depth - 1, alpha, beta, True)[0]
                if min_eval > evaluation:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval, best_move


    
    def evaluate_position(self, position: Checkers):
        # number of possible moves of black player
        # number_of_black_moves = 0

        # for i in range(8):
        #     for j in range(8):
        #         if position.board[i][j] == BLACK_PIECE:
        #           number_of_black_moves += len(position.get_valid_moves_for_piece((i, j)))
        
        # return number_of_black_moves
        
        white_pieces = 0
        black_pieces = 0
        for i in range(8):
          for j in range(8):
            if position.board[i][j] == WHITE_PIECE:
              white_pieces += 1
            elif position.board[i][j] == BLACK_PIECE:
              black_pieces += 1
        if white_pieces == 0:
          return 1000
        elif black_pieces == 0:
          return -1000
        else:
          return black_pieces - white_pieces     
    

