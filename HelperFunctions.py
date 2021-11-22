def getEmptyCell(puzzle):
    for rowIndex, row in enumerate(puzzle):    # For each row
        for cellIndex, cell in enumerate(row):     # For each element in given row
            if cell == 0:
                return [rowIndex, cellIndex]    # Return the index of the element

    return [-1, -1]  # Returns -1 if no empty cells were found