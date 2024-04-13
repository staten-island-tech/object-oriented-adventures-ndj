import turtle
import screen

class Map():
    def __init__(self, map, player):
        self.map = map
        self.location = ''
        a = screen.game_screen(self.map, "map")
        self.screen = a.create(12000, 3000)
        self.screen.tracer(0)
        self.screen.listen()
        self.player = player
        self.player.penup()
        self.player.speed(0)
        self.player.goto(-360, 90)
        turtle.update()
        turtle.tracer(1)
        self.canvas = self.screen.getcanvas()
        self.canvas.config(xscrollincrement=str(50))
        self.canvas.config(yscrollincrement=str(50))
    
    def deactivate(self):
        self.screen.onkeypress(lambda: None, "Up")
        self.screen.onkeypress(lambda: None, "Left")
        self.screen.onkeypress(lambda: None, "Right")
        self.screen.onkeypress(lambda: None, "Down")
    
    def move_left_maps(self):
        if self.player.xcor() < -2100:
            market = screen.game_screen("market.gif", "market")
            market.create(100, 100)
            self.deactivate()
            return
        elif self.player.xcor() < -400 and self.player.ycor() > 200:
            return
        elif 2180 < self.player.xcor() < 2250 and self.player.ycor() > 200:
            return
        elif 4700 < self.player.xcor() < 4770 and self.player.ycor() > 200:
            return
        elif self.player.xcor() < -400 and self.player.ycor() < 0:
            return
        elif 2180 < self.player.xcor() <2250 and self.player.ycor() < 0:
            return
        else:
            self.canvas.xview_scroll(-1, "units")
            self.player.setx(self.player.xcor() - 50)
    
    def move_right_maps(self):
        if self.player.xcor() > 6000:
            self.deactivate()
            return
        elif -280 > self.player.xcor() > -350 and self.player.ycor() > 200:
            return
        elif 2350 < self.player.xcor() < 2420 and self.player.ycor() > 200:
            return
        elif -280 > self.player.xcor() > -350 and self.player.ycor() < 0:
            return
        elif 2350 < self.player.xcor() < 2420 and self.player.ycor() < 0:
            return
        elif 4900 < self.player.xcor() < 4970 and self.player.ycor() > 200:
            return
        else:
            self.canvas.xview_scroll(1, "units")
            self.player.setx(self.player.xcor() + 50)

    def move_up_maps(self):
        if self.player.ycor() > 1500:
            self.deactivate()
            return
        elif self.player.ycor() > 180 and -3000 < self.player.xcor() < -430:
            return
        elif self.player.ycor() > 180 and -280 < self.player.xcor() < 2160:
            return
        elif self.player.ycor() > 180 and 2440 < self.player.xcor() < 4750:
            return
        elif self.player.ycor() > 180 and 4930 < self.player.xcor() < 7000:
            return
        else:
            self.canvas.yview_scroll(-1, "units")
            self.player.sety(self.player.ycor() + 50)

    def move_down_maps(self):
        
        if self.player.ycor() < -1500:
            self.deactivate()
            return
        elif self.player.ycor() < 70 and -3000 < self.player.xcor() < -430:
            return
        elif self.player.ycor() < 70 and -280 < self.player.xcor() < 2160:
            return
        elif self.player.ycor() < 70 and 2440 < self.player.xcor() < 4750:
            return
        elif self.player.ycor() < 70 and 4930 < self.player.xcor() < 7000:
            return
        else:
            self.canvas.yview_scroll(1, "units")
            self.player.sety(self.player.ycor() - 50)
            
