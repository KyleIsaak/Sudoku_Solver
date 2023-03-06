# CMPT417-Project-Sudoku

### Setup:
The dataset can be downloaded from the following link:
https://www.kaggle.com/rohanrao/sudoku

This zip file should be extracted into the directory
that contains Main.py

run the following commands:
pip install numpy


### Running on a dataset:
Run using the following command
python Main.py FILENAME
Where FILENAME is the relative path of a CSV file containing sudoku puzzles

Example: python Main.py sudoku.csv
The example command will work if you properly downloaded and extracted the Kaggle dataset.


### Running on a single file:
python Main.py FILENAME single
Where FILENAME is the relative path of a text file containing a single sudoku puzzle

Example: python Main.py SudokuPuzzle1.txt




### Explanation of file format:
The text files are in the following format:
070000043040009610800634900094052000358460020000800530080070091902100005007040802

Where each 0 represents an empty square and each number represents a filled square, sorted by rows.

Turned into a grid, the above file would look like this:

    -------------------------
    | 0 7 0 | 0 0 0 | 0 4 3 |
    | 0 4 0 | 0 0 9 | 6 1 0 |
    | 8 0 0 | 6 3 4 | 9 0 0 |
    |-------+-------+-------|
    | 0 9 4 | 0 5 2 | 0 0 0 |
    | 3 5 8 | 4 6 0 | 0 2 0 |
    | 0 0 0 | 8 0 0 | 5 3 0 |
    |-------+-------+-------|
    | 0 8 0 | 0 7 0 | 0 9 1 |
    | 9 0 2 | 1 0 0 | 0 0 5 |
    | 0 0 7 | 0 4 0 | 8 0 2 |
    -------------------------




### Code explanation:
Feel free to take a look around the code. I have left in many of the debug functions as comments to make it easier for you to see how the code functions if you choose to uncomment them.

The dataset code compares Breadth-First, Depth-First, Greedy, and Heuristic searches based on their runtimes. For the Greedy searches, there are 3 methods that are explained below.

## Greedy searches:
# Rows:
This search attempts to complete an entire row before moving on to the next row. If no possible solutions remain for a row, the algorithm will backtrack to the previous row and try the next possible solution.

# Columns:
This is the same as rows, but the algorithm will solve by each column instead of each row.

# Cells:
This greedy algorithm will solve by each cell instead of each column / row. Goes from the top left cell to the top right cell, then moves down to the next row of cells until it reaches the end. (A cell in this case is each individual square where a number can be). This is the slowest version as it does not validate each row or column as it goes, it will only backtrack one cell at a time.
