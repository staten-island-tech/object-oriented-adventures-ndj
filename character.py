import random


class Character():

    def __init__(self, atype):
        self.type = atype
        
        
       

    def character_type(self):
        
        a = random.randint(1, 10)
        if a == 1 or a == 2 or a == 3:
            character_type = 'warrior'
        elif a == 4 or a == 5 or a == 6:
            character_type = 'nomad'
        elif a == 7 or a == 8:
            self.type = 'assassin'
        elif a == 9:
            self.type = 'royal'
        elif a == 10:
            self.type = 'peasant'
        return self.type

    def character_attributes(self):
        
        if self.type == 'warrior':
            self.health = 100
        elif self.type == 'royal':
            self.health = 80
        elif self.type == 'nomad':
            self.health = 70
        elif self.type == 'assassin':
            self.health = 60
        elif self.type == 'peasant':
            self.health = 70

Character.character_attributes('ohio')