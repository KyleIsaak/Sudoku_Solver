#Tentative 
#Random Search Algorithm

from DepthFirstSearch import squareChoice
from DepthFirstSearch import squareValues
from HelperFunctions import *
import random

def possibleSolution(puzzle):
    emptyCellIndex = getEmptyCell(puzzle)

    while emptyCellIndex[0] != -1:
        allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        emptyCellIndex = getEmptyCell(puzzle)
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

        #All possible values will only be a subset of possible numbers 
        #We now choose one of those random numbers to place
       
        if len(allPossibleValues) == 0:
            return puzzle

        randomValue = random.choice(allPossibleValues)

        puzzle[emptyCellIndex[0]][emptyCellIndex[1]] = randomValue

def RandomSearch(puzzle):
    zeroIsPresent = True
    while zeroIsPresent == True:
        zeroIsPresent = False
        newPuzzle = possibleSolution(puzzle.copy())
        #print(newPuzzle)
        for i in range(9):
            for j in range(9):
                if newPuzzle[i][j] == 0:
                    zeroIsPresent = True
    return newPuzzle
