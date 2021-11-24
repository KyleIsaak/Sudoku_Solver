#Tentative
#Breadth First Search Algorithm

from HelperFunctions import *

def BreadthFirstSearch(puzzle):

    queue = []
    visited = []

    #x = 0

    queue.append(puzzle)

    # This will run infinitely, but we break / return
    # from within the loop in all possible cases.
    while True:

        # When all states have been explored, return no solution
        if not len(queue):
            print("No Solution")
            return None

        # Pop from queue and add to visited states
        currentState = queue[0]
        del queue[0]
        visited.append(currentState)

        emptyCellIndex = getEmptyCell(currentState)

        # Return solution when found
        if ValidSolution(currentState):
            if emptyCellIndex[0] == -1:
                return currentState

        # Else, create 9 new states for each possible number
        # and add them to the queue 
        if emptyCellIndex[0] != -1:
            for i in range(0,9):
                newState = currentState.copy()
                newState[emptyCellIndex[0], emptyCellIndex[1]] = i

                #x += 1
                #print(x, " states checked")

                # if not compareStates(newState, visited):    # This isn't needed because every state created will be unique
                if ValidSolution(newState):
                    queue.append(newState)

                    print()
                    print()
                    print("State Added:")
                    print(newState)

    







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