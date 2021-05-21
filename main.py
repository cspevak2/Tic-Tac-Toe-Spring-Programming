#Board fuction is here

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


board = [[" " for columns in range(3)] for rows in range(3)]

"""This fuction prints our borad out using special keys and cells"""

def print_board(my_board):
    for row in my_board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print("\n-------")


#Fuction to ask player if they want to move
def take_turn(player):
    count = 0

    for i in range(1):
        
        print("It's your turn," + player + ".Where would you like to move?")

        placed = int(input())

        placement = board[(placed - 1) // 3][(placed - 1) % 3]
        if placement == 'X' or placement == "O":
            print("That place is already filled.\nMove to which place?")
            continue
        board[(placed - 1) // 3][(placed - 1) % 3] = player

def winner():
  #first row
  if board[0][0] == board[0][1]== board[0][2] != ' ':
    return board [0][0]
  #second row
  elif board[1][0] == board[1][1]== board[1][2] != ' ':
    return board[1][0]
  #thrid row
  elif board[2][0] == board[2][1]== board[2][2] != ' ':
    return board[2][0]
  #diagonal top left to bottom right
  elif board[0][0] == board[1][1]== board[2][2] != ' ':
    return board[0][0]
  #diagonal bottom left to top right
  elif board[2][0] == board[1][1]== board[0][2] != ' ':
    return board[2][0]
  #collum one 
  elif board[0][0] == board[1][0]== board[2][0] != ' ':
    return board[0][0]
  #collum two
  elif board[0][1] == board[1][1]== board[2][1] != ' ':
    return board[0][1]
  #collum three
  elif board[0][2] == board[1][2]== board[2][2] != ' ':
    return board[0][2]
    
def game():
  print_board(board)
  while winner() == None: 
    take_turn("X")
    print_board(board)
    if winner() != None:
      break
    take_turn("0")
    print_board(board)
  print("Congrats " + winner() + " Won!")

game()