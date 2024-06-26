import turtle 
import character
import inputs
import screen
import json
import time
import maps

player_inputs = inputs.player_inputs()
name = player_inputs.player_name()
age = player_inputs.player_age()
colony = player_inputs.starting_location()
starting_location = colony[1]
screen_text = colony[0]
Character = character.Create_Character(f'{name}', age, f'{starting_location}')
player = Character.player()
with open("player.json", "w") as file:
    json.dump(player, file)
player_inputs.starting_location_map()

turtle.write(arg=f'{screen_text}', align='center', font=('Times New Roman', 50, 'normal'))
time.sleep(1)
turtle.clear()

turtle.penup() 
turtle.tracer(0)
turtle.goto(0, 300)
turtle.write(arg="Your clan is...", align='center', font=('Times New Roman', 50, 'normal'))
turtle.goto(0,0)
turtle.update()

warrior = screen.game_screen("warrior.gif", "Warrior")
royal = screen.game_screen("royal.gif", "Royal")
nomad = screen.game_screen("nomad.gif", "Nomad")
peasant = screen.game_screen("peasant.gif", "Peasant")
assassin = screen.game_screen("assassin.gif", "Assassin")
t_end = time.time() + 3
while time.time() < t_end:
    warrior.create(100, 100)
    time.sleep(0.15)
    peasant.create(100, 100)
    time.sleep(0.15)
    nomad.create(100, 100)
    time.sleep(0.15)
    assassin.create(100, 100)
    time.sleep(0.15)
    royal.create(100, 100)
    time.sleep(0.15)
if player['type'] == 'warrior':
    warrior.create(100, 100) 
elif player['type'] == 'peasant':
    peasant.create(100, 100)
elif player['type'] == 'nomad':
    nomad.create(100, 100)
elif player['type'] == 'assassin':
    assassin.create(100, 100)
elif player['type'] == 'royal':
    royal.create(100, 100)
turtle.tracer(0)
turtle.goto(0, -350)
turtle.write(arg=f"{player['type'].capitalize()}", align='center', font=('Times New Roman', 50, 'bold'))
turtle.goto(0,0)
turtle.update()
time.sleep(1)
turtle.clear()



new_screen = screen.game_screen(f"blank.gif", "Get ready for adventure")
a = new_screen.create(100, 100)
turtle.penup()
turtle.goto(0, 450)
location = str.split(starting_location, "_")
location1 = ""
for i in location:
    location1 = location1 + " " + i.capitalize()
turtle.write(arg=f"{location1}", align='center', font=('Times New Roman', 50, 'bold'))
turtle.goto(0,0)
continent = turtle.Turtle(f"{starting_location}.gif")
playert = turtle.Turtle(f"{player['type']}.gif")
playert.penup()
playert.goto(600, 0)
playert.speed(2)
turtle.tracer(1)
playert.goto(0, 0)
t_end = time.time() + 1.5
while time.time() < t_end:
    time.sleep(0.3)
    playert.hideturtle()
    time.sleep(0.3)
    playert.showturtle()

continent.hideturtle()
turtle.clear()
starting_map = maps.Map(f"{starting_location}_map.gif", playert, starting_location, str.strip(location1), player)


starting_map.screen.onkeypress(lambda: starting_map.move_right_maps(), key="Right")
starting_map.screen.onkeypress(lambda: starting_map.move_left_maps(), key="Left")
starting_map.screen.onkeypress(lambda: starting_map.move_up_maps(), key="Up")
starting_map.screen.onkeypress(lambda: starting_map.move_down_maps(), key="Down")




turtle.update()

 








turtle.mainloop()