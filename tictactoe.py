def display_menu():
    print("Welcome to Tic Tac Toe!")
    print("P: Play game")
    print("G: Grid size")
    print("Q: Quit")

def validate_position(position, grid):
    valid = True
    if position.count(",") != 1:
        valid = False
    
    position = position.split(",")
    x = int(position[0])
    y = int(position[-1])
    
    if len(position) != 2:
        valid = False
    
    if position[0].isdigit() == False or position[-1].isdigit() == False:
        valid = False
    
    if grid[y][x] != "#":
        valid = False

    return valid

def make_grid():
    grid_dimensions = input("Enter grid dimensions e.g 4x3 (row x columns): ")
    grid_dimensions = grid_dimensions.split("x")
    rows = int(grid_dimensions[0])
    columns = int(grid_dimensions[-1])
    grid = []

    for i in range(rows):
        grid.append([])
        for v in range(columns):
            grid[i].append("#")
    
    return grid

def display_grid(grid):
    for row in grid:
        print()
        for column in row:
            print(column, end="")
    print("\n")

def check_grid(grid):
    
    result = ""

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            vertical = 0
            positive_diag = 0
            negative_diag = 0
            horizontal = 0
            if not((row == 0 and column == 0) or (row == len(grid) - 1 and column == 0) or (row == 0 and column == len(grid[0]) - 1) or (row == len(grid) - 1 and column == len(grid[0]) - 1)):
                if grid[row][column] == "O":
                    try:
                        if row != 0 and row != len(grid) - 1:
                            if grid[row - 1][column] == "O":
                                vertical += 1
                            if grid[row + 1][column] == "O":
                                vertical += 1
                        if column != 0 and column != len(grid[0]) - 1:
                            if grid[row][column - 1] == "O":
                                horizontal += 1
                            if grid[row][column + 1] == "O":
                                horizontal += 1
                        if row != 0 and row != len(grid) - 1 and column != 0 and column != len(grid[0]) - 1:
                            if grid[row - 1][column + 1] == "O":
                                positive_diag += 1
                            if grid[row + 1][column - 1] == "O":
                                positive_diag += 1
                            if grid[row - 1][column - 1] == "O":
                                negative_diag += 1
                            if grid[row + 1][column + 1] == "O":
                                negative_diag += 1
                    except:
                        pass

                    if vertical == 2 or positive_diag == 2 or negative_diag == 2 or horizontal == 2:
                        result = "Player 1"
                
                if grid[row][column] == "X":
                    try:
                        if row != 0 and row != len(grid) - 1:
                            if grid[row - 1][column] == "X":
                                vertical += 1
                            if grid[row + 1][column] == "X":
                                vertical += 1
                        if column != 0 and column != len(grid[0]) - 1:
                            if grid[row][column - 1] == "X":
                                horizontal += 1
                            if grid[row][column + 1] == "X":
                                horizontal += 1
                        if row != 0 and row != len(grid) - 1 and column != 0 and column != len(grid[0]) - 1:
                            if grid[row - 1][column + 1] == "X":
                                positive_diag += 1
                            if grid[row + 1][column - 1] == "X":
                                positive_diag += 1
                            if grid[row - 1][column - 1] == "X":
                                negative_diag += 1
                            if grid[row + 1][column + 1] == "X":
                                negative_diag += 1
                    except:
                        pass

                    if vertical == 2 or positive_diag == 2 or negative_diag == 2 or horizontal == 2:
                        result = "Player 2"

    return result
            
def play_round(grid):
    round_over = False
    turn = 1
    result = ""
    count = 1
    while round_over == False:
        valid_position =  False
        display_grid(grid)

        if turn % 2 != 0:
            turn = 1
        else:
            turn = 2

        while valid_position == False:
            player_move = input(f"Player {turn}'s turn (x,y): ")
            valid_position = validate_position(player_move, grid)
            if valid_position == False:
                print("Invalid position.")
            
        x =int(player_move[0])
        y = int(player_move[-1])
        grid[y][x] = "O" if turn == 1 else "X"

        #Check the grid every turn to see if anyone wins
        result = check_grid(grid)
        if result != "":
            display_grid(grid)
            print(f"{result} wins!")
            print()
            round_over = True

        if count == len(grid) * len(grid[0]):
            print("It's a tie!!")
            round_over = True
            
        turn += 1
        count += 1
        
        

def game():
    #Initializing local variables
    high_score = 0
    grid = [["#","#","#"],["#","#","#"],["#","#","#"]]
    quit = False

    while quit == False:
        display_menu()
        choice = input("Enter option: ").upper()
    
        if choice == "P":
            play_round(grid)
            grid = [["#","#","#"],["#","#","#"],["#","#","#"]]
        elif choice == "G":
            grid = make_grid()
        elif choice == "Q":
            quit = True

game()
print("exited")