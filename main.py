# HERE IS MY TIC-TAC-TOE GAME GAME SOURCE CODE

# Step 1:
#  Write a function that can print out a board.
#  Set up your board as a list, where each index 1-9 corresponds with a number on a number pad

import random


def display_board(board):
    print('   |     |')
    print(' ' + board[7] + ' | ' + ' ' +
          board[8] + ' ' + ' | ' + ' ' + board[9])
    print('   |     |')
    print('------------')

    print('   |     |')
    print(' ' + board[4] + ' | ' + ' ' +
          board[5] + ' ' + ' | ' + ' ' + board[6])
    print('   |     |')
    print('------------')

    print('   |     |')
    print(' ' + board[1] + ' | ' + ' ' +
          board[2] + ' ' + ' | ' + ' ' + board[3])
    print('   |     |')


# STEP 2 :
#  Write a function that can take in a player input and assign their marker as 'X' or 'O'.


def player_input():
    marker = ''
    while marker not in ('X', 'O'):
        marker = input("Plyer 1 : Do you want to be X or O : ").upper()
        if marker not in ('X', 'O'):
            print("Enter X or O ")
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

# STEP 3 :
# Write a function that takes in the board list object
#  a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.


def place_marker(board, marker, position):
    board[position] = marker

# STEP 4 :
# Write a function that takes in a board and checks to see if someone has won.


def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

# STEP 5 :
# write a function that uses the random module to randomly decide who goes first


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# STEP 6 :
# Write a function that returns a boolean indicating whether a space on the board is freely available.


def space_check(board, position):
    return board[position] == ' '

# STEP 7 :
# Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    else:
        return True

# STEP 8 :
# Write a function that asks for a player's next position (as a number 1-9)
# And then uses the function from step 6 to check if its a free position.
# If it is, then return the position for later use.


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position (1-9) : "))
    return position

# STEP 9
# write a function that asks if the  player play again or not


def replay():
    return input("Do you want to play again ? Enter Yes or No : ").lower().startswith('y')


# STEP 10 :
# Here we use the while loop to run the game

print("WELCOME TO TIC-TAC-TOE-GAME ")
while True:
    board1 = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' Will go first')

    play_game = input("Are you ready to play? Enter Yes or No ")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board1)
            position = player_choice(board1)
            place_marker(board1, player1_marker, position)

            if win_check(board1, player1_marker):
                display_board(board1)
                print("Congratulation player 1 Won the game!!! ")
                game_on = False

            else:
                if full_board_check(board1):
                    display_board(board1)
                    print("The game is Draw ")
                    break
                else:
                    turn = 'Player 2'

        else:
            if turn == 'Player 2':
                display_board(board1)
                position = player_choice(board1)
                place_marker(board1, player2_marker, position)

                if win_check(board1, player2_marker):
                    display_board(board1)
                    print("Congratulation player 2 won the game!!! ")
                    game_on = False

                else:
                    if full_board_check(board1):
                        display_board(board1)
                        print("The game is Draw ")
                        break
                    else:
                        turn = 'Player 1'

    if not replay():
        break
