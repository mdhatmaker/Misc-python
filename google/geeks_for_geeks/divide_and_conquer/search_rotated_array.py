import sys

# https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0


# Given a sorted and rotated array A of N distinct elements which is rotated at
# some point, and given an element K. The task is to find the index of the
# given element K in the array A.

###############################################################################

def search_rotated_array(arr, k):
    
    return -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (10, "5 6 7 8 9 10 1 2 3", 5) )
    test_inputs.append( (1, "3 1 2", 1) )
    test_inputs.append( (6, "3 5 1 2", -1) )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{k}, {arr}')
        ix = search_rotated_array(arr, k)
        print(f"{ix} expected: {results}\n")

