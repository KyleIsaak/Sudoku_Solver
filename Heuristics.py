#Tentative
#Heuristics

#https://stackoverflow.com/questions/36037919/heuristic-function-for-applying-a-sudoku
#Pick the most constraint option (Least numbers available)
from HelperFunctions import *
from DepthFirstSearch import *

def options(puzzle):
    dict = {}   
    heuristicPuzzle = puzzle.copy()
    unvisitedValues = []
    emptyCellIndex = getEmptyCell(heuristicPuzzle)
    while emptyCellIndex[0] != -1:
        allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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

        
        dict[tuple([emptyCellIndex[0],emptyCellIndex[1]])] = allPossibleValues
        
        unvisitedValues.append(allPossibleValues)
        
        #print("dict: " + str(dict))
    
        heuristicPuzzle[emptyCellIndex[0]][emptyCellIndex[1]] = -1

        emptyCellIndex = getEmptyCell(heuristicPuzzle)

    return dict

def getEmptyCellByNumConstraints(options):
    smallestLen = 9
    index = [-1,-1]
    for cell in options:
        if len(options[cell]) < smallestLen:
            smallestLen = len(options[cell])
            index = cell
    return [index[0], index[1]]

def Heuristics(puzzle):

    #emptyCellOptions = options(puzzle)
    #print(emptyCellOptions)
    #emptyCellIndex = getEmptyCellByNumContstraints(emptyCellOptions)
    #print(emptyCellIndex)
    
    unvisitedValues = []
    visitedNodes = []
    allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:
        checkFlag = False
        emptyCellOptions = options(puzzle)
        emptyCellIndex = getEmptyCellByNumConstraints(emptyCellOptions)
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
        value = allPossibleValues.pop()

        puzzle[emptyCellIndex[0]][emptyCellIndex[1]] = value
        allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #time.sleep(1)
    