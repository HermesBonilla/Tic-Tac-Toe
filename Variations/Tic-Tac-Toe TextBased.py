#Text-Based Tic Tac Toe by Hermes B.

#importing itertools to cycle between players
import itertools

#initializing initial game map
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]



def game_board(game_map, player=0, row=0, column=0, just_display=False):
    """
        Scalable game board size (up to 10)
    """
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Choose another space.")
            return game_map, False
        
        numberedRow = enumerate(game_map)
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in numberedRow:
            print(count, row)
        print("              ")
        return game_map, True
    
    #Error Handling in function
    except IndexError as e:
        print("Something went wrong... did you input row/column as 0, 1, or 2?", "(", e, ")")
        return game_map, False
        
    except Exception as e:
        print("Something went very wrong!", "(", e, ")")
        return game_map, False
    
    
def win(current_game):
    """
        Winning logic 
    """
    #Function condenses repeated logic
    def all_same(L):
        if L.count(L[0]) == len(L) and L[0] != 0:
            return True
        else:
            return False
        
    #Horizontal logic
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally (⁠—)!")
            return True
    
    #Diagonal logic
    diags = []
    cols = reversed(range(len(game)))
    rows = range(len(game))
    for col, row in zip(cols, rows):
        diags.append(game[row][col])
    if all_same(diags):
            print(f"Player {diags[0]} is the winner diagonally (/)!")
            return True
            
    diags = []    
    for index in range(len(game)):
        diags.append(game[index][index])
    if all_same(diags):
            print(f"Player {diags[0]} is the winner diagonally (\\)!")
            return True
        
    #Vertical logic
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically (|)!")
            return True
    return False
    
play = True
player = [1, 2]
while play:
    
    game_size = int(input("What size game of tic tac toe? (2-10) \nExample: if 3, then the game will be a 3 by 3 square! \nYour input: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"\nCurrent Player: {current_player}")
        played = False
        
        while not played:
            column_choice = int(input("On which column do you want to play? (0, 1, 2): "))
            row_choice = int(input("On which row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
            
        if win(game):
            game_won = True
            again = input("The game is over, ready for another round? (yes/no) \nYour input: ")
            if again.lower() == "yes":
                print("restarting...")
            elif again.lower() == "no":
                print("Hope you come again!")
                play = False
            else:
                print("Not a valid answer, so... Bye!")
                play = False
                
    


