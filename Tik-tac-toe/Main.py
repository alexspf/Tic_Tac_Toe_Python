from Table import print_board
from Logic import check_winner, is_board_full, get_empty_cells, best_move
def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            row = int(input("Player X, enter the row (0, 1, or 2): "))
            col = int(input("Player X, enter the column (0, 1, or 2): "))
        else:
            row, col = best_move(board)
            print(f"Player O chooses row {row} and column {col}")

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()