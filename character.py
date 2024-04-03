import json

class Create_Character():

    def __init__(self, name, age, location, player_type):
        self.name = name
        self.age = age
        self.location = location
        self.player_type = player_type
        self.conquered_nations = []
    
    def player(self):
        player = {
            'name': self.name,
            'age': self.age,
            'starting_location': self.location,
            'current_location': self.location,
            'type': self.player_type,
            'status': 'alive'
        }
        health = 100
        attack = 20
        if player['type'] == 'assassin':
            health = 70
            attack = 25
        elif player['type'] == 'royal':
            health = 80
            attack = 30
        elif player['type'] == 'peasant':
            health = 60
            attack = 15
        elif player['type'] == 'nomad':
            health = 90
            attack = 25
        player['health'] = health
        self.initial_health = health
        player['attack'] = attack
        self.player = player
        return self.player     

    def attacked(self, attack):
        self.player['health'] -= attack
        if self.player['health'] <= 0:
            self.player['status'] = 'dead'
        with open("player.json", "w") as file:
            json.dump(self.player, file)
        return self.player
    
    def healed(self, heal):
        if self.player['health'] + heal <= self.initial_health:
            self.player['health'] += heal
        else:
            self.player['health'] = self.initial_health
        with open("player.json", "w") as file:
            json.dump(self.player, file)
        return self.player
    
    def victory(self):
        with open("player.json", "r") as file:
            data = json.load(file)
        self.player['health'] = data['health']
        return self.player
    
    def defeat():
        return "Player has lost"
    
    def player_location(self, location):
        self.player['current_location'] = location
        with open("player.json", "w") as file:
            json.dump(self.player, file)
        return self.player
    
    def conquered(self, nation):
        self.conquered_nations.append(nation)
        with open("nations.json", "w") as file:
            json.dump(self.conquered_nations, file)

# Creating the player
# Character = Create_Character('Name', 18, 'US', 'royal')
# player = Character.player()
# with open("player.json", "w") as file:
#     json.dump(player, file)