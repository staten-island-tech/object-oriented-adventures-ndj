import turtle

class Hangman():

    def __init__(self, letters, count, death):
        self.letters = letters    
        self.count = count
        self.death = death
     
    def words(self):
        word = ['across',  'against', 'laugh',  'middle',  'minute',  'mountain', 'ninth', 'ocean', 'office', 'parent', 'peanut', 'pencil', 'picnic', 'seconds', 'slowly', 'stories', 'student', 'sudden', 'suit', 'sure', 'swimming', 'though', 'threw', 'tired', 'well', 'whole', 'whose', 'weird', 'wouldnt', 'writing', 'written', 'wrote', 'yell', 'young']
        letterss = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
        while letterss == word:
            if letterss == word:
                print("You found the word!!!")
            else:
                print("You failed to guess the word!!!")
    
    
    def create(self, width, height, screen):
        screen = turtle.Screen()
        screen.screensize(width, height)
        screen.title(self.title)