from TextToMatrix import *
from A_Star_Search import *
from BreadthFirstSearch import *
from DepthFirstSearch import *
from SequentialSearch import *
from RandomSearch import *
from GreedySearch import *
from TreeSearch import *

import sys

#Driver program
#To run, type python Main.py (Txt file)
#Ex: python Main.py SudokuPuzzle1.txt

def initialMatrix():
    file = sys.argv[1]
    with open(file) as f:
        contents = f.read()
    
    puzzle = ConvertTextToMatrix(contents,9)
    return puzzle

def main():
    initalPuzzle = initialMatrix()
    ########Different search techniques#########

    #A_Star_Search(initalPuzzle)
    
    #BreadthFirstSearch(initalPuzzle)
    
    #DepthFirstSearch(initalPuzzle)
    
    #SequentialSearch(initalPuzzle)
    
    #RandomSearch(initalPuzzle)
    
    #GreedySearch(initalPuzzle)
    
    #TreeSearch(initalPuzzle)

    print(initalPuzzle)

main()