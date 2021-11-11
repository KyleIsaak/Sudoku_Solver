import numpy as np

#Takes in a sequence of numbers
#Takes in the size
#Return a matrix for sudoku
def ConvertTextToMatrix(text, size):
    Matrix = np.zeros((size,size))
    row = 0
    column = 0
    for number in text:
        Matrix[row][column] = number
        column += 1
        if column % size == 0:
            column = 0
            row += 1

    return Matrix

#Test cases examples
'''
with open('SudokuPuzzle1.txt') as f:
    contents = f.read()

with open('SudokuPuzzleSolution1.txt') as f:
    contentsSolution = f.read()

puzzle = ConvertTextToMatrix(contents,9)
puzzleSolution = ConvertTextToMatrix(contentsSolution,9)

print(puzzle)
print(puzzleSolution)
'''