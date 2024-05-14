import screen
import turtle

class Loss():

    def __init__(self):
        the_screen = screen.game_screen('blank.gif', 'Game over')
        the_screen.create(100, 100)
        turtle.write(arg="Game over", align='center', font=('Times New Roman', 60, 'normal'))