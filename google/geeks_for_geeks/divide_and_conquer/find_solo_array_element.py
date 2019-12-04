import sys

# https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array/0


# Given a sorted array A, size N, of integers; every element appears twice except
# for one. Find that element that appears once in array.

###############################################################################

def find_solo_element(arr):
    
    return -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 1 2 2 3 3 4 50 50 65 65", 4) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        solo = find_solo_element(arr)
        print(f"{solo} expected: {results}\n")

