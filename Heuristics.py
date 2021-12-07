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

def Heuristics(puzzle):
    emptyOptions = options(puzzle)
        
    print(emptyOptions)

    print(emptyOptions[(0,0)])
    print("Currently the puzzle is...")
    print(puzzle)
    return puzzle