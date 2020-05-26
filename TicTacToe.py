import os
from AskUser import ask_user as As
#initialising the board
class Board():
    def __init__(self):
        self.boxs = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    def display(self):
        print(f' {self.boxs[1]}  |  {self.boxs[2]}  |  {self.boxs[3]} \n---------------')
        print(f' {self.boxs[4]}  |  {self.boxs[5]}  |  {self.boxs[6]} \n---------------')
        print(f' {self.boxs[7]}  |  {self.boxs[8]}  |  {self.boxs[9]} ')

    def update_box(self, box_num, key):
        if self.boxs[box_num] == ' ':    
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

            

    def reset_board(self):
        self.boxs = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

board = Board()

#Introduction 
def clear_screen():
    os.system('clear')
    print('Welcome to the TicTacToe simulator')
    #Displays the board
    board.display()

while True:
    while True:
        #Updates the board after input
        clear_screen()

        #For X Player
        x_move = As('X, Choose a position between 1 - 9 : ',int)
        #Put x input into the board
        board.update_box(x_move, "X")
        
        #Updates the board after input
        clear_screen()
        
    #Check for win for X
        if board.win_solution("X"):
            print('Congrats, X you have won')
            break
        else:
            break    
        
    
    while True:
        #For O Player
        o_move = As('O, Choose a position between 1 - 9 : ',int)
        #Put o input into the board
        board.update_box(o_move, "O")

        #Updates the board after input
        clear_screen()

        #Check for win for O
        if board.win_solution("O"):
            print('Congrats, O you have won')
            break
        else:
            break
   
    p_again = As('Do you want to play again? (Y/N) : ').upper()
    if p_again == "Y":
        board.reset_board()
        continue
    else:
        exit('Game is over')