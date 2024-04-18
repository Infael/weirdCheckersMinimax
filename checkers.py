
BLACK_PIECE = '🔴'
WHITE_PIECE = '🔵'
EMPTY = '⬛'
EMPTY_UNACCESSIBLE = '⬜'

class Checkers:
  def __init__(self):
    self.board = []
    self.turn = 'W'
    self.game_over = False
    self.init_board()

  def init_board(self):
    self.board = [[EMPTY_UNACCESSIBLE if i % 2 == 0 else EMPTY for i in range(8)] if j % 2 == 0 else [EMPTY if i % 2 == 0 else EMPTY_UNACCESSIBLE for i in range(8)] for j in range(8)]

  def add_white_pieces(self, pieces_positions):
    for pos in pieces_positions:
      self.board[pos[0]][pos[1]] = WHITE_PIECE

  def add_black_pieces(self, pieces_positions):
    for pos in pieces_positions:
      self.board[pos[0]][pos[1]] = BLACK_PIECE

  def print_board(self):
    for i in range(8):
      print(''.join(self.board[i]))
      
  def move(self, start, end):
    color = self.board[start[0]][start[1]]
    self.turn = 'B' if self.turn == 'W' else 'W'
    # jump 
    if abs(start[0] - end[0]) == 2:
      self.board[start[0]][start[1]] = EMPTY
      self.board[(start[0] + end[0]) // 2][(start[1] + end[1]) // 2] = EMPTY
      self.board[end[0]][end[1]] = color
      self.is_game_over()
      return

    self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
    self.board[start[0]][start[1]] = EMPTY


  def get_valid_moves_for_piece(self, piece_pos):
    valid_moves = []
    piece_color = self.board[piece_pos[0]][piece_pos[1]]

    # left up
    left_up = (piece_pos[0] - 1, piece_pos[1] - 1)
    if left_up[0] >= 0 and left_up[1] >= 0 and left_up[0] < 8 and left_up[1] < 8:
      if self.board[left_up[0]][left_up[1]] == EMPTY:
        valid_moves.append(left_up)
      elif self.board[left_up[0]][left_up[1]] != piece_color:
        if left_up[0] - 1 >= 0 and left_up[1] - 1 >= 0 and left_up[0] - 1 < 8 and left_up[1] - 1 < 8:
          if self.board[left_up[0] - 1][left_up[1] - 1] == EMPTY:
            valid_moves.append((left_up[0] - 1, left_up[1] - 1))
    # right up
    right_up = (piece_pos[0] - 1, piece_pos[1] + 1)
    if right_up[0] >= 0 and right_up[1] >= 0 and right_up[0] < 8 and right_up[1] < 8:
      if self.board[right_up[0]][right_up[1]] == EMPTY:
        valid_moves.append(right_up)
      elif self.board[right_up[0]][right_up[1]] != piece_color:
        if right_up[0] - 1 >= 0 and right_up[1] + 1 >= 0 and right_up[0] - 1 < 8 and right_up[1] + 1 < 8:
          if self.board[right_up[0] - 1][right_up[1] + 1] == EMPTY:
            valid_moves.append((right_up[0] - 1, right_up[1] + 1))
    # left down
    left_down = (piece_pos[0] + 1, piece_pos[1] - 1)
    if left_down[0] >= 0 and left_down[1] >= 0 and left_down[0] < 8 and left_down[1] < 8:
      if self.board[left_down[0]][left_down[1]] == EMPTY:
        valid_moves.append(left_down)
      elif self.board[left_down[0]][left_down[1]] != piece_color:
        if left_down[0] + 1 >= 0 and left_down[1] - 1 >= 0 and left_down[0] + 1 < 8 and left_down[1] - 1 < 8:
          if self.board[left_down[0] + 1][left_down[1] - 1] == EMPTY:
            valid_moves.append((left_down[0] + 1, left_down[1] - 1))
    # right down
    right_down = (piece_pos[0] + 1, piece_pos[1] + 1)
    if right_down[0] >= 0 and right_down[1] >= 0 and right_down[0] < 8 and right_down[1] < 8:
      if self.board[right_down[0]][right_down[1]] == EMPTY:
        valid_moves.append(right_down)
      elif self.board[right_down[0]][right_down[1]] != piece_color:
        if right_down[0] + 1 >= 0 and right_down[1] + 1 >= 0 and right_down[0] + 1 < 8 and right_down[1] + 1 < 8:
          if self.board[right_down[0] + 1][right_down[1] + 1] == EMPTY:
            valid_moves.append((right_down[0] + 1, right_down[1] + 1))
    return valid_moves
  

  def get_valid_moves(self):
    valid_moves = []
    for i in range(8):
      for j in range(8):
        if self.board[i][j] == WHITE_PIECE and self.turn == 'W':
          valid_moves += [((i, j), move) for move in self.get_valid_moves_for_piece((i, j))]
        elif self.board[i][j] == BLACK_PIECE and self.turn == 'B':
          valid_moves += [((i, j), move) for move in self.get_valid_moves_for_piece((i, j))]
    return valid_moves
  

  def is_game_over(self):
    white_pieces = 0
    black_pieces = 0
    for i in range(8):
      for j in range(8):
        if self.board[i][j] == WHITE_PIECE:
          white_pieces += 1
        elif self.board[i][j] == BLACK_PIECE:
          black_pieces += 1
    if white_pieces == 0 or black_pieces == 0:
      self.game_over = True
      return True
    return False


  def deep_copy(self):
    new_game = Checkers()
    new_game.board = [row[:] for row in self.board]
    new_game.turn = self.turn
    new_game.game_over = self.game_over
    return new_game