import sys
#import numpy as np


# https://practice.geeksforgeeks.org/problems/flood-fill-algorithm/0

# Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K),
# your task is to replace color of the given pixel and all adjacent (excluding
# diagonally adjacent) same colored pixels with the given color K.

###############################################################################

def flood_fill_util(arr2d, r, c, color, new_color):
    if c < 0 or c >= len(arr2d[0]) or r < 0 or r >= len(arr2d):
        return
    if arr2d[r][c] == color:
        arr2d[r][c] = new_color
        #print_array(arr2d)
        flood_fill_util(arr2d, r, c-1, color, new_color)
        flood_fill_util(arr2d, r, c+1, color, new_color)
        flood_fill_util(arr2d, r-1, c, color, new_color)
        flood_fill_util(arr2d, r+1, c, color, new_color)
    return

def flood_fill(arr2d, r, c, color):
    print_array(arr2d)
    old_color = arr2d[r][c]
    flood_fill_util(arr2d, r, c, old_color, color)
    return arr2d

def print_array(arr2d):
    for r in range(len(arr2d)):
        print(arr2d[r])

def to_array(arr, nrows, ncols):
    rv = []
    for r in range(nrows):
        row = []
        for c in range(ncols):
            row.append(arr[r * ncols + c])
        rv.append(row)
    return rv

###############################################################################

if __name__ == "__main__":

    # tuple format: (recurse_to_this_index, list_values, correct_value)
    # (zero means do not recurse)
    test_inputs = []
    test_inputs.append( (3, 4, "0 1 1 0 1 1 1 1 0 1 2 3", "0 1 5", "0 5 5 0 5 5 5 5 0 5 2 3") )
    test_inputs.append( (2, 2, "1 1 1 1", "0 1 8", "8 8 8 8") )
    test_inputs.append( (4, 4, "1 2 3 4 1 2 3 4 1 2 3 4 1 3 2 4", "0 2 9", "1 2 9 4 1 2 9 4 1 2 9 4 1 3 2 4"))

    """ Run process on sample inputs 
    """
    for nrows, ncols, inputs1, inputs2, results in test_inputs:
        arr = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        row, col, color = arr2
        print(f'({row},{col}) {color}   {nrows}x{ncols}  {arr}')
        arr2d = to_array(arr, nrows, ncols)
        rv = flood_fill(arr2d, row, col, color)
        #print(arr2d)
        print(f"{rv} expected: {results}\n")