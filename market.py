import screen
import turtle
import maps

class Market():

    def __init__(self, player, location):
        self.map = "market.gif"
        self.location = location
        a = screen.game_screen(self.map, "map")
        self.screen = a.create(6000, 3000)
        self.screen.tracer(0)
        self.screen.listen()
        self.player = player
        self.player.penup()
        self.player.speed(0)
        self.player.showturtle()
        self.player.goto(0, 0)
        turtle.update()
        turtle.tracer(1)
        self.canvas = self.screen.getcanvas()
        self.canvas.config(xscrollincrement=str(50))
        self.canvas.config(yscrollincrement=str(50))
    
    def maps(self):
        the_map = maps.Map(f"{self.location}_map.gif", self.player, self.location)
        the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
        the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
        the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
        the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")

    def move_left(self):
        self.canvas.xview_scroll(-1, "units")
        self.player.setx(self.player.xcor() - 50)

    def move_right(self):
        if self.player.xcor() > 2500:
            self.maps()
        self.canvas.xview_scroll(1, "units")
        self.player.setx(self.player.xcor() + 50)
        
    def move_up(self):
        self.canvas.yview_scroll(-1, "units")
        self.player.sety(self.player.ycor() + 50)

    def move_down(self):
        self.canvas.yview_scroll(1, "units")
        self.player.sety(self.player.ycor() - 50)