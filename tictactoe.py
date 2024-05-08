
    

def tic_tac_toe():
    Square_moves = ['A1','B1','C1','A2','B2','C2','A3','B3','C3']
    A1 = 'A1'
    B1 = 'B1'
    C1 = 'C1'
    A2 = 'A2'
    B2 = 'B2'
    C2 = 'C2'
    A3 = 'A3'
    B3 = 'B3'
    C3 = 'C3'

    change_squares = [A1,B1,C1,A2,B2,C2,A3,B3,C3]
    a = True
    print("I challenge you to a game of tic-tac-toe: ")
    g = input("Pick x or o: ")
    while a:
        print(A1)
        print(f"""
            {A1} / {B1} / {C1}
            {A2} / {B2} / {C2}
            {A3} / {B3} / {C3}
            """)
        if g == 'x':
            print("You go first!")
            square = input("Pick a square: ")
            if square not in Square_moves:
                print("You are acoustic")
            else:
                print("Good move")
                for i in change_squares:
                    if square == str(i):
                        print(i)
                        i = g
                        print(i)
                        print(A1)

        if g == 'o':
            print("You go after me!")
    
    
    

    
tic_tac_toe()