import screen
import turtle
import maps
import json
import time
import loss
import random


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
        turtle.speed(0)
        turtle.update()
        turtle.tracer(1)
        turtle.listen()
        turtle.penup()
        self.canvas = self.screen.getcanvas()
        self.canvas.config(xscrollincrement=str(50))
        self.canvas.config(yscrollincrement=str(50))
        self.screen.onkeypress(lambda: self.move_right(), key="Right")
        self.screen.onkeypress(lambda: self.move_left(), key="Left")
        self.screen.onkeypress(lambda: self.move_up(), key="Up")
        self.screen.onkeypress(lambda: self.move_down(), key="Down")
        
        self.playerdict = playerdict
        self.playerdict['money'] = 200
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
                buff = 50
            elif x < - 300:
                self.cost = 10
                item = 'bronze'
                buff = 20
            elif x > 300:
                self.cost = 100
                item = 'diamond'
                buff = 100
            if self.playerdict['money'] < self.cost:
                self.screen_commands.text_input("brokie", "You are too broke to buy this item")
                turtle.onscreenclick(self.purchase_armor)
            else:
                self.screen_commands.text_input("Info", f"This is {item} armor which grants you {buff} extra health when equipped")
                certain = self.screen_commands.text_input("Are you sure ;)", f"{item} armor costs {self.cost} money and you have {self.playerdict['money']} money, are you sure you want to buy it?[y/n]")
                if certain.lower() == 'n':
                    wish = self.screen_commands.text_input(' ', 'Well do you want to buy anything?[y/n]')
                    if wish.lower() == 'n':
                        self.screen_commands.text_input(' ', "Then get outta here")
                        market_map = Market(self.player, self.location, self.continent, self.playerdict)
                    else:
                        self.screen_commands.text_input("Loser", "Well make up your mind then")
                else:                  
                    self.playerdict['money'] -= self.cost
                    self.playerdict['health'] += buff
                    self.screen_commands.text_input("Purchased", f"Good purchase, your now have {self.playerdict['money']} money")
                    self.screen_commands.text_input("Health buffed", f"You have equipped {item} armor, your health is now {self.playerdict['health']}")
                    turtle.onscreenclick(self.void)
                    self.iron.hideturtle()
                    self.bronze.hideturtle()
                    self.diamond.hideturtle()
                    for i in self.playerdict['inventory']['armor']:
                        if i == 'iron':
                            self.playerdict['health'] -= 50
                        elif i == 'bronze':
                            self.playerdict['health'] -= 20
                        elif i == 'diamond':
                            self.playerdict['health'] -= 100
                        self.playerdict['inventory']['armor'].remove(i)
                    self.playerdict['inventory']['armor'].append(item)
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
                self.screen_commands.text_input(' ', f"Then here you are my lord, your health is now {self.playerdict['health']}")
        else:
            secret = self.screen_commands.text_input('Hello', 'Hello there traveler')
            if 'shut' in secret.lower() or 'fuck' in secret.lower():
                response = self.screen_commands.text_input('You fucked up', 'Oh you think your all that huh')
                if 'no' in response.lower() or 'sorry' in response.lower():
                    self.screen_commands.text_input('Go away', 'Then fuck off')
                    market_map = Market(self.player, self.location, self.continent, self.playerdict)
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

    def purchase_potion(self, x, y):
        item = ''
        if y < 0 or y > 600:
            turtle.onscreenclick(self.purchase_potion)
        else:
            if x < -1800 and x > -2500:
                self.cost = 50
                item = 'luck'
                description = 'is drank upon purchase and either buffs your stats or nerfs them depending on your luck'
            elif x < -2500:
                self.cost = 25
                item = 'travel'
                description = 'allows you to travel to a new continent by clicking "t" in the maps lobby'
            elif x > -1800:
                self.cost = 150
                item = 'revive'
                description = 'revives you after you die, used automatically if in inventory'
            if self.playerdict['money'] < self.cost:
                self.screen_commands.text_input("brokie", "You are too broke to buy this item")
                turtle.onscreenclick(self.purchase_potion)
            else:
                self.screen_commands.text_input("Info", f"This is a {item} potion which {description}")
                certain = self.screen_commands.text_input("Are you sure ;)", f"A {item} potion costs {self.cost} money and you have {self.playerdict['money']} money, are you sure you want to buy it?[y/n]")
                if certain.lower() == 'n':
                    wish = self.screen_commands.text_input(' ', 'Well do you want to buy anything?[y/n]')
                    if wish.lower() == 'n':
                        self.screen_commands.text_input(' ', "Then get outta here")
                        self.health.hideturtle()
                        self.escape.hideturtle()
                        self.revive.hideturtle()
                        market_map = Market(self.player, self.location, self.continent, self.playerdict)
                    else:
                        self.screen_commands.text_input("Loser", "Well make up your mind then")
                else:                  
                    self.playerdict['money'] -= self.cost
                    self.screen_commands.text_input("Purchased", f"Good purchase, your now have {self.playerdict['money']} money")
                    if item == 'luck':
                        stats = ['health', 'attack']
                        buffs = [100, 50, 30, 20, 15, 10, -10, -15, -20, -30, -50]
                        choice1 = random.choice(stats)
                        choice2 = random.choice(buffs)
                        self.screen_commands.text_input("Results", f"Your luck potion altered your {choice1} stat by {choice2}")
                        self.playerdict[f'{choice1}'] += choice2
                    else:
                        self.screen_commands.text_input(" ", f"The {item} potion has been added to your inventory")
                        self.playerdict['inventory']['potions'].append(item)
                        turtle.onscreenclick(self.void)
                    self.health.hideturtle()
                    self.escape.hideturtle()
                    self.revive.hideturtle()
                    
                    market_map = Market(self.player, self.location, self.continent, self.playerdict)

    def magic_seller(self):
        secret = self.screen_commands.text_input('Hi there', f'Hello there {self.playerdict["type"]}')
        if 'shut' in secret.lower() or 'fuck' in secret.lower():
            response = self.screen_commands.text_input('Your done', 'So you think your him huh')
            if 'no' in response.lower() or 'sorry' in response.lower():
                self.screen_commands.text_input('Go away', 'Then fuck off')
                market_map = Market(self.player, self.location, self.continent, self.playerdict)
            else:
                self.screen_commands.text_input('I see red', 'Get over here young man')
                loss.Loss()
                return
        else:
            self.screen_commands.text_input(' ', 'I sell magic potions which can grant you special abilities')
            browse = self.screen_commands.text_input(' ', "Would you like to browse some of them?[y/n]")
            if browse.lower() == 'n':
                self.screen_commands.text_input(' ', "Then get outta here")
                market_map = Market(self.player, self.location, self.continent, self.playerdict)
            else:
                self.screen_commands.text_input(' ', 'Click on the potion you wish to purchase')
                self.health = turtle.Turtle()
                self.health.speed(0)
                self.health.penup()
                self.health.goto(-2500, 300)
                self.screen.register_shape("health_pot.gif")
                self.health.shape("health_pot.gif")
                self.escape = turtle.Turtle()
                self.escape.speed(0)
                self.escape.penup()
                self.escape.goto(-2000, 300)
                self.screen.register_shape("escape_pot.gif")
                self.escape.shape("escape_pot.gif")
                self.revive = turtle.Turtle()
                self.revive.speed(0)
                self.revive.penup()
                self.revive.goto(-1500, 300)
                self.screen.register_shape("revive_pot.gif")
                self.revive.shape("revive_pot.gif")
                turtle.update()
                turtle.onscreenclick(self.purchase_potion)   

    def purchase_weapons(self, x, y):
        item = ''
        if y < -1000 or y > -300:
            turtle.onscreenclick(self.purchase_weapons)
        else:
            if x < 200 and x > -200:
                self.cost = 50
                item = 'diamond sword'
                buff = 70
            elif x < - 300:
                self.cost = 20
                item = 'iron sword'
                buff = 30
            elif x > 300:
                self.cost = 100
                item = 'copper spear'
                buff = 110
            if self.playerdict['money'] < self.cost:
                self.screen_commands.text_input(" ", "You don't have enough money to buy this weapon")
                turtle.onscreenclick(self.purchase_weapons)
            else:
                self.screen_commands.text_input("Info", f"This is a {item}, which grants you {buff} extra damage when equipped")
                certain = self.screen_commands.text_input("Are you sure", f"A {item} costs {self.cost} money and you have {self.playerdict['money']} money, are you sure you want to buy it?[y/n]")
                if certain.lower() == 'n':
                    wish = self.screen_commands.text_input(' ', 'Alright then, do you still want to make a purchase?[y/n]')
                    if wish.lower() == 'n':
                        self.screen_commands.text_input(' ', "See you later then")
                        market_map = Market(self.player, self.location, self.continent, self.playerdict)
                    else:
                        self.screen_commands.text_input(" ", "Let me know when you make a decision")
                else:                  
                    self.playerdict['money'] -= self.cost
                    self.playerdict['attack'] += buff
                    self.screen_commands.text_input("Purchased", f"Good purchase, your now have {self.playerdict['money']} money")
                    self.screen_commands.text_input("Attack buffed", f"You have equipped {item}, your attack is now {self.playerdict['attack']}")
                    turtle.onscreenclick(self.void)
                    self.irons.hideturtle()
                    self.diamonds.hideturtle()
                    self.coppers.hideturtle()
                    for i in self.playerdict['inventory']['weapons']:
                        if i == 'iron sword':
                            self.playerdict['attack'] -= 30
                        elif i == 'copper spear':
                            self.playerdict['attack'] -= 70
                        elif i == 'diamond':
                            self.playerdict['attack'] -= 110
                        self.playerdict['inventory']['weapons'].remove(i)
                    self.playerdict['inventory']['weapons'].append(item)
                    market_map = Market(self.player, self.location, self.continent, self.playerdict)

    def weapon_seller(self):
        self.screen_commands.text_input(' ', f"What's up buddy")
        self.screen_commands.text_input(' ', 'I sell various weapons which can increase your attack strength')
        browse = self.screen_commands.text_input(' ', "Would you like to choose one?[y/n]")
        if browse.lower() == 'n':
            self.screen_commands.text_input(' ', "Alright then, see ya around")
            market_map = Market(self.player, self.location, self.continent, self.playerdict)
        else:
            self.screen_commands.text_input(' ', 'Click on whichever weapon you want!')
            self.diamonds = turtle.Turtle()
            self.diamonds.speed(0)
            self.diamonds.penup()
            self.diamonds.goto(0, -700)
            self.screen.register_shape("diamond_sword.gif")
            self.diamonds.shape("diamond_sword.gif")
            self.irons = turtle.Turtle()
            self.irons.speed(0)
            self.irons.penup()
            self.irons.goto(-500, -700)
            self.screen.register_shape("iron_sword.gif")
            self.irons.shape("iron_sword.gif")
            self.coppers = turtle.Turtle()
            self.coppers.speed(0)
            self.coppers.penup()
            self.coppers.goto(500, -700)
            self.screen.register_shape("copper_spear.gif")
            self.coppers.shape("copper_spear.gif")
            turtle.update()
            turtle.onscreenclick(self.purchase_weapons)
            

    def move_left(self):
        if self.player.ycor() > 150 or self.player.ycor() < -50:
            if self.player.xcor() < -50:
                return
            else:
                self.canvas.xview_scroll(-1, "units")
                self.player.setx(self.player.xcor() - 50)
        elif self.player.xcor() < -2400:
            self.magic_seller()
        else:
            self.canvas.xview_scroll(-1, "units")
            self.player.setx(self.player.xcor() - 50)

    def move_right(self):
        if self.player.ycor() > 150 or self.player.ycor() < -50:
            if self.player.xcor() > 0:
                return
            else:
                self.canvas.xview_scroll(1, "units")
                self.player.setx(self.player.xcor() + 50)
        elif self.player.xcor() > 2500:
            self.maps()
        else:
            self.canvas.xview_scroll(1, "units")
            self.player.setx(self.player.xcor() + 50)
        
    def move_up(self):
        if self.player.xcor() < -150 or self.player.xcor() > 100:
            if self.player.ycor() > 150:
                return
            else:
                self.canvas.yview_scroll(-1, "units")
                self.player.sety(self.player.ycor() + 50)
        elif self.player.ycor() > 1250:
            self.armor_seller()
        else:
            self.canvas.yview_scroll(-1, "units")
            self.player.sety(self.player.ycor() + 50)

    def move_down(self):
        if self.player.xcor() < -150 or self.player.xcor() > 100:
            if self.player.ycor() < 0:
                return
            else:
                self.canvas.yview_scroll(1, "units")
                self.player.sety(self.player.ycor() - 50)
        elif self.player.ycor() < -900:
            self.weapon_seller()
        else:
            self.canvas.yview_scroll(1, "units")
            self.player.sety(self.player.ycor() - 50)