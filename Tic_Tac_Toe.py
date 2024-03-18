
import sys
 

# boolean flag to determine current player
current = True

# original board state
board = [
    ["-","-","-"], 
    ["-","-","-"],
    ["-","-","-"]
]
# initializing winner to None
winner = None

# helper function to determine if there is a current winner
def check_for_winner(board):
    
    if board[0][0] == board[0][1] == board[0][2] and all(board[0][i] != "-" for i in range(3)):
        return board[0][0]
         
    if board[1][0] == board[1][1] == board[1][2] and all(board[1][i] != "-" for i in range(3)):
        return board[1][0]
         
    if board[2][0] == board[2][1] == board[2][2] and all(board[2][i] != "-" for i in range(3)):
        return board[2][0]
         
    if board[0][0] == board[1][0] == board[2][0] and all(board[i][0] != "-" for i in range(3)):
        return board[0][0]
         
    if board[0][1] == board[1][1] == board[2][1] and all(board[i][1] != "-" for i in range(3)):
        return board[0][1]
         
    if board[0][2] == board[1][2] == board[2][2] and all(board[i][2] != "-" for i in range(3)):
        return board[0][2]
         
    if board[0][0] == board[1][1] == board[2][2] and all(board[i][i] != "-" for i in range(3)): 
        return board[0][0]
         
    if board[2][0] == board[1][1] == board[0][2] and all(board[2 - i][i] != "-" for i in range(3)):
        return board[2][0]
         
    return False

title = """
*******************************
*    Welcome to Tic Tac Toe   *
*******************************
"""
print(title)        


# game loop
while True:
    # check if there is a winner
    check = check_for_winner(board)

    # if true - print the winner and exit game loop
    if check:
        winner = check
        print(board)
        print('\n')
        print(f"{winner} wins the game!!!")
        print('\n')
        break

    # print the board
    print('\n', board[0], '\n', board[1], '\n', board[2], '\n')
    player = "O" if current else "X"
    print(f"Its {player}'s turn") 
    print('\n')
    row = col = None

    # ask for user input as row and column
    try:
        data = input("Please enter your row and column position (1-3) as `row, column`:\n")
        print('\n')
        vals = data.split(",") 

        # verify the user input has 2 arguments
        if len(vals) != 2:
            raise ValueError("Invalid input format. Please enter row and column separated by a comma (e.g., 1,2)")
        row, col = int(vals[0]), int(vals[1])

        # make sure the row and column are valid
        if row <= 0 or row > len(board) or col <= 0 or col > len(board[0]):
            print('\n')
            print(f"{int(vals[0]),int(vals[1])} is not a valid position, please try again!")
            print('\n')
            continue
        # if the spot has not already been taken, update that position
        if board[row - 1][col - 1] == "-":
            board[row - 1][col - 1] = player
        else:
            print('\n')
            print("That position is already taken. Please enter another position!")
            continue
        current = not current 
    except ValueError:
        print('\n')
        print(f"That is not a valid position, please try again!")

    if 'Exit' == data:
        break
    
    