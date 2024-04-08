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
turtle.write(arg=f"{starting_location.capitalize()}", align='center', font=('Times New Roman', 50, 'bold'))
turtle.goto(0,0)
continent = turtle.Turtle(f"{starting_location}.gif")
player = turtle.Turtle(f"{player['type']}.gif")
player.penup()
player.goto(600, 0)
player.speed(2)
turtle.tracer(1)
player.goto(0, 0)
time.sleep(0.3)
player.hideturtle()
time.sleep(0.2)
player.showturtle()
# a.tracer(0)
# a.listen()
# turtle.update()
# turtle.tracer(1)
# a.onkeypress(lambda: player.forward(50), key="Right")
# a.onkeypress(lambda: player.backward(50) , key="Left")




turtle.update()










turtle.mainloop()