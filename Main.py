from TextToMatrix import *
from A_Star_Search import *
from BreadthFirstSearch import *
from DepthFirstSearch import *
from SequentialSearch import *
from RandomSearch import *
from GreedySearch import *
from TreeSearch import *

import sys
import time

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



    
    start_time = time.time()
    BFSPuzzle = BreadthFirstSearch(initalPuzzle)
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("BFS Puzzle:")
    print(BFSPuzzle)
    print("--- %s seconds ---" % (time.time() - start_time))
    


    
    start_time = time.time()
    DFSPuzzle = DepthFirstSearch(initalPuzzle)
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("DFS Puzzle:")
    print(DFSPuzzle)
    print("--- %s seconds ---" % (time.time() - start_time))
    


    #SequentialSearch(initalPuzzle)
    


    """
    start_time = time.time()
    RandomPuzzle = RandomSearch(initalPuzzle)
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("Random Search Puzzle:")
    print(RandomPuzzle)
    print("--- %s seconds ---" % (time.time() - start_time))
    """



    start_time = time.time()
    #GreedySearch(initalPuzzle)
    
    #TreeSearch(initalPuzzle)

    

main()