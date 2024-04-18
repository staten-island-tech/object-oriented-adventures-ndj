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




words = ['across',  'against', 'laugh',  'middle',  'minute',  'mountain', 'ninth', 'ocean', 'office', 'parent', 'peanut', 'pencil', 'picnic', 'seconds', 'slowly', 'stories', 'student', 'sudden', 'suit', 'sure', 'swimming', 'though', 'threw', 'tired', 'well', 'whole', 'whose', 'weird', 'wouldnt', 'writing', 'written', 'wrote', 'yell', 'young']
word = random.choice(words)
spaces = ['_']* len(word)

def get_letter_position(guess, word, spaces):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character ='*'
            word = word[:index]+removed_character+word[index+1:]
            spaces[index] = guess
        else:
            index = -1
    return (word, spaces)

def win_check():
    for i in range(0, len(spaces)):
        if spaces[i] == '_':
            return -1
     
    return 1

num_turns = len(word)
for i in range(-1, num_turns):
    guess = input('Guess a character:')
    if guess in word:
        word, spaces = get_letter_position(guess, word, spaces)
        print(spaces)
    else:
        print('Sorry that letter is not in the word.')
     
    if win_check() == 1:
        print("I didn't think that you were able to figure it out...")
        break 
    print('you have '+str(num_turns - i)+' turns left.')
    print()