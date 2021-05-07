#Board fuction is here

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


board = [[" " for columns in range(3)] for rows in range(3)]


def print_board(my_board):
    for row in my_board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print("\n-------")


#Fuction to ask player if they want to move
def take_turn():
    count = 0
    player = 'X'

    for i in range(1):
        print_board(board)
        print("It's your turn," + player + ".Where would you like to move?")

        placed = int(input())

        placement = board[(placed - 1) // 3][(placed - 1) % 3]
        if placement == 'X' or placement == "O":
            print("That place is already filled.\nMove to which place?")
            continue
        board[(placed - 1) // 3][(placed - 1) % 3] = player


def take_turn2():
    count = 0
    player2 = 'O'

    for i in range(1):
        print_board(board)
        print("It's your turn," + player2 + ".Where would you like to move?")

        placed = int(input())

        placement = board[(placed - 1) // 3][(placed - 1) % 3]
        if placement == 'O' or placement == "X":
            print("That place is already filled.\nMove to which place?")
            continue
        board[(placed - 1) // 3][(placed - 1) % 3] = player2




def turn():
  for i in range(5):
    take_turn()
    take_turn2()

turn()