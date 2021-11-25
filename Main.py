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

def initialMatrix(sizeOfMatrix):
    file = sys.argv[1]
    with open(file) as f:
        contents = f.read()
    
    puzzle = ConvertTextToMatrix(contents,sizeOfMatrix)
    return puzzle

def main():
    SIZE = 9
    initalPuzzle = initialMatrix(SIZE)
    print("") #Spacer
    print("Initial Puzzle:")
    print(initalPuzzle)
    
    ########Different search techniques#########

    #A_Star_Search(initalPuzzle)
    
    #BFSPuzzle = BreadthFirstSearch(initalPuzzle)
    
    DFSPuzzle = DepthFirstSearch(initalPuzzle)
    
    #SequentialSearch(initalPuzzle)
    
    #RandomSearch(initalPuzzle)
    
    #GreedySearch(initalPuzzle)
    
    #TreeSearch(initalPuzzle)

    '''
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("BFS Puzzle:")
    print(BFSPuzzle)
    '''
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("DFS Puzzle:")
    print(DFSPuzzle)
    

main()