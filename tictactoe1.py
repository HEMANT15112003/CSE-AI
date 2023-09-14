# Initialize the board
board = [" " for _ in range(9)]

# Current player
current_player = "X"

# Game over flag
game_over = False

# Main game loop
while not game_over:
    # Display the board
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

    # Get the player's move
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    # Check if the chosen spot is empty
    if board[move] == " ":
        board[move] = current_player
    else:
        print("Invalid move. That spot is already taken.")
        continue

    # Check for a win
    if (
        (board[0] == board[1] == board[2] == current_player) or
        (board[3] == board[4] == board[5] == current_player) or
        (board[6] == board[7] == board[8] == current_player) or
        (board[0] == board[3] == board[6] == current_player) or
        (board[1] == board[4] == board[7] == current_player) or
        (board[2] == board[5] == board[8] == current_player) or
        (board[0] == board[4] == board[8] == current_player) or
        (board[2] == board[4] == board[6] == current_player)
    ):
        print(f"Player {current_player} wins!")
        game_over = True
    # Check for a tie
    elif " " not in board:
        print("It's a tie!")
        game_over = True

    # Switch players
    current_player = "O" if current_player == "X" else "X"
