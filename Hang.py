import random

class Hangman():

    def __init__(self, letters, count, guess):
        self.letters = letters    
        self.count = count
        self.guess = guess


    def inputs(self):
        input = input("Welcome to the 'Hangman' minigame, are you ready to begin?: (Y/N)")
        if input == 'Y':
            print("Wow, I didn't think you were brave enough for this occasion...")
        if input == 'N':
            print("As I thought, you were not as brave as they all say...")


    def words(self):
        word = ['across',  'against', 'laugh',  'middle',  'minute',  'mountain', 'ninth', 'ocean', 'office', 'parent', 'peanut', 'pencil', 'picnic', 'seconds', 'slowly', 'stories', 'student', 'sudden', 'suit', 'sure', 'swimming', 'though', 'threw', 'tired', 'well', 'whole', 'whose', 'weird', 'wouldnt', 'writing', 'written', 'wrote', 'yell', 'young']
        letterss = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        count = 1
        guess = 0 
        guesslist = []
        word_chooser = random.choice(word)
        while letterss != word_chooser:
            guess = print("Enter another letter to guess:")
            if count == 10:
                print("You failed to guess to guess the number of nukes I have, now you die by my NUKES!!!")
                death += 1 
            if letterss == word:
                print("You found the word!!!")
                print('It took you', count, 'guesses!')
                print('You can finally move on to the next mini-game...')
                print(guesslist)
            elif letterss != word:
                count+= 1
                print("Guess another letter!")
                guesslist.append(guess)





word = ['across','against','laugh','middle','minute','mountain','ninth','ocean','office','parent','peanut','pencil','picnic','seconds','slowly','stories','student','sudden','suit','sure','swimming','though','threw','tired','well','whole','whose','weird','wouldnt','writing','written','wrote','yell','young']
letterss = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 1
guess = 0 
guesslist = []
random_word = random.choice(word)
entrance = input("Welcome to the 'Hangman' minigame, are you ready to begin?: (Y/N)")
if input == 'Y':
        print("Wow, I didn't think you were brave enough for this occasion...")
if input == 'N':
        print("As I thought, you were not as brave as they all say...")
while random_word:    
    print(random_word)
    if letterss != random_word:
        guess = input("Enter a letter to guess: ")
        guesslist.append(guess)
        count += 1  
    elif count == 10:
        print("As I thought... You proved worthless in this game of hangman..")
    elif letterss == random_word:
        print("You found the word!!!")
        print('It took you', count, 'guesses!')
        print('You can finally move on to the next mini-game...')
        print(guesslist)
        print(random_word)