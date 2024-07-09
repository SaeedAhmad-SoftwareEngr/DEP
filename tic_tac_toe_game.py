import os

def clear_console():
    """Clears the console for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Prints the current state of the board."""
    clear_console()
    for row in range(3):
        print(" " + " | ".join(board[row]))
        if row < 2:
            print("---|---|---")

def check_winner(board, player):
    """Checks if the specified player has won the game."""
    for i in range(3):
        if all([spot == player for spot in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    return all([spot != ' ' for row in board for spot in row])

def minimax(board, depth, is_maximizing):
    """Minimax algorithm to determine the best move for the computer."""
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def computer_move(board):
    """Determines and makes the best move for the computer."""
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

def user_move(board):
    """Handles the user's move."""
    valid_move = False
    while not valid_move:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            else:
                row, col = divmod(move, 3)
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    valid_move = True
                else:
                    print("Invalid move. The cell is already occupied.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        user_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        computer_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
