import random
    

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

    change_squares = ['A1', 'B1', 'C1', 'A2','B2', 'C2', 'A3', 'B3', 'C3']
    taken_squares = []
    a = True
    print("I challenge you to a game of tic-tac-toe: ")
    g = input("Pick x or o: ")
    while a:
        print(f"""
            {change_squares[0]} / {change_squares[1]} / {change_squares[2]}
            {change_squares[3]} / {change_squares[4]} / {change_squares[5]}
            {change_squares[6]} / {change_squares[7]} / {change_squares[8]}
            """)
        if g == 'x':
            print("You go first!")
            square = input("Pick a square: ")
            if square not in Square_moves:
                print("You are acoustic")
            else:
                print("Good move")
                a = 0
                for i in change_squares:
                    if square == str(i):
                        i = g
                        taken_squares.append(a)
                        change_squares[a] = i
                        
                    a += 1
                random_square = random.randint(0, 8)

                if random_square in taken_squares:
                    random_square = random.randint(0, 8)
                    while random_square in taken_squares:
                        random_square = random.randint(0, 8)
                
                change_squares[random_square] = 'o'

        elif g == 'o':
            print("You go after me!")
            random_square = random.randint(0, 8)
            if random_square in taken_squares:
                random_square = random.randint(0, 8)
                while random_square in taken_squares:
                    random_square = random.randint(0, 8)
            
            change_squares[random_square] = 'x'
            print(f"""
            {change_squares[0]} / {change_squares[1]} / {change_squares[2]}
            {change_squares[3]} / {change_squares[4]} / {change_squares[5]}
            {change_squares[6]} / {change_squares[7]} / {change_squares[8]}
            """)
            square = input("Pick a square: ")
            if square not in Square_moves:
                print("You are acoustic")
            else:
                print("Good move")
                a = 0
                for i in change_squares:
                    if square == str(i):
                        i = g
                        taken_squares.append(a)
                        change_squares[a] = i
                        
                    a += 1
                

            
    
    
    

    
tic_tac_toe()