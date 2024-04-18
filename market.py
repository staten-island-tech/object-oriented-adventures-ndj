import screen
import turtle

class Market():

    def __init__(self, player):
        self.map = "market.gif"
        self.location = ''
        a = screen.game_screen(self.map, "map")
        self.screen = a.create(1200, 350)
        self.screen.tracer(0)
        self.screen.listen()
        self.player = player
        self.player.penup()
        self.player.speed(0)
        turtle.update()
        turtle.tracer(1)
        self.canvas = self.screen.getcanvas()
        self.canvas.config(xscrollincrement=str(50))
        self.canvas.config(yscrollincrement=str(50))
    
    def move_left(self):
        self.canvas.xview_scroll(-1, "units")
        self.player.setx(self.player.xcor() - 50)

    def move_right(self):
        self.canvas.xview_scroll(1, "units")
        self.player.setx(self.player.xcor() + 50)
        print("right")
    
    def move_up(self):
        self.canvas.xview_scroll(-1, "units")
        self.player.sety(self.player.ycor() - 50)

    def move_down(self):
        self.canvas.xview_scroll(1, "units")
        self.player.sety(self.player.ycor() + 50)