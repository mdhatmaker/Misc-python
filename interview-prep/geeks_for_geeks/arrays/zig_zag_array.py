import sys

# https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion/0


# TODO: finish this exercise!!!

# Given an array A (distinct elements) of size N. Rearrange the elements of array
# in zig-zag fashion. The converted array should be in form a < b > c < d > e < f.
# The relative order of elements is same in the output i.e you have to iterate on
# the original array only.


def zigzag_array(arr):
    ret = []
    
    return ret


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("4 3 7 8 6 2 1", "3 7 4 8 2 6 1") )
    test_inputs.append( ("1 4 3 2", "1 4 2 3") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        zigzag = zigzag_array(arr)
        print(f"{zigzag} expected: {results}\n")

