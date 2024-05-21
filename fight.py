import character
import Hang
import nukeguess
import random
import time
import screen
import turtle

class Battle():

    def __init__(self, boss, player):
        turtle.tracer(0)
        self.boss = boss
        self.player = player
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
        boss.hideturtle()
        turtle.goto(0, 400)
        turtle.write(arg="Victory", align="center", font=("Times New Roman", 40, 'normal'))
        time.sleep(1.5)
        
        return True
    
    def defeat(self):
        self.player['status'] = 'dead'
        return False

    def rank6battle(self):
        turtle.goto(0, 0)
        turtle.clear()
        a = True
        while a:
            self.hang = Hang.Hangman(self.boss['image'], self.boss['Name'])
            self.nukeguess = nukeguess.num_guess(self.boss['Name'], self.boss['item'], self.boss['image'])
            self.games = [self.hang, self.nukeguess]
            turtle.clear()
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
                    turtle.clear()
                    turtle.goto(0, 400)
                    turtle.write(arg=f"You have attacked {self.boss['Name']}. His health is now: {self.player['health']}.", align='center', font=('Times New Roman', 40, 'normal'))
                    turtle.update()
                    time.sleep(2)
                    
        else:
            self.player['health'] -= self.boss['attack']
            if self.player['health'] <= 0:
                # create a defeat function
                return self.defeat()
            else:
                num -= 1
                turtle.clear()
                turtle.goto(0, 400)
                turtle.write(arg=f"{self.boss['Name']} has attacked you! Your health is now: {self.player['health']}.", align='center', font=('Times New Roman', 40, 'normal'))
                turtle.update()
                time.sleep(1)
                return self.rank6battle()
    
    def rank5battle(self):
        pass

    def rank4battle(self):
        pass
    
    def rank3battle(self):
        pass

    def rank2battle(self):
        pass

    def rank1battle(self):
        pass
    
    