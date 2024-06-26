import turtle
import screen
import market
import Boss
import json
import time
import fight
import random
import loss

f = open("player.json",)
user = json.load(f)

class Map():
    def __init__(self, map, player, location, continent, playerdict):
        turtle.goto(0, 0)
        turtle.penup()
        self.map = map
        self.continent = continent
        self.location = location
        self.screen_commands = screen.game_screen(self.map, "map")
        self.screen = self.screen_commands.create(12000, 3000)
        self.screen.tracer(0)
        self.screen.listen()
        self.player = player
        self.player.penup()
        self.player.speed(0)
        self.player.goto(-360, 90)
        turtle.clear()
        turtle.update()
        turtle.tracer(1)
        self.canvas = self.screen.getcanvas()
        self.canvas.config(xscrollincrement=str(50))
        self.canvas.config(yscrollincrement=str(50))
        self.screen.onkeypress(lambda: self.travel(), key="t")
        self.screen.onkeypress(lambda: self.inventory(), key="i")
        self.playerdict = playerdict
        turtle.goto(100, 0)
        turtle.write(f"Welcome to {self.continent}", font=("Times New Roman", 60, "normal"))
        time.sleep(2)
        turtle.clear()
        turtle.goto(0, 0)
    
    
    def deactivate(self):
        self.screen.onkeypress(lambda: None, "Up")
        self.screen.onkeypress(lambda: None, "Left")
        self.screen.onkeypress(lambda: None, "Right")
        self.screen.onkeypress(lambda: None, "Down")
    
    def inventory(self):
        self.screen_commands.text_input("Inventory", self.playerdict['inventory'])
        self.screen.onkeypress(lambda: self.move_up_maps(), key="Up")
        self.screen.onkeypress(lambda: self.move_down_maps(), key="Down")
        self.screen.onkeypress(lambda: self.move_left_maps(), key="Left")
        self.screen.onkeypress(lambda: self.move_right_maps(), key="Right")
        self.screen.onkeypress(lambda: self.travel(), key="t")
        self.screen.onkeypress(lambda: self.inventory(), key="i")


    def travel(self):
        continents = ["North America", "South America", "Europe", "Africa", "Asia", "Australia"]
        continents.remove(self.continent)
        if 'travel' not in self.playerdict['inventory']['potions']:
            return
        else:
            certain = self.screen_commands.text_input("Are you sure", "Are you sure you want to use your travel potion?[y/n]")
            if certain.lower() == 'n':
                self.screen_commands.text_input(" ", "Alright then")
                the_map = Map(self.map, self.player, self.location, self.continent, self.playerdict)
            location = self.screen_commands.text_input("Where to", f"Choose a continent to travel to out of: {continents}") 
            while location.title() not in continents:
                location = self.screen_commands.text_input(" ", f"Enter a continent given in the list: {continents}")
            if len(str.split(location)) > 1:
                a = str.split(location)
                a[0] += "_"
                a[0] += a[1]
                new = a[0].lower()
            else:
                new = location.lower()
            self.playerdict['inventory']['potions'].remove('travel')
            new_map = Map(f"{new}_map.gif", self.player, new, location.title(), self.playerdict)

    def market(self):
        market_map = market.Market(self.player, self.location, self.continent, self.playerdict)
        # market_map.screen.onkeypress(lambda: market_map.move_left(), "Left")
        # market_map.screen.onkeypress(lambda: market_map.move_right(), "Right")
        # market_map.screen.onkeypress(lambda: market_map.move_up(), "Up")
        # market_map.screen.onkeypress(lambda: market_map.move_down(), "Down")

    def rank_1(self):
        self.deactivate()
        aboss = Boss.Sort(1, self.continent)
        boss = aboss.rank_sort()
        if boss['status'] != 'alive':
            the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
            the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
            the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
            the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
            the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
            turtle.write(arg=f"You can't fight {boss['Name']} twice", align='center', font=('Times New Roman', 50, 'normal'))
            time.sleep(1)
            turtle.clear()
        
        else:
            aboss_screen = screen.game_screen("new_challenger.gif", "boss")
            boss_screen = aboss_screen.create(1780, 1000)
            boss_screen.register_shape(boss['image'])
            boss_screen.tracer(0)
            enemy = turtle.Turtle()
            enemy.shape(boss['image'])
            enemy.penup()
            enemy.goto(330, 0)
            time.sleep(1)
            boss_screen.update()
            time.sleep(1)
            enemy.hideturtle()
            fight_commands = fight.Battle(boss, self.playerdict)
            result = fight_commands.rank6battle()
            if result:
                turtle.clear()
                the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                turtle.write(arg=f"You have defeated {boss['Name']} and have conquered {boss['country']}", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                reward = random.randint(200, 500)
                turtle.write(arg=f"As a reward you receive {reward} money", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                boss['status'] = 'defeated'
                if self.playerdict['money'] == 0:
                    turtle.write(arg=f"You can now use the market", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                self.playerdict['money'] += reward
            else:
                if 'revive' in self.playerdict['inventory']['potions']:
                    turtle.clear()
                    the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                    the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                    the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                    the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                    the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                    turtle.write(arg=f"You have been defeated by {boss['Name']} but were saved by your revive potion", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                    self.playerdict['inventory']['potions'].remove('revive')
                else:
                    loss.Loss()
                
        
        
    def rank_2(self):
        self.deactivate()
        aboss = Boss.Sort(2, self.continent)
        boss = aboss.rank_sort()
        if boss['status'] != 'alive':
            the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
            the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
            the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
            the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
            the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
            turtle.write(arg=f"You can't fight {boss['Name']} twice", align='center', font=('Times New Roman', 50, 'normal'))
            time.sleep(1)
            turtle.clear()
        
        else:
            aboss_screen = screen.game_screen("new_challenger.gif", "boss")
            boss_screen = aboss_screen.create(1780, 1000)
            boss_screen.register_shape(boss['image'])
            boss_screen.tracer(0)
            enemy = turtle.Turtle()
            enemy.shape(boss['image'])
            enemy.penup()
            enemy.goto(330, 0)
            time.sleep(1)
            boss_screen.update()
            time.sleep(1)
            enemy.hideturtle()
            fight_commands = fight.Battle(boss, self.playerdict)
            result = fight_commands.rank6battle()
            if result:
                turtle.clear()
                the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                turtle.write(arg=f"You have defeated {boss['Name']} and have conquered {boss['country']}", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                reward = random.randint(100, 200)
                turtle.write(arg=f"As a reward you receive {reward} money", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                boss['status'] = 'defeated'
                if self.playerdict['money'] == 0:
                    turtle.write(arg=f"You can now use the market", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                self.playerdict['money'] += reward
            else:
                if 'revive' in self.playerdict['inventory']['potions']:
                    turtle.clear()
                    the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                    the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                    the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                    the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                    the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                    turtle.write(arg=f"You have been defeated by {boss['Name']} but were saved by your revive potion", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                    self.playerdict['inventory']['potions'].remove('revive')
                else:
                    loss.Loss()
        
        

    def rank_3(self):
        self.deactivate()
        aboss = Boss.Sort(3, self.continent)
        boss = aboss.rank_sort()
        if boss['status'] != 'alive':
            the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
            the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
            the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
            the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
            the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
            turtle.write(arg=f"You can't fight {boss['Name']} twice", align='center', font=('Times New Roman', 50, 'normal'))
            time.sleep(1)
            turtle.clear()
        
        else:
            aboss_screen = screen.game_screen("new_challenger.gif", "boss")
            boss_screen = aboss_screen.create(1780, 1000)
            boss_screen.register_shape(boss['image'])
            boss_screen.tracer(0)
            enemy = turtle.Turtle()
            enemy.shape(boss['image'])
            enemy.penup()
            enemy.goto(330, 0)
            time.sleep(1)
            boss_screen.update()
            time.sleep(1)
            enemy.hideturtle()
            fight_commands = fight.Battle(boss, self.playerdict)
            result = fight_commands.rank6battle()
            if result:
                turtle.clear()
                the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                turtle.write(arg=f"You have defeated {boss['Name']} and have conquered {boss['country']}", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                reward = random.randint(45, 90)
                turtle.write(arg=f"As a reward you receive {reward} money", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                boss['status'] = 'defeated'
                if self.playerdict['money'] == 0:
                    turtle.write(arg=f"You can now use the market", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                self.playerdict['money'] += reward
            else:
                if 'revive' in self.playerdict['inventory']['potions']:
                    turtle.clear()
                    the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                    the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                    the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                    the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                    the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                    turtle.write(arg=f"You have been defeated by {boss['Name']} but were saved by your revive potion", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                    self.playerdict['inventory']['potions'].remove('revive')
                else:
                    loss.Loss()

    def rank_4(self):
        self.deactivate()
        aboss = Boss.Sort(4, self.continent)
        boss = aboss.rank_sort()
        if boss['status'] != 'alive':
            the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
            the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
            the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
            the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
            the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
            turtle.write(arg=f"You can't fight {boss['Name']} twice", align='center', font=('Times New Roman', 50, 'normal'))
            time.sleep(1)
            turtle.clear()
        
        else:
            aboss_screen = screen.game_screen("new_challenger.gif", "boss")
            boss_screen = aboss_screen.create(1780, 1000)
            boss_screen.register_shape(boss['image'])
            boss_screen.tracer(0)
            enemy = turtle.Turtle()
            enemy.shape(boss['image'])
            enemy.penup()
            enemy.goto(330, 0)
            time.sleep(1)
            boss_screen.update()
            time.sleep(1)
            enemy.hideturtle()
            fight_commands = fight.Battle(boss, self.playerdict)
            result = fight_commands.rank6battle()
            if result:
                turtle.clear()
                the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                turtle.write(arg=f"You have defeated {boss['Name']} and have conquered {boss['country']}", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                reward = random.randint(20, 40)
                turtle.write(arg=f"As a reward you receive {reward} money", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                boss['status'] = 'defeated'
                if self.playerdict['money'] == 0:
                    turtle.write(arg=f"You can now use the market", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                self.playerdict['money'] += reward
            else:
                if 'revive' in self.playerdict['inventory']['potions']:
                    turtle.clear()
                    the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                    the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                    the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                    the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                    the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                    turtle.write(arg=f"You have been defeated by {boss['Name']} but were saved by your revive potion", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                    self.playerdict['inventory']['potions'].remove('revive')
                else:
                    loss.Loss()

    def rank_5(self):
        self.deactivate()
        aboss = Boss.Sort(5, self.continent)
        boss = aboss.rank_sort()
        if boss['status'] != 'alive':
            the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
            the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
            the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
            the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
            the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
            turtle.write(arg=f"You can't fight {boss['Name']} twice", align='center', font=('Times New Roman', 50, 'normal'))
            time.sleep(1)
            turtle.clear()
        
        else:
            aboss_screen = screen.game_screen("new_challenger.gif", "boss")
            boss_screen = aboss_screen.create(1780, 1000)
            boss_screen.register_shape(boss['image'])
            boss_screen.tracer(0)
            enemy = turtle.Turtle()
            enemy.shape(boss['image'])
            enemy.penup()
            enemy.goto(330, 0)
            time.sleep(1)
            boss_screen.update()
            time.sleep(1)
            enemy.hideturtle()
            fight_commands = fight.Battle(boss, self.playerdict)
            result = fight_commands.rank6battle()
            if result:
                turtle.clear()
                the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                turtle.write(arg=f"You have defeated {boss['Name']} and have conquered {boss['country']}", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                reward = random.randint(10, 20)
                turtle.write(arg=f"As a reward you receive {reward} money", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                boss['status'] = 'defeated'
                if self.playerdict['money'] == 0:
                    turtle.write(arg=f"You can now use the market", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                self.playerdict['money'] += reward
            else:
                if 'revive' in self.playerdict['inventory']['potions']:
                    turtle.clear()
                    the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                    the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                    the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                    the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                    the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                    turtle.write(arg=f"You have been defeated by {boss['Name']} but were saved by your revive potion", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                    self.playerdict['inventory']['potions'].remove('revive')
                else:
                    loss.Loss()

    def rank_6(self):
        self.deactivate()
        aboss = Boss.Sort(6, self.continent)
        boss = aboss.rank_sort()
        if boss['status'] != 'alive':
            the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
            the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
            the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
            the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
            the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
            turtle.write(arg=f"You can't fight {boss['Name']} twice", align='center', font=('Times New Roman', 50, 'normal'))
            time.sleep(1)
            turtle.clear()
        
        else:
            aboss_screen = screen.game_screen("new_challenger.gif", "boss")
            boss_screen = aboss_screen.create(1780, 1000)
            boss_screen.register_shape(boss['image'])
            boss_screen.tracer(0)
            enemy = turtle.Turtle()
            enemy.shape(boss['image'])
            enemy.penup()
            enemy.goto(330, 0)
            time.sleep(1)
            boss_screen.update()
            time.sleep(1)
            enemy.hideturtle()
            fight_commands = fight.Battle(boss, self.playerdict)
            result = fight_commands.rank6battle()
            if result:
                turtle.clear()
                the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                turtle.write(arg=f"You have defeated {boss['Name']} and have conquered {boss['country']}", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                reward = random.randint(1, 10)
                turtle.write(arg=f"As a reward you receive {reward} money", align='center', font=('Times New Roman', 50, 'normal'))
                time.sleep(1)
                turtle.clear()
                boss['status'] = 'defeated'
                if self.playerdict['money'] == 0:
                    turtle.write(arg=f"You can now use the market", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                self.playerdict['money'] += reward
            else:
                if 'revive' in self.playerdict['inventory']['potions']:
                    turtle.clear()
                    the_map = Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
                    the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
                    the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
                    the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
                    the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")
                    turtle.write(arg=f"You have been defeated by {boss['Name']} but were saved by your revive potion", align='center', font=('Times New Roman', 50, 'normal'))
                    time.sleep(1)
                    turtle.clear()
                    self.playerdict['inventory']['potions'].remove('revive')
                else:
                    loss.Loss() 
    

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
            
