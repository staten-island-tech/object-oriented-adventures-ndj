import random
import turtle
import screen
    

class tic_tac_toe():

    def __init__(self):
        turtle.penup()
        turtle.goto(0, 0)
        self.square_moves = ['A1','B1','C1','A2','B2','C2','A3','B3','C3']
        self.change_squares = ['A1', 'B1', 'C1', 'A2','B2', 'C2', 'A3', 'B3', 'C3']
        self.taken_squares = []
        self.player_squares = []
        self.computer_squares = []
        self.winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.a = True
        self.screen_commands = screen.game_screen("blank.gif", "Tic Tac Toe")
        self.screen = self.screen_commands.create(100, 100)
        self.screen_commands.text_input(" ", "I challenge you to a game of tic-tac-toe")
        self.g = self.screen_commands.text_input(" ", "Pick x or o")

    def game(self):    
        while self.a:
            turtle.write(f"""
                    {self.change_squares[0]} / {self.change_squares[1]} / {self.change_squares[2]}
                    {self.change_squares[3]} / {self.change_squares[4]} / {self.change_squares[5]}
                    {self.change_squares[6]} / {self.change_squares[7]} / {self.change_squares[8]}
                    """, font=('Times New Roman', 200, 'normal'))
            if self.g == 'x':
                self.screen_commands.text_input("", "You go first!")
                square = self.screen_commands.text_input(" ", "Pick a square")
                if square not in self.square_moves:
                    self.screen_commands.text_input("", "You're a moron")
                else:
                    self.a = 0
                    for i in self.change_squares:
                        if square == str(i):
                            i = self.g
                            self.taken_squares.append(self.a)
                            self.player_squares.append(self.a)
                            self.change_squares[self.a] = i
                            
                        self.a += 1
                    random_square = random.randint(0, 8)

                    if random_square in self.taken_squares and len(self.taken_squares) <= 8:
                        random_square = random.randint(0, 8)
                        while random_square in self.taken_squares:
                            random_square = random.randint(0, 8)
                    elif len(self.taken_squares) > 8:
                        pass
                    else:  
                        self.change_squares[random_square] = 'o'
                        self.taken_squares.append(random_square)
                        self.computer_squares.append(random_square)
                

            elif self.g == 'o':
                self.screen_commands.text_input("", "You go after me!")
                random_square = random.randint(0, 8)
                if random_square in self.taken_squares:
                    random_square = random.randint(0, 8)
                    while random_square in self.taken_squares:
                        random_square = random.randint(0, 8)
                
                self.change_squares[random_square] = 'x'
                self.taken_squares.append(random_square)
                self.computer_squares.append(random_square)
                turtle.write(f"""
                {self.change_squares[0]} / {self.change_squares[1]} / {self.change_squares[2]}
                {self.change_squares[3]} / {self.change_squares[4]} / {self.change_squares[5]}
                {self.change_squares[6]} / {self.change_squares[7]} / {self.change_squares[8]}
                """, font=("Times New Roman", 200, "normal"))
                square = input("Pick a square: ")
                if square not in self.square_moves:
                    print("You are acoustic")
                else:
                    print("Good move")
                    self.a = 0
                    for i in self.change_squares:
                        if square == str(i):
                            i = self.g
                            self.taken_squares.append(self.a)
                            self.player_squares.append(self.a)
                            self.change_squares[self.a] = i
                            
                        self.a += 1

            if len(self.player_squares) > 2:
                for i in self.winning_combinations:
                    intersection = set(self.player_squares).intersection(set(i))
                    check = all(e in list(intersection) for e in i)
                    if check == True:
                        self.a = False
                        turtle.write(f"""
                        {self.change_squares[0]} / {self.change_squares[1]} / {self.change_squares[2]}
                        {self.change_squares[3]} / {self.change_squares[4]} / {self.change_squares[5]}
                        {self.change_squares[6]} / {self.change_squares[7]} / {self.change_squares[8]}
                        """, font=("Times New Roman", 200, "normal"))
                        self.screen_commands.text_input("", 'You win!')

            if len(self.computer_squares) > 2:
                for i in self.winning_combinations:
                    intersection = set(self.computer_squares).intersection(set(i))
                    check = all(e in list(intersection) for e in i)
                    if check == True:
                        self.a = False
                        turtle.write(f"""
                        {self.change_squares[0]} / {self.change_squares[1]} / {self.change_squares[2]}
                        {self.change_squares[3]} / {self.change_squares[4]} / {self.change_squares[5]}
                        {self.change_squares[6]} / {self.change_squares[7]} / {self.change_squares[8]}
                        """, font=("Times New Roman", 200, "normal"))
                        self.screen_commands.text_input("", 'You lose!')
            
            if len(self.taken_squares) > 8:
                    self.screen_commands.text_input("", "It's a draw!")
                    turtle.write(f"""
                    {self.change_squares[0]} / {self.change_squares[1]} / {self.change_squares[2]}
                    {self.change_squares[3]} / {self.change_squares[4]} / {self.change_squares[5]}
                    {self.change_squares[6]} / {self.change_squares[7]} / {self.change_squares[8]}
                    """, font=("Times New Roman", 200, "normal"))
                    self.a = False

                    

            
    
    
    
 
    
tic = tic_tac_toe()
tic.game()
turtle.mainloop()