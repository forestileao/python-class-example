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

print_game_state(game_state)
