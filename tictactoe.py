board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

for i in range (3):
  print(board[i])
  
charecters = ["X", "O"]
turn = 0
play_charecter = charecters[turn%2]

def determinespot(place):
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for number in numbers:
    if number == place:
      if number == 1:
        return [0, 0]
      if number == 2:
        return [0, 1]
      if number == 3:
        return [0, 2]
      if number == 4:
        return [1, 0]
      if number == 5:
        return [1, 1]
      if number == 6:
        return [1, 2]
      if number == 7:
        return [2, 0]
      if number == 8:
        return [2, 1]
      if number == 9:
        return [2, 2]
        
def check(p1, p2, p3, play_charecter):
  if board[p1[0]][p1[1]] != play_charecter:
    return False
  if board[p2[0]][p2[1]] != play_charecter:
    return False
  if board[p3[0]][p3[1]] != play_charecter:
    return False
  return True
  

while True:
  play_charecter = charecters[turn%2]
  place = int(input("Where do you want to place? 1 is top left, 9 is bottom right, and 7 is bottom left."))
  while place not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    place = input("invalid answer")
  spot = determinespot(place)
  while board[spot[0]][spot[1]] == play_charecter:
    place = input("You've already added it there.")
    spot = determinespot(place)
  while board[spot[0]][spot[1]] == charecters[(turn+1)%2]:
    place = input("There's one already there.")
    spot = determinespot(place)
  board[spot[0]][spot[1]] = play_charecter
  for i in range(3):
    print(board[i])
  turn += 1
  
  #row
  game_still_running = check([0, 0], [0, 1], [0, 2], play_charecter)
  if game_still_running == True:
    print(play_charecter + " won!")
    break
    
  if game_still_running == False:
    game_still_running = check([1, 0], [1, 1], [1, 2], play_charecter)
  else:
    print(play_charecter + " won!")
    break
  if game_still_running == False:
    game_still_running = check([2, 0], [2, 1], [2, 2], play_charecter)
  else:
    print(play_charecter + " won!")
    break
  
  #column
  if game_still_running == False:
    game_still_running = check([0, 0], [1, 0], [2, 0], play_charecter)
  else:
    print(play_charecter + " won!")
    break
  if game_still_running == False:
    game_still_running = check([0, 1], [1, 1], [2, 1], play_charecter)
  else:
    print(play_charecter + " won!")
    break
  if game_still_running == False:
    game_still_running = check([0, 2], [1, 2], [2, 2], play_charecter)
  else:
    print(play_charecter + " won!")
    break
  
  # diagonal
  if game_still_running == False:
    game_still_running = check([0, 0], [1, 1], [2, 2], play_charecter)
  else:
    print(play_charecter + " won!")
    break
  if game_still_running == False:
    game_still_running = check([0, 2], [1, 1], [2, 0], play_charecter)
  else:
    print(play_charecter + " won!")
    break

