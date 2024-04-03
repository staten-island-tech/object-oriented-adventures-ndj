import turtle 
import character
import inputs
import json

player_inputs = inputs.player_inputs()
name = player_inputs.player_name()
age = player_inputs.player_age()
colony = player_inputs.starting_location()
starting_location = colony[1]
Character = character.Create_Character(f'{name}', age, f'{starting_location}', 'royal')
player = Character.player()
with open("player.json", "w") as file:
    json.dump(player, file)

turtle.mainloop()