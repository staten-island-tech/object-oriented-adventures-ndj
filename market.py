import screen
import turtle
import maps
import json
import time

f = open("player.json",)
user = json.load(f)

class Market():

    def __init__(self, player, location, continent, playerdict):
        self.map = "market.gif"
        self.location = location
        self.continent = continent
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
        self.screen.onkeypress(lambda: self.move_right(), key="Right")
        self.screen.onkeypress(lambda: self.move_left(), key="Left")
        self.screen.onkeypress(lambda: self.move_up(), key="Up")
        self.screen.onkeypress(lambda: self.move_down(), key="Down")
        self.playerdict = playerdict
        if user['money'] == 0 and user['type'] != 'royal':
            turtle.write(arg="You are too broke to use the market", align="center", font=('Times New Roman', 70, 'bold'))
            time.sleep(1.5)
            self.maps()
    
    def maps(self):
        the_map = maps.Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
        the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
        the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
        the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
        the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")

    def armor_seller(self):
        if user['type'] == 'royal':
            pass
    
    def move_left(self):
        if user['money'] == 0 and user['type'] != 'royal':
            return
        else:
            self.canvas.xview_scroll(-1, "units")
            self.player.setx(self.player.xcor() - 50)

    def move_right(self):
        if user['money'] == 0 and user['type'] != 'royal':
            return
        elif self.player.xcor() > 2500:
            self.maps()
        else:
            self.canvas.xview_scroll(1, "units")
            self.player.setx(self.player.xcor() + 50)
        
    def move_up(self):
        if user['money'] == 0 and user['type'] != 'royal':
            return
        else:
            self.canvas.yview_scroll(-1, "units")
            self.player.sety(self.player.ycor() + 50)

    def move_down(self):
        if user['money'] == 0 and user['type'] != 'royal':
            return
        else:
            self.canvas.yview_scroll(1, "units")
            self.player.sety(self.player.ycor() - 50)