import turtle

class game_screen():
    def __init__(self, image, title):
        self.image = image
        self.title = title
    
    def create(self):
        screen = turtle.Screen()
        screen.screensize(2600, 1400)
        screen.title(self.title)
        screen.addshape(self.image)
        turtle.shape(self.image)
        self.screen = screen
        return self.screen
    
    def text_input(self, title, text):
        input = self.screen.textinput(title=f"{title}", prompt=f"{text}")
        return input