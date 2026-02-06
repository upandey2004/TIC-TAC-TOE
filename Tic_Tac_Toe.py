def check_input(n):
    if(n.isdigit()):
        n=int(n)
        if(n>=1 and n<=9):
            return True
    return False

def win(board):
    # rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True

    #columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    #diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True 

def reset_board():
    return [[' ' for _ in range(3)] for _ in range(3)]      

def print_board(board):
    print("Current Board:")
    for row in board:
        for cell in row:
            print(cell, end="")
            if(cell!=row[-1]):
                print("|", end="")
        print()
        print("-" * 5)

def position_to_indices(position):
    position -= 1 
    row = position // 3
    col = position % 3
    return row, col
def is_position_taken(board, position):
    row, col = position_to_indices(position)
    return board[row][col] != ' '   

def make_move(board, position, player):
    row, col = position_to_indices(position)
    board[row][col] = player    

def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'

def get_player_move(player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if check_input(move):
            move = int(move)
            return move
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    board = reset_board()
    current_player = 'X'
    print_board(board)

    while True:
        move = get_player_move(current_player)
        if is_position_taken(board, move):
            print("Position already taken. Try again.")
            continue

        make_move(board, move, current_player)
        print_board(board)

        if win(board):
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        current_player = switch_player(current_player)

play_game()



