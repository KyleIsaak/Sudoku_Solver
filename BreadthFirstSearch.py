#Tentative
#Breadth First Search Algorithm

from HelperFunctions import *

def BreadthFirstSearch(puzzle):


    queue = []
    visited = []

    queue.append(puzzle)

    # This will run infinitely, but we break / return
    # from within the loop in all possible cases.
    while True:

        # When all states have been explored, return no solution
        if queue is empty:
            print("No Solution")
            return None

    # Pop from queue and add to visited states
    currentState = queue[0]
    queue.remove[0]
    visited.append(currentState)

    # Return solution when found
    if ValidSolution(currentState):
        if getEmptyCell(currentState) == [-1, -1]:
            return currentState

    # Else, move one step forward and add to queue
    #****CODE FOR FUTURE STATES HERE*****

    emptyCellIndex = getEmptyCell(currentState)

    for i in range(0,9):
        newState = currentState
        currentState[emptyCellIndex] = i
        if ValidSolution(newState)
            queue.append(newState)

"""
    while puzzleSolved == False:
        emptyCellIndex = getEmptyCell(filledPuzzle)
        currentOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if emptyCellIndex == [-1, -1]:
            puzzleSolved == True
            break

        for element in filledPuzzle[emptyCellIndex[0]]: # Check what numbers are in that row
            if element != 0:
                currentOptions.remove(element)
                filledPuzzle[emptyCellIndex[0], emptyCellIndex[1]] = currentOptions[0]
"""

    return filledPuzzle