#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:40:07 2020

@author: Zuhairi Anuar
"""

# Our Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

### Is the game still ongoing?
game_ongoing = True


### First player starts with O.
current_player = "X"

#### Who's The winner?
winner = None

import random 


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

 ### What happens in every turn?
def player_move(player):
    print(player + "'s turn!")
   
    ### player X is us
    if player == 'X':
        position = input("Pick position 1-9: ")
    ### if the input not valid (1 to 9), ask for position again!
        if position not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            position = input("Pick position 1-9: ")
    ### Because the first position is in index 0! Thats why minus 1 and I must change the str to int.
        position = int(position)-1

    ## If the board is already occupied, I will print out the error message
    # and ask them to input again
        while board[position] == 'O' or board[position] == 'X':
            position = int(input("Pick position 1-9: "))-1
            break
        
        ### current player X or O will then be slot into the position.
        board[position] = player
        
    
    ### if not player X it is the computer
    else:
        ### to make sure the computer tries to put in the center.
        if board[4] == '-':
            board[4] = player
        
        else:
            ### if already occupied in the middle, they will generate a random position
            position = random.randrange(0,8)
        
        ### if computer generates a position that is occupied, will generate a random position again
            while board[position] == 'O' or board[position] == 'X':
                position = random.randrange(0,8)
           
            ### current player X or O will then be slot into the position
            board[position] = player
     
    #### Shows updated board
    display_board()
            

            
def winning_conditions():
    ### using check_win and check_tie to find winner
    
    check_win()
    check_tie()
    
    

    #### The player can win with rows, cols or diags.
def check_win():
    check_rows()
    check_columns()
    check_diagonals()
    
    ### Check if there are any winnings rows.
def check_rows():
    global game_ongoing
    global winner
    if board[0] == board[1] == board[2] != "-":
    ### This will tell if the game should stop cause' theres a winning row.
        game_ongoing = False
    ### I want to know the winner is X or O
        winner = board[0]
    elif board[3] == board[4] == board[5] != "-":
        game_ongoing = False
        winner = board[3]
    elif board[6] == board[7] == board[8] != "-":
        game_ongoing = False
        winner = board[6]
    else:
    ### If no winning row just return none.
        return None

def check_columns():
    global game_ongoing
    global winner
  ### This will tell if the game should stop cause' theres a winning col.
    if board[0] == board[3] == board[6] != "-":
        game_ongoing = False
  ### I want to know the winner is X or O
        winner = board[0]
    elif board[1] == board[4] == board[7] != "-":
        game_ongoing = False
        winner = board[1]
    elif board[2] == board[5] == board[8] != "-":
        game_ongoing = False
        winner = board[2]
    else:
    ### if no winning col just return none.
        return None
    
def check_diagonals():
    global game_ongoing
    global winner
    if board[0] == board[4] == board[8] != "-":
    ### This will tell if the game should stop cause' theres a winning diag.
        game_ongoing = False
    ### I want to know the winner is X or O
        winner = board[0]  
    elif board[6] == board[4] == board[2] != "-":
        game_ongoing = False
        winner = board[6]
    else:
    ### If no winning diag just return none.
        return None

def check_tie():
    global game_ongoing
    ### Once all the rows and cols are filled up obviously they won't be "-"
    if "-" not in board:
        game_ongoing = None


# switch O to X, or O to X.    
def switch_turns():
    global current_player
    ### if its O, make it X
    if current_player == "O":
        current_player = "X"
    ### if not make it O
    else:
        current_player = "O"
        
def game():
    ### start with the board
    display_board()
    ### this will only play if it is true
    while game_ongoing:
    ### prompt for player move
        player_move(current_player)
    ### check for any wins
        winning_conditions()
    ### then switch turns
        switch_turns()
    ### but if winner is changed from None to X or O,
    if winner == "X" or winner == "O":
    ### we get the winner!!
        print(winner + " won the game!")
    ### if not, its a tie.
    elif winner == None:
        print("Sadly, it's a tie!")
        
        
game()