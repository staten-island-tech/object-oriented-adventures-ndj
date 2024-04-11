class Hangman():

    def inputs(self):
        self.input = input("Welcome to the 'Hangman' minigame, are you ready to begin?: (Y/N)")
        while self.input == 'Y':
            print("Wow, I didn't think you were brave enough for this occasion...")
            if self.input == 'N':
                print("As I thought, you were not as brave as they all say...")


        
    def words(self):
        word = ['across',  'against', 'laugh',  'middle',  'minute',  'mountain', 'ninth', 'ocean', 'office', 'parent', 'peanut', 'pencil', 'picnic', 'seconds', 'slowly', 'stories', 'student', 'sudden', 'suit', 'sure', 'swimming', 'though', 'threw', 'tired', 'well', 'whole', 'whose', 'weird', 'wouldnt', 'writing', 'written', 'wrote', 'yell', 'young']
        letterss = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while letterss == word:
            if self.count == 10:
                print("You failed to guess to guess the number of nukes I have, now you die by my NUKES!!!")
                self.death += 1 
            elif self.death == 5:
                print("You must restart back at your originated checkpoint")
            elif letterss == word:
                print("You found the word!!!")
                print('It took you', self.count, 'guesses!')
                print('You can finally move on to the next mini-game...')
                print(self.guesslist)
            elif letterss != word:
                self.count+= 1
                self.guesslist.append(self.guess)
    def tries(self):
        self.count = 1 
        self.guess = 0
        self.death = 1
        self.guesslist = []

  
    def __init__(self, letters, count, death, lives):
        self.letters = letters    
        self.count = count
        self.death = death
        self.lives = lives