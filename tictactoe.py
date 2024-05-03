Square_moves = ['A1,B1,C1,A2,B2,C2,A3,B3,C3']
    

def tic_tac_toe():
    print("I challenge you to a game of tic-tac-toe: ")
    g = input("Pick x or o: ")
    if g == 'x':
        print("You go first!")
    if g == 'o':
        print("You go after me!")
    print("""
        A1 / B1 / C1
        A2 / B2 / C2
        A3 / B3 / C3
    """)
    

    
tic_tac_toe()