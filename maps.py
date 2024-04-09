import turtle
import screen

class Map():
    def __init__(self, map, title, turtle):
        self.map = map
        self.title = title
        a = screen.game_screen("map.gif", "map")
        self.screen = a.create(100, 100)
        self.player = turtle
        self.screen.onkeypress(lambda: self.player.forward(50), key="Right")
        self.screen.onkeypress(lambda: self.player.backward(50) , key="Left")
        self.screen.onkeypress(lambda: self.player.sety(self.player.ycor() + 50), key="Up")
        self.screen.onkeypress(lambda: self.player.sety(self.player.ycor() - 50), key="Down")
