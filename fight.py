import character
import Hang
import nukeguess
import random
import time
import screen
import turtle

class Battle():

    def __init__(self, boss, player):
        self.boss = boss
        self.player = player
        self.hang = Hang.Hangman(boss['image'], boss['Name'])
        self.nukeguess = nukeguess.num_guess(boss['Name'], boss['item'], boss['image'])
        self.games = [self.hang, self.nukeguess]
        turtle.penup()
    
    def victory(self):
        time.sleep(1)
        turtle.clear()
        victory = screen.game_screen("blank.gif", "Victory")
        victory_screen = victory.create(100, 100)
        victory_screen.register_shape(self.boss['image'])
        victory_screen.register_shape(f"{self.player['type']}.gif")
        victory_screen.tracer(0)
        boss = turtle.Turtle()
        boss.shape(self.boss['image'])
        boss.penup()
        boss.speed(0)
        boss.goto(0, 0)
        victory_screen.update()
        player = turtle.Turtle()
        player.shape(f"{self.player['type']}.gif")
        player.hideturtle()
        player.penup()
        player.speed(0)
        player.goto(-500, 0)
        player.speed(3)
        player.showturtle()
        player.goto(0, 0)
        boss.hideturtle()
        turtle.goto(0, 400)
        turtle.write(arg="Victory", align="center", font=("Times New Roman", 40, 'normal'))
        time.sleep(1.5)
        player.hideturtle()
        return True
    
    def defeat(self):
        self.player['status'] = 'dead'
        return False

    def rank6battle(self):
        num = random.randint(0, 1)
        random_game = self.games[num]
        result = random_game.game()
        if result == True:
            self.boss['health'] -= self.player['attack']
            if self.boss['health'] <= 0:
                # create a victory function
                return self.victory()
            else:
                num -= 1
                self.rank6battle()
        else:
            self.player['health'] -= self.boss['attack']
            if self.player['health'] <= 0:
                # create a defeat function
                return self.defeat()
            else:
                num -= 1
                self.rank6battle()

    
    