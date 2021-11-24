def getEmptyCell(puzzle):
    for rowIndex, row in enumerate(puzzle):    # For each row
        for cellIndex, cell in enumerate(row):     # For each element in given row
            if cell == 0:
                return [rowIndex, cellIndex]    # Return the index of the element

    return [-1, -1]  # Returns -1 if no empty cells were found

def CheckDuplicates(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            #Duplicate values found
            if numbers[i] == numbers[j]:
                return True
    return False

#Check if row is valid, containing unique values
def ValidRow(puzzle, row):
    if CheckDuplicates(puzzle[row]) == True:
        return False

    return True

#Check if column is valid, containing unique values
def ValidColumn(puzzle, column):
    if CheckDuplicates(puzzle[column]) == True:
        return False
        
    return True

#Check if square is valid, containing unique values
# 0 1 2
# 3 4 5
# 6 7 8
def ValidSquare(puzzle, square):
    numbers = []
    if square == 0:
        for i in range(0,3):
            for j in range(0,3):
                numbers.append(puzzle[i][j])
    elif square == 1:
        for i in range(0,3):
            for j in range(3,6):
                numbers.append(puzzle[i][j])
    elif square == 2:
        for i in range(0,3):
            for j in range(6,9):
                numbers.append(puzzle[i][j])
    elif square == 3:
        for i in range(3,6):
            for j in range(0,3):
                numbers.append(puzzle[i][j])
    elif square == 4:
        for i in range(3,6):
            for j in range(3,6):
                numbers.append(puzzle[i][j])
    elif square == 5:
        for i in range(3,6):
            for j in range(6,9):
                numbers.append(puzzle[i][j])
    elif square == 6:
        for i in range(6,9):
            for j in range(0,3):
                numbers.append(puzzle[i][j])
    elif square == 7:
        for i in range(6,9):
            for j in range(3,6):
                numbers.append(puzzle[i][j])
    elif square == 8:
        for i in range(6,9):
            for j in range(6,9):
                numbers.append(puzzle[i][j])

    if CheckDuplicates(numbers) == True:
        return False

    return True

#Loop through all conditions of a sudoku puzzle
def ValidSolution(puzzle):
    length = len(puzzle)
    for i in range(length):
        #Check all rows
        if ValidRow(puzzle, i) == False:
            return False
        #Check all columns
        if ValidColumn(puzzle, i) == False:
            return False
        #Check all squares
        if ValidSquare(puzzle, i) == False:
            return False
    return True