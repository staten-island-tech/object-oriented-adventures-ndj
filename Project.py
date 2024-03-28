import json
import os


class Enemies():

    def __init__(self, Name, health, attack):
        self.Name = Name
        self.health = health
        self.attack = attack

    def dictionary(self):
        Enemies = {
            'Name' : self.Name,
            'health' : self.health,
            'attack' : self.attack,
        }
        return Enemies


with open("enemies.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

def new_Enemies():
    Name = input("Enter an Enemies Name: ")
    health = int(input("Enter their health: "))
    attack = int(input("Enter their attack: "))
    enemy = Enemies(f"{Name}", health, attack)
    data.append(enemy.dictionary())

new_Enemies()