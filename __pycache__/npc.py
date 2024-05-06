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

    
    def dialogue_spoken():
        dialogue_spoken_to_player = input("Do you want to speak to this character? (Y/N): ")
        if dialogue_spoken_to_player == 'Y':
            npc_spoken = input("Have you heard of the scary bosses located around the world? (Yes I have/No, I definitely haven't heard of them): ")
            npc_spoken2 = input("Theres a rumour out there that the scariest boss of all is located in Russia.. (Who is he?/How do you know of him?): ")
            npc_spoken3 = input("From what i've heard, Africa is the hardest place to be in.... Try and get out of the Sahara Desert alive!!! (What kind of dangers are hiding in Africa?/OUT OF ALL PLACES.. AFRICA??): ")
            npc_spoken4 = input("I sure hope my husband comes back Russia.. (He is probably dead../ I couldn't care less): ")
            npc_spoken5 = input("Don't talk to me, you weakling.. (Why are you being so rude?/Im sorry for disturbing you..): ")
            npc_spoken6 = input("This generation is just a bunch of degenerates... (Who are you talking to?/Why are you so upset?): ")
            npc_spoken7 = input("I heard that there is a secret fight at the end... Try and find it before it is too late..")
            npc_spoken8 = input("I fought the strongest man... (Who is the strongest man?/You're lying): ")
            npc_spoken9 = input("Im warning you young one.. Don't be a wuss in front of those bosses... It'll ruin you.. I promise (Okay.../Why?): ")
        npc_spoken10 = input("Putin and Biden... Two of the most strongest presidents in the world... I wouldn't dare to fight them like you are.. (What kind of power do they withhold?/You aren't sigma like I am): ")