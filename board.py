class Board:
    def __init__(self):
        self.board = [str(i) for i in range (1,10)]


    def display_board(self):
        for i in range (0,9,3):
            print("|".join(self.board[i:i+3]))  
            if i<6:
                print("-"*5) 


    def upd_board(self , symbol:str , choice:int):
        if self.valid_move(choice):
            self.board[choice-1] = symbol


    def valid_move(self , choice:int):
        if choice >= 1 and choice <= 9 and not self.board[choice-1].isalpha():
            return True


    def reset_board(self):
        self.board = [str(i) for i in range (1,10)]