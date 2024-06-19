player_1_simbol = 1
player_2_simbol = 2

game_state = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

'''
  output:
    [0 0 0]
    [0 0 0]
    [0 0 0]

    OR

    [1 0 0]
    [0 1 0]
    [0 2 1]
'''
def print_game_state(game_matrix: list[list]) -> None:
  for row in game_matrix:
    print('[', end='')
    for element in row:
      print(element, end=' ')
    print(']')


def check_box(game_matrix, line_number, col_number, marker):
  row = game_matrix[line_number]
  row[col_number] = marker

def moves():
  row = int(input('Choose row 0, 1, 2: '))
  col = int(input('Choose collumn 0, 1, 2: '))
  return row, col
  if int(input) < 2:
    return print('This is an invalid number')

def valid_moves(game_matrix, row, col):
  return 0 <= row < 3 and 0 <=col < 3 and game_matrix[row][col] == 0


def player_move(game_matrix, player, row, col):
  game_matrix[row][col] = player


def is_final_state(game_matrix):
  for row in game_matrix:
    if row[0] == row[1] and row[1] == row[2]:
      return True 
  for collumn in range (0,2):
    if game_matrix[0][collumn] == game_matrix[1][collumn] and game_matrix[1][collumn] == game_matrix[2][collumn]:
      return True
  if game_matrix[0][0] == game_matrix[1][1] and game_matrix[1][1] == game_matrix[2][2]:
    return True
  if game_matrix[0][2] == game_matrix[1][1] and game_matrix[1][1] == game_matrix[2][0]:
    return True
  
'''
- create a game loop checking if its not a final state
- create Round system saying if it's time for player 1/2 to play.
- Ask the Player 1/2 in which coordinate to mark (It cannot be already marked)
- Find a way to display who won the game (Player 1/2 Won!)
'''

print_game_state(game_state)