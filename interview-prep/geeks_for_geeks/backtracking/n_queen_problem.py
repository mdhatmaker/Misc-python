import sys

# https://practice.geeksforgeeks.org/problems/n-queen-problem/0


# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other. Given an integer n, print all distinct
# solutions to the n-queens puzzle. Each solution contains distinct board configurations
# of the n-queens’ placement, where the solutions are a permutation of [1,2,3..n] in
# increasing order, here the number in the ith place denotes that the ith-column
# queen is placed in the row with that number. For eg below figure represents a
# chessboard [3 1 4 2].
#
# | |Q| | |
# | | | |Q|
# |Q| | | |
# | | |Q| |


###############################################################################

def n_queens(n):
    
    return -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (1, "[1 ]") )
    test_inputs.append( (4, "[2 4 1 3 ] [3 1 4 2 ]") )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        solutions = n_queens(n)
        print(f"{solutions} expected: {results}\n")

