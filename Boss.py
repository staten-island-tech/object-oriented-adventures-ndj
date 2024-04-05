import json
import os


class Enemies():

    def __init__(self, Name, health, attack, continent):
        self.Name = Name
        self.health = health
        self.attack = attack
        self.continent = continent

    def dictionary(self):
        Enemies = {
            'Name' : self.Name,
            'health' : self.health,
            'attack' : self.attack,
            'continent': self.continent
        }
        return Enemies


f = open("enemies.json",)
enemies = json.load(f)
    ##Call classes in here


Name = input("Enter an Enemies Name: ")
health = int(input("Enter their health: "))
attack = int(input("Enter their attack: "))
continent = input("Enter their continent: ")
x = Enemies(Name, health, attack, continent)
enemies.append(x.__dict__)


#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(enemies)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("enemies.json")
os.rename(new_file, "enemies.json")