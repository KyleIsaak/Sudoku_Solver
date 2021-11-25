#Tentative
#Depth First Search Algorithm

from numpy import empty
from HelperFunctions import *
import time

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

def DepthFirstSearch(puzzle):

    unvisitedValues = []
    visitedNodes = []
    chosenValues = []
    allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
    #for i in range(0,20):
        checkFlag = False
        emptyCellIndex = getEmptyCell(puzzle)
        if emptyCellIndex[0] == -1:
            return puzzle

        #print(emptyCellIndex)

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
            #print(puzzle)
            continue
        #print(checkFlag)
        #print(allPossibleValues)
        value = allPossibleValues.pop()
        chosenValues.append(value)
        #print("Chosen Values: " + str(chosenValues))

        #print(unvisitedValues)
        puzzle[emptyCellIndex[0]][emptyCellIndex[1]] = value
        allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #print(allPossibleValues)
        #print(puzzle)
        #time.sleep(1)
        
    return puzzle