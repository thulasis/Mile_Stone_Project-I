# STEP-I Creating a user interacting board
# a raw Tic Tac Toe game
# function-1
import random
from IPython.display import clear_output

def display_board(board):
    # using print function to make a board
    clear_output()

    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])

#Step II: Creating a function to assign user input
# function-2
def player_input():
    
    marker = ''
    #Ask Player to choose X or O
    
    while marker != 'X' and marker != 'O':
        marker = input('Player1, please choose X or O: ')
    
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return (player1, player2) 
    
#Step III: Assigning X or O to board numbers
#function-3 - positioning of marker
def place_marker(board, marker, position):
    board[position] = marker

#Step IV: Function win Check.. check who is the winner
#function-4
def win_check(board,marker):
    # this function is checking marker across all the directions
    
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # across the top
    (board[4] == marker and board[5] == marker and board[6] == marker) or # across the middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or # across the bottom
    (board[7] == marker and board[4] == marker and board[1] == marker) or # down the middle
    (board[8] == marker and board[5] == marker and board[2] == marker) or # down the middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or # down the right side
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal
    
#Step V: Program to decide which player will start first

def first_play():
    if random.randint(0,1) == 0:
        return 'Player2'
    else:
        return 'Player1'

# function-7 for checking free cells
def free_cells(board,position):
    return board[position] == ' '
    
#function-8 -check for fullboard  
def full_board_check(board):
   for i in range(1,10):
       if free_cells(board,i):
           return False
   return True
   
#function-9 player choosing the position   
def player_choice(board):
   position = 0
    
   while position not in [1,2,3,4,5,6,7,8,9] or not free_cells(board, position):
       position = int(input('Choose your next position: (1-9) '))
        
   return position

#function-10 replay function
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#Executing the main game

print ('Welcome to interactive Tic Tac Toe !!!')

while True:
    
    new_board = [' ']*10
    
    turn = first_play()
    
    print(turn + ' will go first.')
    
    print ('Its program decision')
    
    
    player1_marker, player2_marker = player_input()
    
    
    #choosing the turn
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    # while game goes on
    while game_on:
        if turn == 'Player1':
            
            print ('Player1 Turn')
            
            display_board(new_board)
            position = player_choice(new_board)
            place_marker(new_board, player1_marker, position)
                
            if win_check(new_board,player1_marker):
                display_board(new_board)
                print ('Congratulations!!! Player1 Won!!!')
                game_on = False
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('The game is a draw!!!')
                    break
                else:
                    turn = 'Player2'
                    print ('Player2 Turn')
                        
            # loop goes on 
        else:
            # player2's turn
            print ('Player2 Turn')
            
            display_board(new_board)
            position = player_choice(new_board)
            place_marker(new_board, player2_marker, position)
                
            if win_check(new_board,player2_marker):
                display_board(new_board)
                print ('Player2 won!!! Congrats!!')
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player1'
                    print ('Player1 Turn')
        
        ## terminating the game       
                
    if not replay():
        break
