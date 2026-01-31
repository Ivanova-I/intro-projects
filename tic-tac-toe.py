def print_board(board: list[list[str]]) -> None:
    for row in board:
        print(" | " + " | ".join(f" {cell} " for cell in row) + " |")

def check_for_winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print_board(board)
            print(f"Player with sign '{board[i][0]}' wins!")
            exit()
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print_board(board)
            print(f"Player with sign '{board[0][i]}' wins!")
            exit()

    if board[0][0] == board[1][1] == board[2][2] != " ":
        print_board(board)
        print(f"Player with sign '{board[0][0]}' wins!")
        exit()
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print_board(board)
        print(f"Player with sign '{board[0][2]}' wins!")
        exit()

    if all(cell != " " for row in board for cell in row):
        print_board(board)
        print("The game is a draw!")
        exit()


player_name_1 = input("Enter your name: ")
player_name_2 = input("Enter your name: ")
print(f"Welcome {player_name_1} and {player_name_2} to Tic Tac Toe!")
player_1_sign = input(f"{player_name_1 } enter the sign you choose 'X' or 'O': ").upper()

while player_1_sign not in ('X', 'O'):
    print("Invalid sign! Please choose either 'X' or 'O'.")
    player_1_sign = input(f"{player_name_1 } enter the sign you choose 'X' or 'O': ").upper()

player_2_sign = 'O' if player_1_sign == 'X' else 'X'
print(f"{player_name_1} will play as '{player_1_sign}' and {player_name_2} will play as '{player_2_sign}'.")

print("This is the numeration of the board positions:")
print(" 1 | 2 | 3 ")

print(" 4 | 5 | 6 ")

print(" 7 | 8 | 9 ")

print("Let's start the game!")
print(f"{player_name_1}, you go first.")

turn = 1
board = [[" " for _ in range(3)] for _ in range(3)]
mapp = {1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
       }

while True:
    current_player = player_name_1 if turn  % 2 != 0 else player_name_2
    current_sign = player_1_sign if turn  % 2 != 0 else player_2_sign

    try:
        position = int(input(f"{current_player}, enter the position (1-9) where you want to place your '{current_sign}': "))
        print(f"{current_player} placed '{current_sign}' on position {position}.")
    except ValueError:
        print("Invalid number! Please enter a number between 1 and 9.")
        continue

    if not 1 <= position <= 9:
        print("Invalid position! Please choose a position between 1 and 9.")
        continue
    row, col = mapp[position]
    if board[row][col] != " ":
        print("Position already taken! Please choose another position.")
        continue

    board[row][col] = current_sign
    if turn >= 5:
        check_for_winner(board)

    turn += 1
    print_board(board)