import sys

# https://practice.geeksforgeeks.org/problems/trapping-rain-water/0

# Given an array arr[] of N non-negative integers representing height of blocks
# at index i as Ai where the width of each block is 1. Compute how much water can
# be trapped in between blocks after raining.
#
# Bars for input: {3, 0, 0, 2, 0, 4}
# Total trapped water = 3 + 3 + 1 + 3 = 10

def trapped_water(arr):
    total = 0
    i1 = 0
    i2 = 1
    #while i2 < len(arr):
    #    if arr[i2]
    return total


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("7 4 0 9", 10) )
    test_inputs.append( ("6 9 9", 0) )
    test_inputs.append( ("3, 0, 0, 2, 0, 4", 10))
    
    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        water = trapped_water(arr)
        print(f"{water} expected: {results}\n")

