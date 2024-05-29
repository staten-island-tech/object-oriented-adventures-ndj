import random

list1 = ["You are the one that they were all talking about... huh? (Y/N):", "Be fr with me, am I cute? (HELL NO/You are one of the ugliest creature I have seen!): "]

while input("Do you want to speak to this boss? (Y/N)"):
    if input == 'Y':
        print(random.choice(list1))
    if input == 'N':
        print("Have a good day!")
    else:
        print("You dumb fuck")