import sys
from collections import deque

# https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k/0


# Given an array A and an integer K. Find the maximum for each and every contiguous
# subarray of size K.

###############################################################################

def max_of_subarrays(arr, k):
    rv = []
    q = deque()
    for x in arr:
        q.append(x)
        if len(q) == k:
            #print(q)
            rv.append(max(q))
            q.popleft()
    return rv

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (3, "1 2 3 1 4 5 2 3 6", "3 3 4 5 5 5 6") )
    test_inputs.append( (4, "8 5 10 7 9 4 15 12 90 13", "10 10 10 15 15 90 90") )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        rv = max_of_subarrays(arr, k)
        print(f"{rv} expected: {results}\n")

