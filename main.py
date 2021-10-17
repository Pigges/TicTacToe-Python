import os
import platform
import math

if (platform.system() == "Linux" or platform.system() == "Darwin") :
    clear = lambda: os.system('clear')
elif (platform.system() == "Windows") :
    clear = lambda: os.system('cls')

# Startup message
clear()
print("""\
***********************
Title:   Tic Tac Toe
Author:  Pigges
Version: 1.0
***********************
    X  O  O
    O  X  -
    X  -  X
***********************\
""")
input("Press ENTER to start: ")

def changeTurn(turn) :
    # turn = 0: Player X
    if (turn == 0) :
        return 1
    # turn = 1: Player O
    elif (turn == 1) :
        return 0
    # else: ERROR
    else :
        return -1

def getTurnName(turn) :
    if (turn == 0) :
        return 'X'
    elif (turn == 1) :
        return 'O'
    else :
        return "n/a"

def displayDetails(turn, turns) :
    return (f"""\
**********
Player: {getTurnName(turn)}
Turns: {turns}
**********\
    """)
    

# rederTable Function
def renderTable(table) :
    temp = ""
    x = 0
    while (x < len(table)) :
        y = 0
        temp += " "
        while (y < len(table[x])) :
            temp += f"{table[x][y]}  "
            y +=1
        x +=1
        temp += "\n"
    return temp

# Check if user wants to quit Function
def quitGame(awnser) :
    if (awnser == 'q') : 
        return True
    else : return False

# Check if awnser is valid Function
def checkValidAwnser(awnser) :
    # Check if awnser is a digit
    if (not awnser.isdigit()) :
        return False

    # Convert awnser to number
    awnser = int(awnser)

    # Check if number is between 1-9
    if (not (awnser > 0 and awnser < 10)) :
        return False
    
    return True

# Get position Function
def getPosition(awnser) :
    # Get the row
    row = int(math.ceil(awnser/3))
    # Get position on row
    position = awnser-((row-1)*3)

    return row, position

# Check if position is available Function
def CheckPosition(row, position, table) :
    # Check if position is available
    if (table[row-1][position-1] == '-') :
        return True
    else :
        return False

# Update table Function
def updateTable(row, position, table, turn) :
    table[row-1][position-1] = getTurnName(turn)
    return table

# Check if player won Function
def checkWon(table, turnName) :
    if (checkRow(table, turnName)) : return True
    if (checkCol(table, turnName)) : return True
    if (checkDiag(table, turnName)) : return True
    return False


# Search win for each row Function
def checkRow(table, turnName) :
    x = 0
    # Going through each row
    while (x < len(table)) : 
        completeRow = True
        y = 0
        # Going through each column on row
        while (y < len(table)) :
            if (not (table[x][y] == turnName)) :
                completeRow = False
                break
            y +=1
        if (completeRow) : return True
        x += 1
    return False

# Search win for each column Function
def checkCol(table, turnName) :
    y = 0
    # Going through each column
    while (y < len(table)) :
        completeCol = True
        x = 0
        # Going through each row in column
        while (x < len(table)) :
            if (not (table[x][y] == turnName)) :
                completeCol = False
                break
            x +=1
        if (completeCol) : return True
        y +=1
    return False

# Search win in each diagonal
def checkDiag(table, turnName) :
    # Top left to bottom right
    if (table[0][0] == turnName and table[1][1] == turnName and table[2][2] == turnName) : return True
    # Top right to bottom left
    if (table[0][2] == turnName and table[1][1] == turnName and table[2][0] == turnName) : return True
    # If none is true: return False
    return False

# Setting up variables
gameOn = True
table = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]
turn = 0
turns = 0

clear()
while (gameOn) :
    # Show details
    print(displayDetails(turn, turns))

    # Show the game table
    print(renderTable(table))
    awnser = input("Please enter a number between 1-9 or \"q\" to quit: ")

    # Check if user quits
    if (quitGame(awnser.lower())) :
        print("Thanks for playing!")
        gameOn = False
        continue
    
    # Check if awnser is valid
    if (not checkValidAwnser(awnser)) :
        clear()
        print("Invalid Syntax!")
        continue
    
    # Convert awnser to number
    awnser = int(awnser)

    # Get position
    row, position = getPosition(awnser)
    
    # Check if position is available
    if (not CheckPosition(row, position, table)) :
        clear()
        print("Position not available!")
        continue
    
    # Update table
    table = updateTable(row, position, table, turn)

    # Add to total turns
    turns +=1

    # Check if won
    if (checkWon(table, getTurnName(turn))) :
        clear()
        # Show details
        print(displayDetails(turn, turns))

        # Show the game table
        print(renderTable(table))

        # Show winner
        print(f"Player {getTurnName(turn)} Won!\n")
        gameOn = False
        continue
    
    # Check if tie
    if (turns == 9) :
        clear()
        # Show details
        print(displayDetails(turn, turns))

        # Show the game table
        print(renderTable(table))

        # Show tie
        print(f"Tie! No one won\n")
        gameOn = False
        continue

    # Change Player
    turn = changeTurn(turn)

    clear()