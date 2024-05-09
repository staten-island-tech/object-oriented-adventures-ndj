import random

dialogue_spoken_to_player = input("Do you want to speak to this character? (Y/N): ")
if dialogue_spoken_to_player == 'Y':
    list1 = ["Have you heard of the scary bosses located around the world? (Yes I have/No, I havent heard of them): ", "Theres a rumour out there that the scariest boss of all is located in Russia.. (Who is he?/How do you know of him?):" , "I sure hope my husband comes back Russia.. (He is probably dead../ I couldn't care less): ", "I sure hope my husband comes back Russia.. (He is probably dead../ I couldn't care less): ", "Don't talk to me, you weakling.. (Why are you being so rude?/Im sorry for disturbing you..): ", "This generation is just a bunch of degenerates... (Who are you talking to?/Why are you so upset?): ", "I heard that there is a secret fight at the end... Try and find it before it is too late..", "I fought the strongest man... (Who is the strongest man?/You're lying): ", "Im warning you young one.. Don't be a wuss in front of those bosses... It'll ruin you.. I promise (Okay.../Why?): ", "Putin and Biden... Two of the most strongest presidents in the world... I wouldn't dare to fight them like you are.. (What kind of power do they withhold?/You aren't sigma like I am): "]
    input(random.choice(list1))
if 'Have you heard of the scary bosses locted around the world?' == 'Yes I have':
    input("There are many strong ones, but I am too cowardly to try and fight them myself. Make sure to get to them as fast as you can youngling, cuz you may be in trouble later on... (I got it!/What if I dont make it in time?): ") 
if 'There are many strong ones, but I am too cowardly to try and fight them myself. Make sure to get to them as fast as you can youngling, cuz you may be in trouble later on...' == 'What if I dont make it in time?':
    print("Hopefully you do, or else they will cause another war amongst us all... Which will mark the END of our civilization..")
if 'There are many strong ones, but I am too cowardly to try and fight them myself. Make sure to get to them as fast as you can youngling, cuz you may be in trouble later on...' == 'I got it!':
    print("Good luck youngling, and I hope to see you when you return..")
if 'Have you heard of the scary bosses located around the world' == 'No, I havent heard of them':
    print("Oh.... Just know that there will be many troubles amongst your adventure..")
if dialogue_spoken_to_player == 'N':
    list2 =["Good luck on your adventure!!","Glad you approached me..", "Return back to me when you need my help!", "Talk to me later on, youngling..."]
    print(random.choice(list2))

# npc_dialogue = input("Do you want to know some tips? (Y/N): ")
# if npc_dialogue == 'Y':
#     list3 = ["Always make sure to stock up on items before a boss fight","It is a finite, beautiful world out there... Make sure to take your time and explore the right places", "If you are playing a mini-game, always make sure that when you lose, one of your hearts gets removed", "There are merchants across every location, make sure to talk to them for items ;)", "RNG plays a big part in this game, so dont rage if you get bad luck :)","There mayyy be a secret boss at the end..."]
#     print(random.choice(list3))
# if npc_dialogue == 'N':
#     list4 = ["Okay, have a good day", "Piss off!", "I hope to talk to you again...","Good luck on your adventures!!"]
#     print(random.choice(list4))