from IPython.display import clear_output
import random


def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
 


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker
    return board



def win_check(board, mark):
    if board[7]==mark and board[8]==mark and board[9]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    elif board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[3]==mark and board[6]==mark and board[9]==mark:
        return True
    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return True
    else:
        return False



def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True




def player_choice(board):
    valid_number = False
    position_free = False
    while valid_number == False or position_free == False:
        position = input('Please enter a number (1-9):')
        if position.isdigit():
            if int(position) >= 1 and int(position) <= 9:
                valid_number = True
                if space_check(board, int(position)):
                    position_free = True
                    return int(position)
                else:
                    print('That position is not free')
                    position_free = False
            else:
                print('Please enter a valid number from 1-9')   
        else:
            print('Please enter a valid number from 1-9')
    

def replay():
    print('')
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



print("")
print("######################")
print("#  TIC TAC TOE GAME  #")
print("######################")
print("")

while True: 
	board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

	player1_mark, player2_mark = player_input()    
	turn = choose_first()
	print(turn + ' will go first.')

	game_on = True

	while game_on:
	    #Player 1 Turn
	    if turn == 'Player 1':
	        print('')
	        print("Player1's turn ({})".format(player1_mark))  
	        display_board(board)
	        position = player_choice(board)
	        board = place_marker(board, player1_mark, position)
	        if win_check(board, player1_mark):
	            print('')
	            print('PLAYER1 WON!')
	            display_board(board)
	            game_on = False
	            break
	        else:
	            turn = 'Player 2'
	    
	    # Player2's turn
	    if turn == 'Player 2':
	        print('')
	        print("Player2's turn ({})".format(player2_mark))    
	        display_board(board)
	        position = player_choice(board)
	        board = place_marker(board, player2_mark, position)
	        win_check(board, player2_mark)
	        if win_check(board, player2_mark):
	            print('')
	            print('PLAYER2 WON!')
	            display_board(board)
	            game_on = False
	            break
	        else:
	            turn = 'Player 1'
	    
	    if full_board_check(board):
	        print('')
	        print('IT WAS A TIE')
	        display_board(board)
	        game_on = False

	if not replay():
		break