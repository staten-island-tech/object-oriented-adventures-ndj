dialogue_spoken_to_player = input("Do you want to speak to this character? (Y/N): ")
npc_spoken = input()
while dialogue_spoken_to_player: 
    if dialogue_spoken_to_player == 'Y':
        npc_spoken = input("Have you heard of the scary bosses located around the world? (Yes I have/No, I havent heard of them): ")
    if dialogue_spoken_to_player == 'N':
        print("Good luck on your adventure!!")
    npc_spoken = input("Have you heard of the scary bosses located around the world? (Yes I have/No, I havent heard of them): ")
    if npc_spoken:
        if npc_spoken == 'Yes I have':
            input("There are many strong ones, but I am too cowardly to try and fight them myself. Make sure to get to them as fast as you can youngling, cuz you may be in trouble later on... (I got it!/What if I dont make it in time?): ") 
        if npc_spoken == 'What if I dont make it in time?':
            print("Hopefully you do, or else they will cause another war amongst us all... Which will mark the END of our civilization..")
        if npc_spoken == 'I got it!':
            print("Good luck youngling, and I hope to see you when you return..")
        if npc_spoken == 'No, I havent heard of them':
            print("Oh.... Just know that there will be many troubles amongst your adventure..")