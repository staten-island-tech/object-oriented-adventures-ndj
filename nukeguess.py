import random
import screen
import turtle
import time
import json

class num_guess():

    def __init__(self, boss, item, image):
        self.boss = boss
        self.item = item
        self.image = image
        
        

    def game(self):
        self.screen_commands = screen.game_screen(self.image, "Number guessing")
        self.screen = self.screen_commands.create(100, 100)
        self.screen.tracer(0)
        turtle.penup()
        turtle.goto(0, 350)
        turtle.write(arg=f"{self.boss} wants you to guess how {self.item} he has", align='center', font=('Times New Roman', 50, 'normal'))
        turtle.goto(0, 0)
        self.screen.update()

        number = random.randint(1, 200)
        guess = 0
        count = 1
        guesslist=[]
        while guess != number:
            try:
                guess = int(self.screen_commands.text_input('Guess number', 'Enter number from 1 to 200: '))
            except ValueError:
                self.screen_commands.text_input('You are stupid', 'Enter an integer next time')
            if 1 > guess or guess > 200:
                pass
            elif count == 10:
                turtle.clear()
                turtle.goto(0, 0)
                turtle.write(arg=f"You failed to guess to guess how {self.item} I have, now you die!!!", align='center', font=('Times New Roman', 40, 'normal'))
                time.sleep(1)
                return False
            elif guess < number:
                turtle.clear()
                turtle.goto(0, 400)
                turtle.write(arg=f"{self.boss} wants you to guess how {self.item} he has", align='center', font=('Times New Roman', 40, 'normal'))
                turtle.goto(0, -450)
                turtle.write(arg=f"Guess higher! You have {10 - count} guesses left", align='center', font=('Times New Roman', 40, 'normal'))
                count += 1
                guesslist.append(guess)
                turtle.goto(-700, 0)
                turtle.write(arg=f"You have guessed {guesslist}", align='center', font=('Times New Roman', 20, 'normal'))
            elif guess > number:
                turtle.clear()
                turtle.goto(0, 400)
                turtle.write(arg=f"{self.boss} wants you to guess how {self.item} he has", align='center', font=('Times New Roman', 40, 'normal'))
                turtle.goto(0, -450)
                turtle.write(arg=f"Guess lower! You have {10 - count} guesses left", align='center', font=('Times New Roman', 40, 'normal'))
                count += 1
                guesslist.append(guess)
                turtle.goto(-700, 0)
                turtle.write(arg=f"You have guessed {guesslist}", align='center', font=('Times New Roman', 20, 'normal'))
            else:
                turtle.clear()
                turtle.goto(0, 400)
                turtle.write(arg="You won!", align='center', font=('Times New Roman', 60, 'normal'))
                guesslist.append(guess)
                turtle.goto(0, -400)
                turtle.write(arg=f'It took you {count} guesses.', align='center', font=('Times New Roman', 40, 'normal'))
                time.sleep(0.5)
                turtle.goto(0, 0)
                turtle.write(arg='You can finally move on...', align='center', font=('Times New Roman', 60, 'normal'))
                time.sleep(1)
                return True
        turtle.mainloop()

