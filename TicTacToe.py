import os
from ask_user import ask_user as a_s
from random import randint, randrange  
from time import sleep

#initialising the board
class Board:
    def __init__(self):
        self.boxs = [' '] * 10

    def display(self):
        print(f' {self.boxs[1]}  |  {self.boxs[2]}  |  {self.boxs[3]} \n---------------')
        print(f' {self.boxs[4]}  |  {self.boxs[5]}  |  {self.boxs[6]} \n---------------')
        print(f' {self.boxs[7]}  |  {self.boxs[8]}  |  {self.boxs[9]} ')

    def update_box(self, box_num, key):
        def valid_position(box_num, key):
            min_box, max_box = 0 , 10
            return min_box < box_num < max_box and self.boxs[box_num] == ' '
        while not valid_position(box_num, key):
            box_num = a_s("Please enter a valid position: ", int)
        self.boxs[box_num] = key
   
    def win_solution(self,boxs,key):
        if (self.boxs[1] == key and self.boxs[2] == key and self.boxs[3] == key) or\
            (self.boxs[4] == key and self.boxs[5] == key and self.boxs[6] == key) or\
            (self.boxs[7] == key and self.boxs[8] == key and self.boxs[9] == key) or\
            (self.boxs[1] == key and self.boxs[4] == key and self.boxs[7] == key) or\
            (self.boxs[2] == key and self.boxs[5] == key and self.boxs[8] == key) or\
            (self.boxs[3] == key and self.boxs[6] == key and self.boxs[9] == key) or\
            (self.boxs[1] == key and self.boxs[5] == key and self.boxs[9] == key) or\
            (self.boxs[3] == key and self.boxs[5] == key and self.boxs[7] == key):
            return True
        else:
            return False
        
    def ai_win_sol(self,boxs):
        global box_num
        box_num = 0
        #horizontal
        if ((self.boxs[1] == self.boxs[2] != ' ') and self.boxs[3] == ' '):
            box_num = 3
            
        elif ((self.boxs[4] == self.boxs[5] != ' ') and self.boxs[6] == ' '):
            box_num = 6
            
        elif ((self.boxs[7] == self.boxs[8] != ' ') and self.boxs[9] == ' '):
            box_num = 9
            
        elif ((self.boxs[1] == self.boxs[3] != ' ') and self.boxs[2] == ' '):
            box_num = 2
            
        elif ((self.boxs[4] == self.boxs[6] != ' ') and self.boxs[5] == ' '):
            box_num = 5
            
        elif ((self.boxs[7] == self.boxs[9] != ' ') and self.boxs[8] == ' '):
            box_num = 8
            
        elif ((self.boxs[2] == self.boxs[3] != ' ') and self.boxs[1] == ' '):
            box_num = 1
            
        elif ((self.boxs[5] == self.boxs[6] != ' ') and self.boxs[4] == ' '):
            box_num = 4
            
        elif ((self.boxs[8] == self.boxs[9] != ' ') and self.boxs[7] == ' '):
            box_num = 7
            
        #vertical
        elif ((self.boxs[1] == self.boxs[4] != ' ') and self.boxs[7] == ' '):
            box_num = 7
            
        elif ((self.boxs[2] == self.boxs[5] != ' ') and self.boxs[8] == ' '):
            box_num = 8
            
        elif ((self.boxs[3] == self.boxs[6] != ' ') and self.boxs[9] == ' '):
            box_num = 9
            
        elif ((self.boxs[1] == self.boxs[7] != ' ') and self.boxs[4] == ' '):
            box_num = 4
            
        elif ((self.boxs[2] == self.boxs[8] != ' ') and self.boxs[5] == ' '):
            box_num = 5
            
        elif ((self.boxs[3] == self.boxs[9] != ' ') and self.boxs[6] == ' '):
            box_num = 6
            
        elif ((self.boxs[4] == self.boxs[7] != ' ') and self.boxs[1] == ' '):
            box_num = 1
            
        elif ((self.boxs[6] == self.boxs[9] != ' ') and self.boxs[3] == ' '):
            box_num = 3
            
        elif ((self.boxs[5] == self.boxs[8] != ' ') and self.boxs[2] == ' '):
            box_num = 2
            
        #Cross
        elif ((self.boxs[1] == self.boxs[5] != ' ') and self.boxs[9] == ' '):
            box_num = 9
            
        elif ((self.boxs[1] == self.boxs[9] != ' ') and self.boxs[5] == ' '):
            box_num = 5
            
        elif ((self.boxs[5] == self.boxs[9] != ' ') and self.boxs[1] == ' '):
            box_num = 1
            
        elif ((self.boxs[3] == self.boxs[5] != ' ') and self.boxs[7] == ' '):
            box_num = 7
            
        elif ((self.boxs[5] == self.boxs[7] != ' ') and self.boxs[3] == ' '):
            box_num = 3
            
        elif ((self.boxs[7] == self.boxs[3] != ' ') and self.boxs[5] == ' '):
            box_num = 5
        else:
            box_num = 0
        return box_num
        
    def tie_game(self):
        count = 0
        for i in self.boxs:
            if i != ' ':
                count += 1
        return count == 9   

    def reset_board(self):
        self.boxs = [' '] * 10

board = Board()

def select_number(board_ai):
    global r
    ln = len(board_ai)
    r = randrange(0 ,ln)
    return board_ai[r]

def comp_auto_move():
    available_move = [x for x, letter in enumerate(board.boxs) if letter == ' ' and x != 0]
    select_number(available_move)
    board.boxs[r] = 'O'
m = 0
#Introduction 
def clear_screen():
    os.system('clear')
    print('Welcome to the TicTacToe simulator')
    
    global m
    if m == 0:
        print('Assign youselves as "X" or "O"')
        m += 1
        print('3......') ; sleep(1)
        print('2......') ; sleep(1)
        print('1......') ; sleep(1)

    #Displays the board
    board.display()

def clear_screen_ai():
    os.system('clear')
    print('Welcome to the TicTacToe simulator')
    
    global m
    if m == 0:
        print('You are "X", Computer is "0"')
        m += 1
        print('3......') ; sleep(1)
        print('2......') ; sleep(1)
        print('1......') ; sleep(1)

    #Displays the board
    board.display()
#To let the user choose either single or multiplayer
def choice_game():
    while True:
        global choice
        os.system('clear')
        print('Welcome to the TicTacToe simulator')
        choice = a_s('Press 1 for Multiplayer\nPress 2 for Single Player: ',int)
        if 0 < choice < 3:
            break
        else:
            print("Enter 1 or 2 only")
            continue

while True:
    choice_game()
#Multiplayer
    if choice == 1:
        turn = randint(0,1)
        while True:
            if turn == 1:
                #Updates the board after input
                clear_screen()

                #For X Player
                x_move = a_s('X, Choose a position between 1 - 9 : ',int)

                #Put x input into the board
                board.update_box(x_move, "X")
                turn = 0
                #Updates the board after input
                clear_screen()
                #Check for win for X or tie
                if board.win_solution(board.boxs,"X"):
                    print('Congrats, X you have won')
                    turn = 3
                elif board.tie_game():
                    print('This is a tie game')
                    turn = 3

            elif turn == 0: 
                clear_screen()
                #For O Player
                o_move = a_s('O, Choose a position between 1 - 9 : ',int)
                #Put o input into the board
                board.update_box(o_move, "O")
                turn = 1
                #Updates the board after input
                clear_screen()

                #Check for win for O or tie
                if board.win_solution(board.boxs,"O"):
                    print('Congrats, O you have won')
                    turn = 3
                elif board.tie_game():
                    print('This is a tie game')
                    turn = 3

            else:
                while True:
                    p_again = a_s('Do you want to play again? (Y/N) : ').upper()
                    if p_again == "Y":
                        board.reset_board()
                        turn = randint(0,1)
                        m = 0
                        break
                    elif p_again == "N":
                        exit('Game is over')
                    else:
                        continue
                break
#Single Player
    else:
        turn = randint(0,1)
        while True:
            if turn == 1:
                #Updates the board after input
                clear_screen_ai()
                #For X Player
                x_move = a_s('X, Choose a position between 1 - 9 : ',int)
                #Put x input into the board
                board.update_box(x_move, "X")
                turn = 0
                #Updates the board after input
                clear_screen_ai()
                box_num = 0
                #Check for win for X or tie
                if board.win_solution(board.boxs,"X"):
                    print('Congrats, X you have won')
                    turn = 3
                elif board.tie_game():
                    print('This is a tie game')
                    turn = 3

            elif turn == 0: 
                clear_screen_ai()
                board.ai_win_sol(board.boxs)
                if box_num != 0:
                    board.boxs[box_num] = 'O'
                else:  
                    comp_auto_move()
                turn = 1
                
                #Updates the board after input
                clear_screen_ai()
                #Check for win for O or tie
                if board.win_solution(board.boxs,"O"):
                    print('You lose to the AI')
                    turn = 3
                elif board.tie_game():
                    print('This is a tie game')
                    turn = 3

            else:
                while True:
                    p_again = a_s('Do you want to play again? (Y/N) : ').upper()
                    if p_again == "Y":
                        board.reset_board()
                        turn = randint(0,1)
                        m = 0
                        break
                    elif p_again == "N":
                        exit('Game is over')
                    else:
                        continue
                break