#Tentative
#Breadth First Search Algorithm

from HelperFunctions import getEmptyCell

def BreadthFirstSearch(puzzle):

    filledPuzzle = puzzle
    puzzleSolved = False
    emptyCellIndex = [0, 0]

    while puzzleSolved == False:
        emptyCellIndex = getEmptyCell(puzzle)

        if emptyCellIndex == [-1, -1]:
            puzzleSolved == True
            break

        filledPuzzle[emptyCellIndex[0], emptyCellIndex[1]] = 99

    return filledPuzzle