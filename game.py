from menu import Menu
from board import Board
from player import Player
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class game:
    def __init__(self):
        self.menu = Menu()
        self.players = [Player(),Player()]
        self.board = Board()
        self.current_player_ind = 0


    def start_game(self):
        choice = self.menu.main_menu() 
        if choice == '1':
            self.setup_players()
            self.play_game()


    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"\nPlayer {number}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

        if number == 2:
            self.valid_symbol()
            

        
    def valid_symbol(self):
        while self.players[0].symbol == self.players[1].symbol:
            print(f"{self.players[1].name} your input is incorrect")
            self.players[1].symbol = self.players[1].choose_symbol()


    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                if self.check_win():
                    self.players[self.current_player_ind - 1].score += 1
                    clear_screen()
                    self.display_score()
                    self.board.display_board()
                    self.display_winner()
                    
                else:
                    clear_screen()
                    self.board.display_board()
                    print("------- Draw! -------")
                    self.display_score()
                choice = self.menu.end_menu()
                if choice == '1':
                    self.restart_game()

                else:
                    self.quit_game()
                break


    def play_turn(self):
        while True:
            self.board.display_board()
            choice = int(input(f"{self.players[self.current_player_ind].name}, enter your position on the board(1 - 9): "))
            if self.board.valid_move(choice):
                break

            else:
                clear_screen()
                print("Your input is incorrect \n")
                    
        self.board.upd_board(self.players[self.current_player_ind].symbol, choice)
        self.board.display_board()
        clear_screen()
        self.current_player_ind = 1 - self.current_player_ind



    def check_win(self):
        for i in range(7):
            if i % 3 == 0:
                if self.board.board[i] == self.board.board[i + 1] == self.board.board[i + 2]:
                    return True
            if i == 0:
                if self.board.board[i] == self.board.board[i + 4] == self.board.board[i + 8]:
                    return True
            if i == 2:
                if self.board.board[i] == self.board.board[i + 2] == self.board.board[i + 4]:
                    return True
            if i < 3:
                if self.board.board[i] == self.board.board[i + 3] == self.board.board[i + 6]:
                    return True

    
    def check_draw(self):
        for i in range(9):
            if not self.board.board[i].isalpha():
                return False
        return True


    def restart_game(self):
        clear_screen()
        self.board.reset_board()
        self.play_game()


    def display_score(self):
        print(f"{self.players[0].name}: {self.players[0].score}, {self.players[1].name}: {self.players[1].score}\n")


    def display_winner(self):
        print(f"\n------- {self.players[self.current_player_ind - 1].name} wins! -------\n")


    def quit_game(self):
        print("Thank you Goodbye!")


    def end_game(self):
        clear_screen()
        self.display_score()
        self.show_game_winner()
        print("Thank you for playing Zizo's Tic-Tac-Toe!")
    

    def show_game_winner(self):
        if self.players[self.current_player_ind].score > self.players[self.current_player_ind - 1].score:
            print(f"{self.players[self.current_player_ind].name} is the winner!")
        elif self.players[self.current_player_ind].score < self.players[self.current_player_ind - 1].score:
            print(f"{self.players[self.current_player_ind - 1].name} is the winner!")
        else:
            print("Draw!")

game = game()
game.start_game()
