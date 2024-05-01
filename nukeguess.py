import random
<<<<<<< HEAD

joe_biden = print("Joe Biden wants you to guess how much nukes he has")

number = random.randint(1, 20)
guess = 0
count = 1
guesslist=[]
while guess != number:
    guess = int(input("Enter Guess: "))
   
    if count == 3:
            print("You failed to guess to guess the number of nukes I have, now you die by my NUKES!!!")
    elif guess < number:
        print("Guess higher!")
        count += 1
        guesslist.append(guess)
    elif guess > number:
        print("Guess lower!")
        count += 1
        guesslist.append(guess)
    else:
        print("You won!")
        guesslist.append(guess)

print('It took you', count, 'guesses!')
print('You can finally move on to the next mini-game...')
print(guesslist)
=======
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
                turtle.write(arg=f"You failed to guess to guess how {self.item} I have, now you die by my NUKES!!!", align='center', font=('Times New Roman', 40, 'normal'))
                time.sleep(1)
                self.screen.register_shape("nuke.gif")
                nuke = turtle.Turtle()
                nuke.speed(0)
                nuke.penup()
                nuke.goto(0, 700)
                nuke.shape("nuke.gif")
                nuke.speed(3)
                turtle.update()
                turtle.tracer(1)
                nuke.goto(0, 0)
                turtle.clear()
                nuke.hideturtle()
                nuclear = screen.game_screen("nukediekillyou.gif", "Nuked")
                nuclear.create(574, 574)    
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

>>>>>>> main
