import sys

# https://practice.geeksforgeeks.org/problems/number-of-paths/0

# The problem is to count all the possible paths from top left to bottom right of
# a MxN matrix with the constraints that from each cell you can either move to
# right or down.

###############################################################################

def count_paths_util(nrows, ncols, r, c):
    if r == nrows-1 and c == ncols-1:
        return 1
    elif r >= nrows or c >= ncols:
        return 0
    else:
        return count_paths_util(nrows, ncols, r+1, c) + count_paths_util(nrows, ncols, r, c+1)
    
# Only moving right/down -- top left to bottom right
def count_paths(nrows, ncols):
    count = count_paths_util(nrows, ncols, 0, 0)
    return count
    

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("3 3", 6) )
    test_inputs.append( ("2 8", 8) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        rv = count_paths(arr[0], arr[1])
        print(f"{rv} expected: {results}\n")

