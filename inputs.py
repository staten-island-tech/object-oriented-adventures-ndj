import turtle
import screen


class player_inputs():

    def __init__(self):
        self.conquest = screen.game_screen("world_map.gif", "Conquest")
        self.map = self.conquest.create(100, 100)
        self.conquest.text_input("How to use screens", "Utilize the scrollbars on the right and bottom of the screen to scroll up/down and left/right respectively.")
        
    def player_name(self):
        self.name = self.conquest.text_input("Name", "Enter your character's name")
        return self.name
    
    def player_age(self):
        a = True
        while a:
            try: 
                self.age = int(self.conquest.text_input("Age", "Enter your character's starting age[1-18]"))
                if self.age > 18 or self.age < 1:
                    self.conquest.text_input("Stop being annoying", "Please press OK and then enter a number from 1-18")
                else:
                    a = False
            except ValueError:
                self.conquest.text_input("Stop being dumb", "Please press OK and then enter an INTEGER")
        return self.age

    def starting_location(self):
        
        a = True
        while a:
            self.colony = self.conquest.text_input("Starting location", "Enter the continent you want to start off at:(North America/South America/Europe/Africa/Asia/Australia)")
            if self.colony.capitalize() == "North america":
                return "Welcome to your new adventure!", "North america"
            elif self.colony.capitalize() == "South america":
                return "Good luck escaping the walls!", "South america"
            elif self.colony.capitalize() == "Europe":               
                return "Get geared up for your new journey!", "Europe"
            elif self.colony.capitalize() == "Africa":
                return "Don't try and become dehydrated!", "Africa"
            elif self.colony.capitalize() == "Asia":
                return "Welcome to the largest continent in the world!", "Asia"
            elif self.colony.capitalize() == "Australia":
                return "Don't let the kangaroos hurt you!", "Australia"
            else:
                self.conquest.text_input("Don't be annoying", "Click OK and then enter ONE OF THE OPTIONS")

    def starting_location_map(self):
        self.colony = self.colony.capitalize()
        if self.colony == 'South america':
            south_america = screen.game_screen("south_america.gif", "South America")
            south_america.create(100, 100)
        elif self.colony == 'North america':
            north_america = screen.game_screen("north_america.gif", "North America")
            north_america.create(100, 100)
        elif self.colony == 'Africa':
            africa = screen.game_screen("africa.gif", "Africa")
            africa.create(100, 100)
        elif self.colony == 'Asia':
            asia = screen.game_screen("asia.gif", "Asia")
            asia.create(100, 100)
        elif self.colony == 'Europe':
            europe = screen.game_screen("europe.gif", "Europe")
            europe.create(100, 100)
        elif self.colony == 'Australia':
            Australia = screen.game_screen("oceania.gif", "Oceania")
            Australia.create(100, 100)

