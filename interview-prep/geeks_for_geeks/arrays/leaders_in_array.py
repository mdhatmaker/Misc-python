import sys

# https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

# Given an array of positive integers. Your task is to find the leaders in the array.
# Note: An element of array is leader if it is greater than or equal to all the elements
# to its right side. Also, the rightmost element is always a leader. 

def get_leaders(arr):
    ret = []
    max_so_far = -1
    for x in arr[::-1]:
        if x > max_so_far:
            ret.insert(0, x)
            max_so_far = x
    return ret


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("16 17 4 3 5 2", "17 5 2") )
    test_inputs.append( ("1 2 3 4 0", "4 0") )
    test_inputs.append( ("7 4 5 7 3", "7 7 3") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        leaders = get_leaders(arr)
        print(f"{leaders} expected: {results}\n")

