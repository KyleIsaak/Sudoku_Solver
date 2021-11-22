#Tentative
#Breadth First Search Algorithm

from HelperFunctions import getEmptyCell

def BreadthFirstSearch(puzzle):

    filledPuzzle = puzzle
    puzzleSolved = False
    emptyCellIndex = [0, 0]

    while puzzleSolved == False:
        emptyCellIndex = getEmptyCell(filledPuzzle)
        currentOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if emptyCellIndex == [-1, -1]:
            puzzleSolved == True
            break

        for element in filledPuzzle[emptyCellIndex[0]]:
            if element != 0:
                currentOptions.remove(element)

        filledPuzzle[emptyCellIndex[0], emptyCellIndex[1]] = currentOptions[0]

    return filledPuzzle