import random
    

def tic_tac_toe():
    Square_moves = ['A1','B1','C1','A2','B2','C2','A3','B3','C3']

    change_squares = ['A1', 'B1', 'C1', 'A2','B2', 'C2', 'A3', 'B3', 'C3']
    taken_squares = []
    player_squares = []
    computer_squares = []
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

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
                        player_squares.append(a)
                        change_squares[a] = i
                        
                    a += 1
                random_square = random.randint(0, 8)

                if random_square in taken_squares:
                    random_square = random.randint(0, 8)
                    while random_square in taken_squares:
                        random_square = random.randint(0, 8)
                
                change_squares[random_square] = 'o'
                taken_squares.append(random_square)
                computer_squares.append(random_square)

        elif g == 'o':
            print("You go after me!")
            random_square = random.randint(0, 8)
            if random_square in taken_squares:
                random_square = random.randint(0, 8)
                while random_square in taken_squares:
                    random_square = random.randint(0, 8)
            
            change_squares[random_square] = 'x'
            taken_squares.append(random_square)
            computer_squares.append(random_square)
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
                        player_squares.append(a)
                        change_squares[a] = i
                        
                    a += 1

        if len(player_squares) > 2:
            print('ohio')
            check = all(e in winning_combinations for e in player_squares)
            if check == True:
                a = False
                print('You win!')

        if len(computer_squares) > 2:
            print('ohio')
            check = all(e in winning_combinations for e in computer_squares)
            if check == True:
                a = False
                print('You lose!')
                

            
    
    
    
 
    
tic_tac_toe()