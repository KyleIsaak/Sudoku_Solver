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

    """
    testPuzzle = initalPuzzle.copy()
    start_time = time.time()
    BFSPuzzle = BreadthFirstSearch(testPuzzle)
    end_time = time.time()
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("BFS Puzzle:")
    print(BFSPuzzle)
    print("--- %s seconds ---" % (end_time - start_time))
    """ 

    """
    testPuzzle = initalPuzzle.copy()
    start_time = time.time()
    DFSPuzzle = DepthFirstSearch(testPuzzle)
    end_time = time.time()
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("DFS Puzzle:")
    print(DFSPuzzle)
    print("--- %s seconds ---" % (end_time - start_time))
    

    testPuzzle = initalPuzzle.copy()
    start_time = time.time()
    #SequentialSearch(testPuzzle)
    end_time = time.time()
    """

    """
    testPuzzle = initalPuzzle.copy()
    start_time = time.time()
    RandomPuzzle = RandomSearch(testPuzzle)
    end_time = time.time()
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("Random Search Puzzle:")
    print(RandomPuzzle)
    print("--- %s seconds ---" % (end_time - start_time))
    """


    testPuzzle = initalPuzzle.copy()
    start_time = time.time()
    GreedyPuzzle = GreedySearch(testPuzzle)
    end_time = time.time()
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("Greedy Search Puzzle:")
    print(GreedyPuzzle)
    print("--- %s seconds ---" % (end_time - start_time))



    #TODO
    """
    testPuzzle = initalPuzzle.copy()
    start_time = time.time()
    TreePuzzle = TreeSearch(initalPuzzle)
    end_time = time.time()
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("Tree Search Puzzle:")
    print(TreePuzzle)
    print("--- %s seconds ---" % (end_time - start_time))
    """

    #TODO
    """
    testPuzzle = initalPuzzle.copy()
    start_time = time.time()
    AStarPuzzle = A_Star_Search(initalPuzzle)
    end_time = time.time()
    print("") #Spacer
    print("") #Spacer
    print("") #Spacer
    print("A_Star Search Puzzle:")
    print(AStarPuzzle)
    print("--- %s seconds ---" % (end_time - start_time))
    """

main()