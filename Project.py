import turtle 
import character
import inputs
import screen
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

warrior = screen.game_screen("warrior_img.gif", "Warrior")
royal = screen.game_screen("royal.gif", "Royal")
nomad = screen.game_screen("nomad.gif", "Nomad")
peasant = screen.game_screen("peasant.gif", "Peasant")
assassin = screen.game_screen("assassin.gif", "Assassin")


turtle.mainloop()