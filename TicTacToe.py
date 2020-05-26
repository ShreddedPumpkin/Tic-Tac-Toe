import os
from AskUser import ask_user as As
from random import randint

#initialising the board
class Board():
    def __init__(self):
        self.boxs = [' '] * 10
    
    def display(self):
        print(f' {self.boxs[1]}  |  {self.boxs[2]}  |  {self.boxs[3]} \n---------------')
        print(f' {self.boxs[4]}  |  {self.boxs[5]}  |  {self.boxs[6]} \n---------------')
        print(f' {self.boxs[7]}  |  {self.boxs[8]}  |  {self.boxs[9]} ')

    def update_box(self, box_num, key):
        def valid_position(box_num, key):
            return 0 < box_num < 10 and self.boxs[box_num] == ' '
        while not valid_position(box_num, key):
            box_num = As("Please enter a valid position: ", int)
        self.boxs[box_num] = key
   
    def win_solution(self,key):
        if (self.boxs[1] == key and self.boxs[2] == key and self.boxs[3] == key) or\
            (self.boxs[4] == key and self.boxs[5] == key and self.boxs[6] == key) or\
            (self.boxs[7] == key and self.boxs[8] == key and self.boxs[9] == key) or\
            (self.boxs[1] == key and self.boxs[4] == key and self.boxs[7] == key) or\
            (self.boxs[2] == key and self.boxs[5] == key and self.boxs[8] == key) or\
            (self.boxs[3] == key and self.boxs[6] == key and self.boxs[9] == key) or\
            (self.boxs[1] == key and self.boxs[5] == key and self.boxs[9] == key) or\
            (self.boxs[3] == key and self.boxs[5] == key and self.boxs[7] == key):
            return True
        return False

    def tie_game(self):
        count = 0
        for i in self.boxs:
            if i != ' ':
                count += 1
        return count == 9   

    def reset_board(self):
        self.boxs = [' '] * 10

board = Board()
Turn = randint(0,1)

#Introduction 
def clear_screen():
    os.system('clear')
    print('Welcome to the TicTacToe simulator')
    #Displays the board
    board.display()


while True:
    if Turn == 1:
        #Updates the board after input
        clear_screen()

        #For X Player
        x_move = As('X, Choose a position between 1 - 9 : ',int)
        #Put x input into the board
        board.update_box(x_move, "X")
        Turn = 0
        #Updates the board after input
        clear_screen()
    #Check for win for X or tie
        if board.win_solution("X"):
            print('Congrats, X you have won')
            Turn = 3
        elif board.tie_game():
            print('This is a tie game')
            Turn = 3
        else:
            pass

    elif Turn == 0: 
        clear_screen()
        #For O Player
        o_move = As('O, Choose a position between 1 - 9 : ',int)
        #Put o input into the board
        board.update_box(o_move, "O")
        Turn = 1
        #Updates the board after input
        clear_screen()

        #Check for win for O or tie
        if board.win_solution("O"):
            print('Congrats, O you have won')
            Turn = 3
        elif board.tie_game():
            print('This is a tie game')
            Turn = 3
        else:
            pass

    else:
        p_again = As('Do you want to play again? (Y/N) : ').upper()
        if p_again == "Y":
            board.reset_board()
            Turn = randint(0,1)
            continue
        else:
            exit('Game is over')