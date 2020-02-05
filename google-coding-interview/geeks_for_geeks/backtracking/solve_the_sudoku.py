import sys

# https://practice.geeksforgeeks.org/problems/solve-the-sudoku/0


# Given an incomplete Sudoku configuration in terms of a 9 x 9  2-D square
# matrix (mat[][]). The task to print a solved Sudoku. For simplicity you may assume
# that there will be only one unique solution.

###############################################################################

def solve_sudoku(n):
    
    return -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (1, "[1 ]") )
    test_inputs.append( (4, "[2 4 1 3 ] [3 1 4 2 ]") )

    """
    INPUT:
    "3 0 6 5 0 8 4 0 0"
    "5 2 0 0 0 0 0 0 0"
    "0 8 7 0 0 0 0 3 1" 
    "0 0 3 0 1 0 0 8 0"
    "9 0 0 8 6 3 0 0 5"
    "0 5 0 0 9 0 6 0 0"
    "1 3 0 0 0 0 2 5 0"
    "0 0 0 0 0 0 0 7 4"
    "0 0 5 2 0 6 3 0 0"
    OUTPUT:
    "3 1 6 5 7 8 4 9 2"
    "5 2 9 1 3 4 7 6 8"
    "4 8 7 6 2 9 5 3 1"
    "2 6 3 4 1 5 9 8 7"
    "9 7 4 8 6 3 1 2 5"
    "8 5 1 7 9 2 6 4 3"
    "1 3 8 9 4 7 2 5 6"
    "6 9 2 3 5 1 8 7 4"
    "7 4 5 2 8 6 3 1 9"
    """

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        solutions = n_queens(n)
        print(f"{solutions} expected: {results}\n")

