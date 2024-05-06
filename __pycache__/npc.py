class NPC():
    def __init__(self, dialogue, tips):
        self.dialogue = dialogue
        self.tips = tips
    
    def dialogue_player():
        npc_dialogue = input("Do you want to know some tips? (Y/N): ")
        if npc_dialogue == 'Y':
            print("Always make sure to stock up on items before a boss fight")
            print("It is a finite, beautiful world out there... Make sure to take your time and explore the right places")
            print("If you are playing a mini-game, always make sure that when you lose, one of your hearts gets removed")
            print("There are merchants across every location, make sure to talk to them for items ;)")
            print("RNG plays a big part in this game, so dont rage if you get bad luck :)")
            print("There mayyy be a secret boss at the end...")
        if npc_dialogue == 'N':
            print("Okay, have a good day")
            print("Piss off!")
            print("I hope to talk to you again...")
            print("Good luck on your adventures!!")

    
    def dialogue_spoken():
        dialogue_spoken_to_player = input("Do you want to speak to this character? (Y/N): ")
        while dialogue_spoken_to_player: 
            if dialogue_spoken_to_player == 'Y':
                npc_spoken = input("Have you heard of the scary bosses located around the world? (Yes I have/No, I havent heard of them): ")
                npc_spoken2 = input("Theres a rumour out there that the scariest boss of all is located in Russia.. (Who is he?/How do you know of him?): ")
                npc_spoken3 = input("From what i've heard, Africa is the hardest place to be in.... Try and get out of the Sahara Desert alive!!! (What kind of dangers are hiding in Africa?/OUT OF ALL PLACES.. AFRICA??): ")
                npc_spoken4 = input("I sure hope my husband comes back Russia.. (He is probably dead../ I couldn't care less): ")
                npc_spoken5 = input("Don't talk to me, you weakling.. (Why are you being so rude?/Im sorry for disturbing you..): ")
                npc_spoken6 = input("This generation is just a bunch of degenerates... (Who are you talking to?/Why are you so upset?): ")
                npc_spoken7 = input("I heard that there is a secret fight at the end... Try and find it before it is too late..")
                npc_spoken8 = input("I fought the strongest man... (Who is the strongest man?/You're lying): ")
                npc_spoken9 = input("Im warning you young one.. Don't be a wuss in front of those bosses... It'll ruin you.. I promise (Okay.../Why?): ")
                npc_spoken10 = input("Putin and Biden... Two of the most strongest presidents in the world... I wouldn't dare to fight them like you are.. (What kind of power do they withhold?/You aren't sigma like I am): ")
            if dialogue_spoken_to_player == 'N':
                print("Good luck on your adventure!!")
                print("Glad you approached me..")
                print("Return back to me when you need my help!")
                print("Talk to me later on, youngling...")
        while dialogue_spoken_to_player(npc_spoken) == 'Y':
            if  dialogue_spoken_to_player(npc_spoken) == 'Yes I have':
                input("There are many strong ones, but I am too cowardly to try and fight them myself. Make sure to get to them as fast as you can youngling, cuz you may be in trouble later on... (I got it!/What if I dont make it in time?): ")
                if dialogue_spoken_to_player(npc_spoken) == 'What if I dont make it in time?':
                    print("Hopefully you do, or else they will cause another war amongst us all... Which will mark the END of our civilization..")
            if dialogue_spoken_to_player(npc_spoken) == 'I got it!':
                print("Good luck youngling, and I hope to see you when you return..")
            if dialogue_spoken_to_player(npc_spoken) == 'No, I havent heard of them':
                print("Oh.... Just know that there will be many troubles amongst your adventure..")