# Tic Tac Toe Game

# Defines a game board
import random

player_symbol = "X"
computer_symbol = "0"
empty_symbol = "-"
draw_symbol = "!"

# board = [" " for x in range(19)]
board = "-"*20

# Returns the game board with the icons/move from player and computer
def print_board(board):
    print(board)


def move(board, mark, pos):
    board = board[:pos] + mark + board[pos+1:]
    return board

def player_move(board):
    print("Your turn player {}".format(player_symbol))
    while True:
      choice = int(input("Enter your move (Numbers from 0-19): ").strip())
      if board[choice] == "-":
          return move(board, player_symbol, choice)
      else:
          print()
          print("That space is occupied! Try again!")

def computer_move(board):
    print("Your turn computer {}".format(computer_symbol))

    while True:
        index = random.randint(0, 18)
        if board[index] == "-":
            return move(board, computer_symbol, index)


# Defines the icon-winningpositions/opportunities
def evaluate(board):
    if board.find(player_symbol*3) != -1:
        return player_symbol

    if board.find(computer_symbol*3) != -1:
        return computer_symbol

    if board.find(empty_symbol) == -1:
        return draw_symbol

    return empty_symbol


while True:
    print_board(board)
    board = player_move(board)
    print_board(board)
    if evaluate(board) == player_symbol:
        print("X wins! Congratulations!")
        break

# print("Draw!")
# break
    board = computer_move(board)
    print_board(board)
    if evaluate(board) == computer_symbol:
        print("Computer wins! Congratulations!")
        break
    elif evaluate(board) == draw_symbol:
        print("Draw!")
        break
