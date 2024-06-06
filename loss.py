import screen
import turtle

class Loss():

    def __init__(self):
        turtle.clear()
        the_screen = screen.game_screen('gameover.gif', 'Game over')
        the_screen.create(100, 100)
        