import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
class Menu:
    
    def main_menu(self):
        print("------------------------------ \n"
              "Welcome to Zeyad's Tic-Tac-Toe \n"
              "------------------------------")
        print("1: Start the game \n"
            "2: Quit the game" )
    
        while True:
            choice = input("Please choose 1 or 2: ")
            if choice == '1' or choice == '2':
                clear_screen()
                if choice == '1':
                    print("\nStarting the game.... ") 

                else:
                    print("Thank you Goodbye!")
                break

            else :
                print("Your input is incorrect")

        return choice 
           

    def end_menu(self):
        print("1: Restart the game \n"
            "2: Quit the game " )
        
        while True:
            choice = input("Please choose 1 or 2: ")
            if choice == '1' or choice == '2':
                self.choice = choice

                if choice == '1':
                    print("\nRestarting the game....") 
                break

            else :
                print("Your input is incorrect ")
        return choice