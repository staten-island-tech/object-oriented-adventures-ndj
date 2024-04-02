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


f = open("enemies.json",)
data = json.load(f)
    ##Call classes in here

def new_Enemies():
    Name = input("Enter an Enemies Name: ")
    health = int(input("Enter their health: "))
    attack = int(input("Enter their attack: "))
    x = Enemies(Name, health, attack)
    data.append(x.dictionary())

new_Enemies()






