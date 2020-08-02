
# coding: utf-8

# In[ ]:


#game of tic tac toe by Hermes B.

#initializing initial game map
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]



def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        numberedRow = enumerate(game_map)
        print("   A  B  C")
        if not just_display:
            game_map[row][column] = player
        for count, row in numberedRow:
            print(count, row)
        print("              ")
        return game_map
    
    #Error Handling in function
    except IndexError as e:
        print("Something went wrong... did you input row/column as 0, 1, or 2?", "(", e, ")")
        
    except Exception as e:
        print("Something went very wrong!", "(", e, ")")
    
    
def win(current_game):
    #Horizontal logic
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally (⁠—)!")
    
    #Diagonal logic
    diags = []
    cols = reversed(range(len(game)))
    rows = range(len(game))
    for col, row in zip(cols, rows):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            print(f"Player {diags[0]} is the winner diagonally (/)!")
            
    diags = []    
    for index in range(len(game)):
        diags.append(game[index][index])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
            print(f"Player {diags[0]} is the winner diagonally (\\)!")
        
    #Vertical logic
    for col in range(len(game)):
        check = []
        
        for row in game:
            check.append(row[col])
        
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically (|)!")
    
    
play = True
player = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    game = game_board(game, just_display=True)
    while not game_won:
        current_player = 1
        column_choice = input("On which column do you want to play? (0, 1, 2): ")
        row_choice = input("On which row do you want to play? (0, 1, 2): ")
        game = game_board(game, current_player, row_choice, column_choice)
    
    


# In[ ]:




