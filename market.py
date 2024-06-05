import screen
import turtle
import maps
import json
import time
import loss


class Market():

    def __init__(self, player, location, continent, playerdict):
        self.map = "market.gif"
        self.location = location
        self.continent = continent
        self.screen_commands = screen.game_screen(self.map, "map")
        self.screen = self.screen_commands.create(6000, 3000)
        self.screen.tracer(0)
        self.screen.listen()
        self.player = player
        self.player.penup()
        self.player.speed(0)
        self.player.showturtle()
        self.player.goto(0, 0)
        turtle.update()
        turtle.tracer(1)
        turtle.listen()
        self.canvas = self.screen.getcanvas()
        self.canvas.config(xscrollincrement=str(50))
        self.canvas.config(yscrollincrement=str(50))
        self.screen.onkeypress(lambda: self.move_right(), key="Right")
        self.screen.onkeypress(lambda: self.move_left(), key="Left")
        self.screen.onkeypress(lambda: self.move_up(), key="Up")
        self.screen.onkeypress(lambda: self.move_down(), key="Down")
        self.playerdict = playerdict
        self.playerdict['money'] = 10
        if self.playerdict['money'] == 0 and self.playerdict['type'] != 'royal':
            turtle.write(arg="You are too broke to use the market", align="center", font=('Times New Roman', 70, 'bold'))
            time.sleep(1.5)
            self.maps()
        self.cost = 0
    
    def maps(self):
        the_map = maps.Map(f"{self.location}_map.gif", self.player, self.location, self.continent, self.playerdict)
        the_map.screen.onkeypress(lambda: the_map.move_right_maps(), key="Right")
        the_map.screen.onkeypress(lambda: the_map.move_left_maps(), key="Left")
        the_map.screen.onkeypress(lambda: the_map.move_up_maps(), key="Up")
        the_map.screen.onkeypress(lambda: the_map.move_down_maps(), key="Down")

    def void(self, x, y):
        pass

    def purchase_armor(self, x, y):
        item = ''
        if y < 1000 or y > 2000:
            turtle.onscreenclick(self.purchase_armor)
        else:
            if x < 200 and x > -200:
                self.cost = 50
                item = 'iron'
            elif x < - 300:
                self.cost = 10
                item = 'bronze'
            elif x > 300:
                self.cost = 100
                item = 'diamond'
            if self.playerdict['money'] < self.cost:
                self.screen_commands.text_input("brokie", "You are too broke to buy this item")
                turtle.onscreenclick(self.purchase_armor)
            else:
                certain = self.screen_commands.text_input("Are you sure ;)", f"This item costs {self.cost} money and you have {self.playerdict['money']} money, are you sure you want to buy it?[y/n]")
                if certain.lower() == 'n':
                    self.screen_commands.text_input("Loser", "Well make up your mind then")
                else:                  
                    self.playerdict['money'] -= self.cost
                    if item == 'iron':
                        self.playerdict['health'] += 50
                    elif item == 'bronze':
                        self.playerdict['health'] += 20
                    elif item == 'diamond':
                        self.playerdict['health'] += 100
                    self.screen_commands.text_input("Purchased", f"Good purchase, your now have {self.playerdict['money']} money")
                    self.screen_commands.text_input("Health buffed", f"You have equipped {item} armor, your health is now {self.playerdict['health']}")
                    turtle.onscreenclick(self.void)
                    self.iron.hideturtle()
                    self.bronze.hideturtle()
                    self.diamond.hideturtle()
                    
                    market_map = Market(self.player, self.location, self.continent, self.playerdict)

    def armor_seller(self):
        if self.playerdict['type'] == 'royal':
            self.screen_commands.text_input('Hi there', 'Hello there... my lord')
            self.screen_commands.text_input(' ', 'I sell armor which can increase your health so you survive stronger hits')
            self.diamond = turtle.Turtle()
            self.diamond.speed(0)
            self.diamond.penup()
            self.diamond.goto(500, 1300)
            self.screen.register_shape("diamond_armor.gif")
            self.diamond.shape("diamond_armor.gif")
            turtle.update()
            browse = self.screen_commands.text_input(' ', "Do you want a set of diamond armor, I'll give you it for free my lord[y/n]")
            if browse.lower() == 'n':
                self.screen_commands.text_input(' ', 'As you wish')
                self.diamond.hideturtle()
            else:
                self.playerdict['health'] += 100
                self.screen_commands.text_input(' ', f'Then here you are my lord, your health is now {self.playerdict['health']}')
        else:
            secret = self.screen_commands.text_input('Hello', 'Hello there traveler')
            if 'shut' in secret.lower() or 'fuck' in secret.lower():
                response = self.screen_commands.text_input('You fucked up', 'Oh you think your all that huh')
                if 'no' in response.lower() or 'sorry' in response.lower():
                    self.screen_commands.text_input('Go away', 'Then fuck off')
                    return
                else:
                    self.screen_commands.text_input('Its over for you', 'Get yo ass over here')
                    loss.Loss()
                    return
            else:
                self.screen_commands.text_input(' ', 'I sell armor which can increase your health so you survive stronger hits')
                browse = self.screen_commands.text_input(' ', "Do you want to buy a set of armor?[y/n]")
                if browse.lower() == 'n':
                    self.screen_commands.text_input(' ', "Alright then")
                    market_map = Market(self.player, self.location, self.continent, self.playerdict)
                else:
                    self.screen_commands.text_input(' ', 'Click on the armor you want to buy!')
                    self.iron = turtle.Turtle()
                    self.iron.speed(0)
                    self.iron.penup()
                    self.iron.goto(0, 1300)
                    self.screen.register_shape("iron_armor.gif")
                    self.iron.shape("iron_armor.gif")
                    self.bronze = turtle.Turtle()
                    self.bronze.speed(0)
                    self.bronze.penup()
                    self.bronze.goto(-500, 1300)
                    self.screen.register_shape("bronze_armor.gif")
                    self.bronze.shape("bronze_armor.gif")
                    self.diamond = turtle.Turtle()
                    self.diamond.speed(0)
                    self.diamond.penup()
                    self.diamond.goto(500, 1300)
                    self.screen.register_shape("diamond_armor.gif")
                    self.diamond.shape("diamond_armor.gif")
                    turtle.update()
                    turtle.onscreenclick(self.purchase_armor)



    
    def move_left(self):
        if self.playerdict['type'] == 'royal':
            return
        else:
            self.canvas.xview_scroll(-1, "units")
            self.player.setx(self.player.xcor() - 50)

    def move_right(self):
        if self.playerdict['type'] == 'royal':
            return
        elif self.player.xcor() > 2500:
            self.maps()
        else:
            self.canvas.xview_scroll(1, "units")
            self.player.setx(self.player.xcor() + 50)
        
    def move_up(self):
        if self.player.xcor() < -250 or self.player.xcor() > 100:
            return
        if self.playerdict['type'] == 'royal':
            return
        elif self.player.ycor() > 1250:
            self.armor_seller()
        else:
            self.canvas.yview_scroll(-1, "units")
            self.player.sety(self.player.ycor() + 50)

    def move_down(self):
        if self.playerdict['money'] == 0 and self.playerdict['type'] != 'royal':
            return
        else:
            self.canvas.yview_scroll(1, "units")
            self.player.sety(self.player.ycor() - 50)