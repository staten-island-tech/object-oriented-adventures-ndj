import random
import screen
import turtle
import time

class Hangman():

    def __init__(self, image, boss):
        self.words = ['across',  'against', 'laugh',  'middle',  'minute',  'mountain', 'ninth', 'ocean', 'office', 'parent', 'peanut', 'pencil', 'picnic', 'seconds', 'slowly', 'stories', 'student', 'sudden', 'suit', 'sure', 'swimming', 'though', 'threw', 'tired', 'well', 'whole', 'whose', 'weird', 'wouldnt', 'writing', 'written', 'wrote', 'yell', 'young']
        self.word = random.choice(self.words)
        self.spaces = ['_'] * len(self.word)
        self.image = image
        self.boss = boss
        

    def get_letter_position(self, guess, word, spaces):
        index = -2
        while index != -1:
            if guess in word:
                index = word.find(guess)
                removed_character ='*'
                word = word[:index]+removed_character+word[index+1:]
                spaces[index] = guess
            else:
                index = -1
        return (word, spaces)

    def win_check(self):
        for i in range(0, len(self.spaces)):
            if self.spaces[i] == '_':
                return -1
        
        return 1
    
    def game(self):
        self.screen_commands = screen.game_screen("hangman.gif", "Hangman")
        self.screen = self.screen_commands.create(250, 250)
        self.screen.tracer(0)
        turtle.penup()
        self.screen.register_shape(self.image)
        boss = turtle.Turtle()
        boss.shape(self.image)
        boss.penup()
        boss.goto(-700, 0)
        self.screen.update()
        guess_list = []
        num_turns = 11
        b = 0
        while num_turns - b > 1:
            b += 1
            turtle.goto(0, -400)
            turtle.write(arg=f"{self.boss} wants you to guess his favorite word", align='center', font=('Times New Roman', 40, 'normal'))
            turtle.goto(0, 400)
            turtle.write(arg=f'You have {num_turns - b} turns left.', align='center', font=('Times New Roman', 40, 'normal'))
            guess = self.screen_commands.text_input("Guess", 'Guess a letter or a word:')
            try:
                test = int(guess)
                self.screen_commands.text_input("You are stupid", "Enter a string next time")
                turtle.clear()
            except ValueError:
                if len(guess) == 0:
                    turtle.clear()
                    b -= 1
                    guess = 'yqowipeyroqiwpeyropyqweoipry'
                    word, spaces = self.get_letter_position(guess, self.word, self.spaces)
                    turtle.clear()
                    turtle.goto(0, 0)
                    turtle.write(arg=spaces, align='left', font=('Times New Roman', 50, 'normal'))
                    turtle.goto(-400, -200)
                    turtle.write(arg=f"You have guessed: {guess_list}", align='left', font=('Times New Roman', 30, 'normal'))
                    
                    
                elif len(guess) > 1:
                    if guess == self.word:
                        turtle.clear()
                        turtle.goto(0, 0)
                        turtle.write(arg=f"I didn't think that you would be able to figure it out...", align='center', font=('Times New Roman', 60, 'normal'))
                        turtle.mainloop()
                        time.sleep(1)
                        return True
                    else:
                        turtle.clear()
                        word, spaces = self.get_letter_position(guess, self.word, self.spaces)
                        turtle.goto(0, 0)
                        turtle.write(arg=spaces, align='left', font=('Times New Roman', 50, 'normal'))
                        turtle.goto(-400, -200)
                        guess_list.append(guess)
                        turtle.write(arg=f"You have guessed: {guess_list}", align='center', font=('Times New Roman', 30, 'normal'))
                        self.screen_commands.text_input('You suck', 'Sorry, that is not the word.')
                elif guess in self.word:
                    word, spaces = self.get_letter_position(guess, self.word, self.spaces)
                    turtle.clear()
                    turtle.goto(0, 0)
                    turtle.write(arg=spaces, align='left', font=('Times New Roman', 50, 'normal'))
                    turtle.goto(-400, -200)
                    guess_list.append(guess)
                    turtle.write(arg=f"You have guessed: {guess_list}", align='left', font=('Times New Roman', 30, 'normal'))
                else:
                    turtle.clear()
                    word, spaces = self.get_letter_position(guess, self.word, self.spaces)
                    turtle.goto(0, 0)
                    turtle.write(arg=spaces, align='left', font=('Times New Roman', 50, 'normal'))
                    turtle.goto(-400, -200)
                    guess_list.append(guess)
                    turtle.write(arg=f"You have guessed: {guess_list}", align='left', font=('Times New Roman', 30, 'normal'))
                    self.screen_commands.text_input('You suck', 'Sorry, that letter is not in the word.')
                
                if self.win_check() == 1:
                    turtle.clear()
                    turtle.goto(0, 0)
                    turtle.write(arg=f"I didn't think that you would be able to figure it out...", align='center', font=('Times New Roman', 60, 'normal'))
                    turtle.mainloop()
                    time.sleep(1)
                    return True
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write(arg=f"You failed. The word was {self.word}.", align='center', font=('Times New Roman', 60, 'normal'))
        turtle.mainloop()
        time.sleep(1)
        return False

