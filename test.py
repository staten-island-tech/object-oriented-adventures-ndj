import random


def Boss_dialogue():
    list1 = ["You are the one that they were all talking about... huh? (Y/N):", "Be fr with me, am I cute? (HELL NO/You are one of the ugliest creature I have seen!): "]
    testv1 = input("Do you want to speak to this boss? (Y/N)")
    if testv1 == 'Y':
        print(input(random.choice(list1)))
    if testv1 == 'N':
        print("Have a good day!")
    while random.choice(list1) == "You are the one that they were all talking about... huh? (Y/N):":
        if input == 'Y':
            print("Тебе предстоит непростое испытание, молодой человек --> Translator: Mr. Putin said you are up for quite a challenge young one...")
        if input == 'N':
            print("Тогда ты бесполезен, молодой --> Translator: Mr. Putin said that you are worthless young one...")
Boss_dialogue()