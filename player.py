class Player:
    def __init__(self):
        self.name = None
        self.symbol = None
        self.score = 0


    def choose_name(self):
        while True:
            self.name = input("Enter your name: ")
            if self.name.isalpha():
                break
            else:
                print("Your input is incorrect")

        return self.name        


    def choose_symbol(self):
        while True:            
            self.symbol = input (f"{self.name} enter you symbol(x or o): ")
            if self.symbol == 'x' or self.symbol == 'o':
                self.symbol = self.symbol.upper()
                break
            else :
                print(f"{self.name} your input is incorrect")

        return self.symbol