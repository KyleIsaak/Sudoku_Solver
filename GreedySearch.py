#Tentative
#Greedy Search Algorithm
from HelperFunctions import *
import time
# -------------------------------------------------- Get Number of Empty Squares -------------------------------------------------------------------------------------------

# Get number of empties per row
def getRowEmpties(puzzle):

    numEmpties = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for rowIndex, row in enumerate(puzzle):     # For each row
        for cellIndex, cell in enumerate(row):  # For each element in given row
            if cell == 0:
                numEmpties[rowIndex] += 1
    
    return numEmpties


# Get number of empties per column
def getColumnEmpties(puzzle):
    numEmpties = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0,9):
        for j in range(0,9):
            if puzzle[j][i] == 0:
                numEmpties[i] += 1
    
    return numEmpties

# -------------------------------------------------- Get Order of Rows / Columns -------------------------------------------------------------------------------------------


# Get order of rows from most constrained to least constrained
def getRowOrder(puzzle):

    numEmpties = getRowEmpties(puzzle)

    sortedOrder = sorted(range(len(numEmpties)), key=lambda k: numEmpties[k])
    
    #print('Row Order = ', sortedOrder)
    return sortedOrder


# Get order of columns from most constrained to least constrained
def getColumnOrder(puzzle):
   
    numEmpties = getColumnEmpties(puzzle)
    
    sortedOrder = sorted(range(len(numEmpties)), key=lambda k: numEmpties[k])
    
    #print('Column Order = ',sortedOrder)
    return sortedOrder


def getCellOrder(puzzle):

    numEmptiesByCell = []
    numEmptiesByRow = getRowEmpties(puzzle)
    numEmptiesByColumn = getColumnEmpties(puzzle)   

    for rowIndex, row in enumerate(puzzle):     # For each row
        for cellIndex, cell in enumerate(row):  # For each element in given row
            sumEmpties = numEmptiesByRow[rowIndex] + numEmptiesByColumn[cellIndex]
            if cell == 0:
                numEmptiesByCell.append([sumEmpties, [rowIndex, cellIndex]])
    
    numEmptiesByCell = sorted(numEmptiesByCell, key=lambda x: x[0])

    sortedArray = []
    for element in numEmptiesByCell:
        sortedArray.append(element[1])


    print("Sorted Array:")
    print(sortedArray)
    
    return sortedArray



# -------------------------------------------------- Get Next Empty Cell -------------------------------------------------------------------------------------------

def getEmptyCellByRow(puzzle, rowOrder):
    for rowIndex in range(0, len(rowOrder)):
        #print(rowIndex)
        #print(len(rowOrder))
        row = puzzle[rowOrder[rowIndex]]
        #print(row)
        for columnIndex, cell in enumerate(row):     # For each element in given row
            if cell == 0:
                return [rowOrder[rowIndex], columnIndex]    # Return the index of the element

    return [-1, -1]  # Returns -1 if no empty cells were found



def getEmptyCellByColumn(puzzle, columnOrder):
    for orderIndex, columnIndex in enumerate(columnOrder):
        #print(columnIndex)
        #print(len(columnOrder))
        column = []

        for i in range(0,len(columnOrder)):
            column.append(int(puzzle[i][columnIndex]))

        #print(column)
        for rowIndex, cell in enumerate(column):     # For each element in given row
            if cell == 0:
                cellIndex = [rowIndex, columnIndex]
                #print("**CELL INDEX: ", cellIndex)
                return cellIndex    # Return the index of the element
                #return [rowIndex ,columnOrder[columnIndex]]

    return [-1, -1]  # Returns -1 if no empty cells were found


def getEmptyCellByCell(puzzle, cellOrder):
    for cell in cellOrder:
        if puzzle[cell[0]][cell[1]] == 0:
            return cell      
              
    return [-1, -1]  # Returns -1 if no empty cells were found



# -------------------------------------------------- Helper Functions ----------------------------------------------------------------------------------------------

def squareChoice(row,column):
    if row <= 2 and column <= 2:
        square = 0
    elif row <= 2 and column <= 5:
        square = 1
    elif row <= 2 and column <= 8:
        square = 2

    elif row <= 5 and column <= 2:
        square = 3
    elif row <= 5 and column <= 5:
        square = 4
    elif row <= 5 and column <= 8:
        square = 5

    elif row <= 8 and column <= 2:
        square = 6
    elif row <= 8 and column <= 5:
        square = 7
    elif row <= 8 and column <= 8:
        square = 8

    return square

def squareValues(square, puzzle):
    squaredList = []
    if square == 0:
        for i in range(0,3):
            for j in range(0,3):
                squaredList.append(puzzle[i][j])
    elif square == 1:
        for i in range(0,3):
            for j in range(3,6):
                squaredList.append(puzzle[i][j])
    elif square == 2:
        for i in range(0,3):
            for j in range(6,9):
                squaredList.append(puzzle[i][j])
    elif square == 3:
        for i in range(3,6):
            for j in range(0,3):
                squaredList.append(puzzle[i][j])
    elif square == 4:
        for i in range(3,6):
            for j in range(3,6):
                squaredList.append(puzzle[i][j])
    elif square == 5:
        for i in range(3,6):
            for j in range(6,9):
                squaredList.append(puzzle[i][j])
    elif square == 6:
        for i in range(6,9):
            for j in range(0,3):
                squaredList.append(puzzle[i][j])
    elif square == 7:
        for i in range(6,9):
            for j in range(3,6):
                squaredList.append(puzzle[i][j])
    elif square == 8:
        for i in range(6,9):
            for j in range(6,9):
                squaredList.append(puzzle[i][j])    

    while 0 in squaredList:
        squaredList.remove(0)

    return squaredList


# ----------------------------------------------------------- Search Algorithms -------------------------------------------------------------------------------------

'''
def GreedySearch(puzzle):

    unvisitedValues = []
    visitedNodes = []
    chosenValues = []
    allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    rowOrder = getRowOrder(puzzle)

    while True:
        checkFlag = False

        emptyCellIndex = getEmptyCellByRow(puzzle, rowOrder)

        if emptyCellIndex[0] == -1:
            return puzzle

        #Check row
        for row in range(0,9):
            if puzzle[emptyCellIndex[0]][row] in allPossibleValues:
                allPossibleValues.remove(puzzle[emptyCellIndex[0]][row])
        #Check column
        for column in range(0,9):
            if puzzle[column][emptyCellIndex[1]] in allPossibleValues:
                allPossibleValues.remove(puzzle[column][emptyCellIndex[1]])
        #Check sqaure
        square = squareChoice(emptyCellIndex[0],emptyCellIndex[1])
        squareListValues = squareValues(square, puzzle)
        for index in range(len(squareListValues)):
            if squareListValues[index] in allPossibleValues:
                allPossibleValues.remove(squareListValues[index])

        #Backtrack here if all possible values cannot continue
       
        unvisitedValues.append(allPossibleValues)
        visitedNodes.append(emptyCellIndex)
        #print("unvisited: " + str(unvisitedValues))
        #print("empty cells: " + str(visitedNodes))
        #print("Choices" + str(allPossibleValues))
        
        while len(allPossibleValues) == 0:
            allPossibleValues = unvisitedValues.pop()
            emptyCell = visitedNodes.pop()
            puzzle[emptyCell[0]][emptyCell[1]] = 0
            #print("unvisited pop: " + str(unvisitedValues))
            #print("empty cells pop: " + str(visitedNodes))
            #print("Choices pop" + str(allPossibleValues))
            checkFlag = True

        if checkFlag == True:
            continue
        value = allPossibleValues.pop(0)
        chosenValues.append(value)

        puzzle[emptyCellIndex[0]][emptyCellIndex[1]] = value
        allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #time.sleep(1)
'''       

def GreedySearch(puzzle, greedyType: str):

    unvisitedValues = []
    visitedNodes = []
    chosenValues = []
    allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if greedyType == 'rows':
        greedyOrder = getRowOrder(puzzle)
    elif greedyType == 'columns':
        greedyOrder = getColumnOrder(puzzle)
    elif greedyType == 'cells':
        greedyOrder = getCellOrder(puzzle)
    else:
        print("INVALID GREEDY TYPE!")
        print("Types of greedy searches are as follows:")
        print("rows")
        print("columns")
        print("cells")
        return
        
    # ---------- Greedy Rows and Columns ----------
    if greedyType == 'rows' or greedyType == 'columns':
        while True:
            checkFlag = False

            if greedyType == 'rows':
                emptyCellIndex = getEmptyCellByRow(puzzle, greedyOrder)
            elif greedyType == 'columns':
                emptyCellIndex = getEmptyCellByColumn(puzzle, greedyOrder)
            

            if emptyCellIndex[0] == -1:
                return puzzle

            #Check row
            for row in range(0,9):
                if puzzle[emptyCellIndex[0]][row] in allPossibleValues:
                    allPossibleValues.remove(puzzle[emptyCellIndex[0]][row])
            #Check column
            for column in range(0,9):
                if puzzle[column][emptyCellIndex[1]] in allPossibleValues:
                    allPossibleValues.remove(puzzle[column][emptyCellIndex[1]])
            #Check sqaure
            square = squareChoice(emptyCellIndex[0],emptyCellIndex[1])
            squareListValues = squareValues(square, puzzle)
            for index in range(len(squareListValues)):
                if squareListValues[index] in allPossibleValues:
                    allPossibleValues.remove(squareListValues[index])

            #Backtrack here if all possible values cannot continue
        
            unvisitedValues.append(allPossibleValues)
            visitedNodes.append(emptyCellIndex)
            #print("unvisited: " + str(unvisitedValues))
            #print("empty cells: " + str(visitedNodes))
            #print("Choices" + str(allPossibleValues))
            
            while len(allPossibleValues) == 0:
                allPossibleValues = unvisitedValues.pop()
                emptyCell = visitedNodes.pop()
                puzzle[emptyCell[0]][emptyCell[1]] = 0
                #print("unvisited pop: " + str(unvisitedValues))
                #print("empty cells pop: " + str(visitedNodes))
                #print("Choices pop" + str(allPossibleValues))
                checkFlag = True

            if checkFlag == True:
                continue
            value = allPossibleValues.pop(0)
            chosenValues.append(value)

            puzzle[emptyCellIndex[0]][emptyCellIndex[1]] = value
            allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            #time.sleep(1)


    # ---------- Greedy Cells ----------
    if greedyType == 'cells':
         while True:
            checkFlag = False

            emptyCellIndex = getEmptyCellByCell(puzzle, greedyOrder)
          
            if emptyCellIndex[0] == -1:
                return puzzle

            #Check row
            for row in range(0,9):
                if puzzle[emptyCellIndex[0]][row] in allPossibleValues:
                    allPossibleValues.remove(puzzle[emptyCellIndex[0]][row])
            #Check column
            for column in range(0,9):
                if puzzle[column][emptyCellIndex[1]] in allPossibleValues:
                    allPossibleValues.remove(puzzle[column][emptyCellIndex[1]])
            #Check sqaure
            square = squareChoice(emptyCellIndex[0],emptyCellIndex[1])
            squareListValues = squareValues(square, puzzle)
            for index in range(len(squareListValues)):
                if squareListValues[index] in allPossibleValues:
                    allPossibleValues.remove(squareListValues[index])

            #Backtrack here if all possible values cannot continue
        
            unvisitedValues.append(allPossibleValues)
            visitedNodes.append(emptyCellIndex)
            #print("unvisited: " + str(unvisitedValues))
            #print("empty cells: " + str(visitedNodes))
            #print("Choices" + str(allPossibleValues))
            
            while len(allPossibleValues) == 0:
                allPossibleValues = unvisitedValues.pop()
                emptyCell = visitedNodes.pop()
                puzzle[emptyCell[0]][emptyCell[1]] = 0
                #print("unvisited pop: " + str(unvisitedValues))
                #print("empty cells pop: " + str(visitedNodes))
                #print("Choices pop" + str(allPossibleValues))
                checkFlag = True

            if checkFlag == True:
                continue
            value = allPossibleValues.pop(0)
            chosenValues.append(value)

            puzzle[emptyCellIndex[0]][emptyCellIndex[1]] = value
            allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            #time.sleep(1)

