import random

dialogue_spoken_to_player = input("Do you want to speak to this character? (Y/N): ")
if dialogue_spoken_to_player == 'Y':
    list1 = ["Have you heard of the scary bosses located around the world? (Yes I have/No, I havent heard of them): ", "Theres a rumour out there that the scariest boss of all is located in Russia.. (Who is he?/How do you know of him?):" , "I sure hope my husband comes back Russia.. (He is probably dead../ I couldn't care less): ", "I sure hope my husband comes back Russia.. (He is probably dead../ I couldn't care less): ", "Don't talk to me, you weakling.. (Why are you being so rude?/Im sorry for disturbing you..): ", "This generation is just a bunch of degenerates... (Who are you talking to?/Why are you so upset?): ", "I heard that there is a secret fight at the end... Try and find it before it is too late..", "I fought the strongest man... (Who is the strongest man?/You're lying): ", "Im warning you young one.. Don't be a wuss in front of those bosses... It'll ruin you.. I promise (Okay.../Why?): ", "Putin and Biden... Two of the most strongest presidents in the world... I wouldn't dare to fight them like you are.. (What kind of power do they withhold?/You aren't sigma like I am): "]
    input(random.choice(list1))
if dialogue_spoken_to_player == 'N':
    list2 =["Good luck on your adventure!!","Glad you approached me..", "Return back to me when you need my help!", "Talk to me later on, youngling..."]
    print(random.choice(list2))