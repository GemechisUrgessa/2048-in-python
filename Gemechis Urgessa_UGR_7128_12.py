import random
import copy

# first of all lets draw a sample grid to show the player.
def samp_grid():
    grid_inist=[]
    for i in range(4):
        grid_inist.append([0]*4)
# here we use for loop to iterate through our grid
    for i in grid_inist:
        vbar = "|"
        for j in i:
            if j == 0:
                vbar +=(" "*3) +"0|"
        print(vbar)
# here we create a function to build our grid.
def grid_style():
    largernum  = 0
    for i in range(4):
        for j in range(4):
            if len("j") == len("00"):
                largernum  = len("00")
            elif len("j") == len("000"):
                largernum = len("00")
            else:
                largernum  = len("0000")

    for i in grid:
        d = "|"
        for j in i:
            if j == 0:
                d +=" " *  largernum+"|"
            else:
                d+=" "* ( largernum- len(str(j))) +str(j) + "|"
        print(d)
# here goes our function to merge left, and we use loops for itering through the row.
def rowmerge_left(row):
    j = 0
    while j <3 :
        for i in range(3, 0, -1):
            if row[i-1] == 0:
                row[i-1] = row[i]
                row[i] = 0
        j+=1
    i =0
    while i < 3:
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i + 1] = 0
        i+=1
    return row
# here will be another function which will send send the row to our rowmerge_left function so to merge the row.    
def merge_left(board):
    for i in range(4):
        board[i] = rowmerge_left(board[i])
    return board
# here will be another function where we send the row to our rowmerge_right function so to merge the row.  
def rowmerge_right(r):
    j = 0
    while j <3 :
        for i in range(3):
            if r[i+1]==0:
                r[i+1]=r[i]
                r[i]=0
        j+=1
    for i in range(3):
        if r[i+1]==r[i]:
            r[i+1]*=2
            r[i]=0            
    return r
# here will be another function where we send the row to our rowmerge_right function so to merge the row.
def merge_right(board):
    for i in range(4):
        board[i]=rowmerge_right(board[i])
    return board
# in order to merge up and down we have to transpose our grid for it will be esay to merge that way.
# so we transpose it then we merge either right or left then we transpose it back.   
def transpose(board):
    i = 0
    while i < 4:
        for j in range(i, 4):
            if  i != j:
                board[j][i],board[i][j]=board[i][j],board[j][i]     
        i+=1
    return board
# here goes our function which does merging up. 
def merge_up(board):
    board=transpose(board)
    board=merge_left(board)
    board=transpose(board)
    return board
# here goes our function which does merging down.
def merge_down(board):
    board=transpose(board)
    board=merge_right(board)
    board=transpose(board)
    return board
# to check if the game is over we use this function in which we make two copies and comper if there is no further move/.
def lost():
    board1 = copy.deepcopy(grid)
    board2 = copy.deepcopy(grid)
    board1 = merge_down(board1)
    if board1 == board2:
        board1 = merge_up(board1)
        if board1 == board2:
            board1 = merge_left(board1)
            if board1 == board2:
                board1 = merge_right(board1)
                if board1 == board2:
                    return True
    return False
# here we use a function to check wether the player has won or not.
def won():        
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True
# here we cteate a function to random numbers then assign 2 or 4 for every values it generates and we give some pirority for 2(with no reason). 
def randomnum_generator ():
    randnum = random.randint(0, 3)
    if (randnum>=0 and randnum <=2):
        return 2
    else:
        return 4
# this function detectes a random entry with value 0 then insert the values 4 and 2.       
def numgenerator():
    row = random.randint(0, 3)
    column = random.randint(0, 3) 
    while grid[row][column] != 0:
        row = random.randint(0, 3)
        column = random.randint(0, 3) 
    grid[row][column]=randomnum_generator ()
# here will be our grid with 0 values in all entry.
grid = []
i = 0
while i < 4:
    grid.append([0]*4)
    i +=1
# this function will make sure that every time random number is generated and assignes 2 or 4 for it there will be two numbers((2,2) or (2,4) or (4,4)) to be viewed.
for i in range(2):
    row = random.randint(0, 3)
    column = random.randint(0, 3)
    if grid[row][column] == 0:
        grid[row][column] = randomnum_generator()
    
# here goes our function to calculate the maximum sum of numbers the entries.
def score():
    total=0       
    for i in range(4):
        for j in range(4):
            total+=grid[i][j]
    print()
    print("Your total score is: ",total)
    print()
# here goes then intoductory parts for our plays.
print("#DEVELOPED BY Max")
print("Hi there, thanks for choosing to play this game hope you will enjoy it.")
print("The name of this game is called 2048.\nThe game is all about merging the same numbers u find until you score 2048 in a single element of the grid.\nTo play this game all you need to do is to follow the instruction, which is easy: ")
print("The instructions are as follows:")
print("press w or W to merge up.")
print("press a or A to merge left.")
print("press d or D to merge right. ")
print("press s or S to merge down.")
print("Our grid looks like the one below:")
print()
samp_grid()
print()
# here we use an input to ask the play if want to play our game.
to_start= input("To start the game press Y for Yes or N for No:")
# we will use if statement and follow what the player desires.
if to_start == "Y" or to_start == "y":
    print("Welcome to my game, following the instructions listed above enjoye the game! ")
    print()
    grid_style()
    # here goes the function for our moves plus we can call it our main function fairly we can say in which every thing is done
    def moves():
        gameover = False
        while not gameover:
            move = input("Please choose your move: ")
            validInput = True
            tempboard = copy.deepcopy(grid)
            if move == "w" or move=="W":
                merge_up(grid)
            elif move == "a" or move ==  "A":
                merge_left(grid)
            elif move == "d" or move =="D" :
                merge_right(grid)
            elif move == "s" or move == "S" :
                merge_down(grid)
            else:
                validInput = False

            if not validInput:
                print("Worng move!")
            else:
                if grid == tempboard:
                    print("No further possible move, try another!")
                else:
                    if won():
                        print("Congrats!! You have won the game")
                    else:
                        numgenerator()
                        grid_style()
                        score()
                        if lost():
                            print("BUUUUUUUUUU! YOU LOST!")
    moves()
elif to_start == "N" or to_start == "n":
    print("See you later.")
else:
    print("Invalid key")
  






