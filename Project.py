import turtle 
import character
import inputs
import screen
import json
import time

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
starting_continent = player_inputs.starting_location_map()

turtle.write(arg=f'{screen_text}', align='center', font=('Times New Roman', 50, 'normal'))
time.sleep(1)
turtle.clear()

turtle.penup()
turtle.tracer(0)
turtle.goto(0, 300)
turtle.write(arg="Your clan is...", align='center', font=('Times New Roman', 50, 'normal'))
turtle.goto(0,0)
turtle.update()

warrior = screen.game_screen("warrior_img.gif", "Warrior")
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
starting_continent.create(100, 100)
starting_continent.addshape(f"{player['type']}.gif")
turtle.shape(f"{player['type']}.gif")

turtle.update()










turtle.mainloop()