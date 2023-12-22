
class Board:
    def create_board():
        board = [[' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' ']]
        return board


# class Players:
#     def name_of_players(first_player, second_player):
#         str(input(f'Enter the name of player1 : {first_player}'))
#         str(input(f'Enter the name of player2 : {second_player}'))
#         # return player1, player2



# Create an empty board
game_board = Board.create_board()

# player1 = str(input(f'Enter the name of player1 : '))
# player2 = str(input(f'Enter the name of player2 : '))
player1 = 'CAS'
player2 = 'CB'


def play(player, player_symbol):
    print(f'{player}, indicate the coordonate of your play')
    row = int(input('Indicate the row : '))
    col = int(input('Indicate the column: '))
    game_board[row][col] = str(player_symbol)
    print(game_board)
    return game_board

# for turn in range(0,10):
#     turn = play(player1, 'X')
#     if game_board 
#     turn = play(player2, 'O')

 
game_board = [[' ', 'X', ' '],
              [' ', 'X', ' '],
              [' ', 'X', ' ']]

class WinConditions():
    def check_row(board, player_symbol):
        for row in board:
            if all(cell == player_symbol for cell in row):
                return True
            else: 
                return False

    def check_col(board, player_symbol):
        for col in board:
            if all(cell == player_symbol for cell in col):
                return True
            else:
                return False

    def check_diag(board, player_symbol):
        if all(board[i][i] == player_symbol for i in range(3)):
            return True
        elif all(board[2-i][i] == player_symbol for i in range(3)):
            return True
        else: 
            return False



# def wining(board, player_symbol):
#     if WinConditions.check_col(board, player_symbol) == True:
#         return True
#     else : 
#         return False

# print(WinConditions.check_col(game_board, 'X'))    

def check_col(board):
    for col in range(3):
        print(col)
        # if all(cell == player_symbol for cell in col):
        #     return True
        # else:
        #     return False

game_board = [[' ', 'X', ' '],
              [' ', 'X', ' '],
              [' ', 'X', ' ']]

print(check_col(game_board))