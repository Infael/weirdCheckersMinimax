from checkers import Checkers
from minimax import AlphaBetaMinimax

def main():
  game = Checkers()
  game.add_black_pieces([(0, 1)])
  game.add_white_pieces([(2, 3), (3, 2)])

  # print(game.get_valid_moves())
  game.print_board()

  minimax = AlphaBetaMinimax()
  
  for _ in range(4):
    if game.game_over:
      break
    minimax.minimax_runs = 0
    # white is on move and black is maximizing player so the last argument is False first
    next_move = minimax.minimax(game, 6, float('-inf'), float('inf'), True if game.turn == 'B' else False)
    print(next_move)
    print('minimax runs:', minimax.minimax_runs)
    game.move(next_move[1][0], next_move[1][1])
    game.print_board()

  



if __name__ == '__main__':
  main()