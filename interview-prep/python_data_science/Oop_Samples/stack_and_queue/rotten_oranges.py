import sys

# https://practice.geeksforgeeks.org/problems/rotten-oranges/0

# TODO: what does this have to do with stack or queue?

# Given a matrix of dimension r*c where each cell in the matrix can have
# values 0, 1 or 2 which has the following meaning:
# 0 : Empty cell 
# 1 : Cells have fresh oranges 
# 2 : Cells have rotten oranges
#
# So, we have to determine what is the minimum time required to rot all oranges.
# A rotten orange at index [i,j] can rot other fresh orange at
# indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time.
# If it is impossible to rot every orange then simply return -1.

###############################################################################

nrows = ncols = 0

def get(arr, r, c):
    return arr[r * ncols + c]

def set(arr, r, c, value):
    #print('set:', r, c, value)
    arr[r * ncols + c] = value

def print_matrix(arr):
    for r in range(nrows):
        print('| ', end='')
        for c in range(ncols):
            print(get(arr, r, c), end=' | ')
        print()

def count_fresh(arr):
    nfresh = 0
    for x in arr:
        if x == 1: nfresh += 1
    return nfresh

def check_rot(arr, r, c):
    x = get(arr, r, c)
    if x == 2:
        if r > 0 and get(arr, r-1, c) == 1:
            set(arr, r-1, c, 2)
        if r < nrows-1 and get(arr, r+1, c) == 1:
            set(arr, r+1, c, 2)
        if c > 0 and get(arr, r, c-1) == 1:
            set(arr, r, c-1, 2)
        if c < ncols-1 and get(arr, r, c+1) == 1:
            set(arr, r, c+1, 2)

def rotten_oranges(arr):
    print_matrix(arr)
    print(count_fresh(arr), arr)
    time = 1
    prev = None
    while count_fresh(arr) > 0 and arr != prev:
        time += 1
        for r in range(nrows):
            for c in range(ncols):
                check_rot(arr, r, c)
        prev = arr
        print(count_fresh(arr), arr)
    if count_fresh(arr) > 0:
        return -1
    else:
        return time

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (3, 5, "2 1 0 2 1 1 0 1 2 1 1 0 0 2 1", "2") )
    test_inputs.append( (3, 5, "2 1 0 2 1 0 0 1 2 1 1 0 0 2 1", "-1") )

    """ Run process on sample inputs 
    """
    for nrows, ncols, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        rv = rotten_oranges(arr)
        print(f"{rv} expected: {results}\n")

