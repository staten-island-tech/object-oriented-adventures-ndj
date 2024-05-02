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
        if npc_dialogue == 'N':
            print("Okay, have a good day")

    
    def dialogue_spoken():
        npc_spoken = input("Have you heard of the scary bosses located around the world? (Y/N): ")
        npc_spoken2 = input("Theres a rumour out there that the scariest boss of all is located in Russia..")
