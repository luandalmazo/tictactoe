import random

def choose_first(): #FUNCTION RESPONSIBLE FOR RANDOMLY DECIDE WHICH ONE WILL BE THE FIRST PLAYER
    verify = random.randint(0,1)
    if verify == 0:
            return 'Player 1'
    else:
            return 'Player 2'

def space_check (board, position): #FUNCTION RESPONSIBLE FOR CHECK THE POSITION
    return board[position] == ' '

def board_check(board): #FUNCTION RESPONSIBLE FOR CHECK IF THE BOARD IS ALREADY FULL
    for i in range (1,10):
        if space_check(board,i):
            return False

    return True

def player_choice (board): #FUNCTION RESPONSIBLE FOR DISPLAY, UNTIL THE BOARD IS FILLED, OF THE OPTION TO CHOOSE A POSITION
    position = 0
    while (position not in range(1,10)) or (not space_check(board,position)):
        position = int (input("Choose a position: (1-9) "))
    return position

def replay(): #FUNCTION RESPONSIBLE FOR ASK IF THE PLAYERS WOULD LIKE OTHER MATCH
    choice = input("Play again: Enter Y or N: ")
    return choice == 'Y'

def display_board(board): #FUNCTION RESPONSIBLE FOR DISPLAY THE ENTIRE BOARD
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')

def player_input(): #FUNCTION RESPONSIBLE FOR PROCESS THE PLAYER'S CHOICE
    marker = ''

    while (marker != 'X') and (marker!= 'O'):
        marker = input('PLAYER 1, CHOOSE X OR O: ')
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1,player2) #RETURN A TUPLE FOR FUTURE UNPACKING

def place_marker (board, marker, position): #FUNCTION RESPONSIBLE FOR MARK THE POSITION DIGITIZED BY THE PLAYER
    board[position] = marker

def win_check (board, mark): #FUNCTION RESPONSIBLE FOR LOGICAL TESTS TO VERIFY IF THE GAME ALREADY HAS A WINNER
    return ((board[1] == board[2] == board[3] == mark) or 
    (board[4] == board[5] == board[6] == mark) or 
    (board[7] == board[8] == board[9] == mark) or
    (board[2] == board[5] == board [8] == mark) or
    (board[1] == board [4] == board[7] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board [5] == board[7] == mark))

def game (): #THE CORE OF THE GAME, FUNCTION RESPONSIBLE TO LINK EVERY FUNCTION AND MAKE EVERYTHING WORK TOGETHER
    print('========== WELCOME MY FRIEND! ==========')

    while True:
        board = [' ']*10
        player1, player2 = player_input()
        turn = choose_first()
        print(turn + " will go first!")
        play=''
        while (play!= "Y" and play!= "y" and play!= "N" and play!= "n"):
            play = input("Ready to play? Y or N? ")

        if play == 'Y' or play == "y":
            game_still_on = True
        else:  
            game_still_on = False
            break

        while game_still_on:
            if turn == "Player 1":
                display_board(board)
                position = player_choice(board)
                place_marker(board,player1,position)
                if win_check(board,player1):
                    display_board(board)
                    print("PLAYER 1 HAS WON!!!!!")
                    game_still_on = False
                else:
                    if board_check(board):
                        display_board(board)
                        print("TIE GAME!!!!")
                        break
                    else:    
                        turn = "Player 2"
            else:
                display_board(board)
                position = player_choice(board)
                place_marker(board,player2,position)
                if win_check(board,player2):
                    display_board(board)
                    print("PLAYER 2 HAS WON!!!!!")
                    game_still_on = False
                else:
                    if board_check(board):
                        display_board(board)
                        print("TIE GAME!!!!")
                        break
                    else:    
                        turn = "Player 1"
        if not replay():
            break    

        
game()