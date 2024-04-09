import random

joe_biden = print("Joe Biden wants you to guess how much nukes he has")

number = random.randint(1, 20)
guess = 0
count = 1
guesslist=[]
while guess != number:
    guess = int(input("Enter Guess: "))
   
    if count == 3:
        print("You failed to guess to guess the number of nukes I have, now you die by my NUKES!!!")
    elif guess < number:
        print("Guess higher!")
        count += 1
        guesslist.append(guess)
    elif guess > number:
        print("Guess lower!")
        count += 1
        guesslist.append(guess)
    else:
        print("You won!")
        guesslist.append(guess)

print('It took you', count, 'guesses!')
print('You can finally move on to the next mini-game...')
print(guesslist)