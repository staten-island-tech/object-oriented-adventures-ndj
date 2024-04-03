import turtle 
import screen
import inputs

player_inputs = inputs.player_inputs()
name = player_inputs.player_name()
age = player_inputs.player_age()
colony = player_inputs.starting_location()
starting_location = colony[1]

turtle.mainloop()