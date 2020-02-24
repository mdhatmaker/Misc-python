import sys
from collections import namedtuple
Entry = namedtuple('Entry', ['value', 'idx'])


# https://practice.geeksforgeeks.org/problems/maximum-index/0

# Given an array A[] of N positive integers. The task is to find the maximum
# of j - i subjected to the constraint of A[i] <= A[j].

###############################################################################

def maximum_index(arr):
    entries = [Entry(v,i) for i,v in enumerate(arr)]
    entries.sort(key = lambda x: x.value)
    minIdx = len(entries)
    maxIJ = -1
    for e in entries:
        maxIJ = max(maxIJ, e.idx-minIdx)
        minIdx = min(minIdx, e.idx)
    return maxIJ

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("34 8 10 3 2 80 30 33 1", 6) )
    test_inputs.append( ("9 2 3 4 5 6 7 8 18 0", 8) )
    test_inputs.append( ("1 2 3 4 5 6", 5) )
    test_inputs.append( ("6 5 4 3 2 1", -1) )

    
    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{inputs}')
        rv = maximum_index(arr)
        print(f"{rv} expected: {results}")

