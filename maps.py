import turtle
import screen
import market
import Boss
import json

f = open("player.json",)
user = json.load(f)

class Map():
    def __init__(self, map, player, location, continent):
        turtle.clear()
        self.map = map
        self.continent = continent
        self.location = location
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
    
    def market(self):
        market_map = market.Market(self.player, self.location, self.continent)
        market_map.screen.onkeypress(lambda: market_map.move_left(), "Left")
        market_map.screen.onkeypress(lambda: market_map.move_right(), "Right")
        market_map.screen.onkeypress(lambda: market_map.move_up(), "Up")
        market_map.screen.onkeypress(lambda: market_map.move_down(), "Down")

    def rank_1(self):
        aboss = Boss.Sort(1, self.continent)
        boss = aboss.rank_sort()
        aboss_screen = screen.game_screen(boss['image'], "boss")
        boss_screen = aboss_screen.create(1000, 1000)

    def rank_2(self):
        aboss = Boss.Sort(2, self.continent)
        boss = aboss.rank_sort()
        aboss_screen = screen.game_screen(boss['image'], "boss")
        boss_screen = aboss_screen.create(1000, 1000)

    def rank_3(self):
        aboss = Boss.Sort(3, self.continent)
        boss = aboss.rank_sort()
        aboss_screen = screen.game_screen(boss['image'], "boss")
        boss_screen = aboss_screen.create(1000, 1000)

    def rank_4(self):
        aboss = Boss.Sort(4, self.continent)
        boss = aboss.rank_sort()
        aboss_screen = screen.game_screen(boss['image'], "boss")
        boss_screen = aboss_screen.create(1000, 1000)

    def rank_5(self):
        aboss = Boss.Sort(5, self.continent)
        boss = aboss.rank_sort()
        aboss_screen = screen.game_screen(boss['image'], "boss")
        boss_screen = aboss_screen.create(1000, 1000)

    def rank_6(self):
        aboss = Boss.Sort(6, self.continent)
        boss = aboss.rank_sort()
        aboss_screen = screen.game_screen(boss['image'], "boss")
        boss_screen = aboss_screen.create(1000, 1000)
    

    def move_left_maps(self):
        if self.player.xcor() < -2100:
            self.market()
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
            self.rank_1()
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
        if self.player.ycor() > 1500 and -420 < self.player.xcor() < -200:
            self.rank_5()
            return
        elif self.player.ycor() > 1500 and 2170 < self.player.xcor() < 2400:
            self.rank_3()
        elif self.player.ycor() > 1500 and 4760 < self.player.xcor() < 4900:
            self.rank_2()
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
        
        if self.player.ycor() < -1500 and -420 < self.player.xcor() < -200:
            self.rank_6()
            return
        elif self.player.ycor() < -1500 and 2170 < self.player.xcor() < 2400:
            self.rank_4()
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
            
