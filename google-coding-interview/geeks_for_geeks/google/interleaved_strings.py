import sys
from collections import deque

# https://practice.geeksforgeeks.org/problems/interleaved-strings/1

# Given three strings A, B and C your task is to complete the function isInterleave
# which returns true if C is an interleaving of A and B else returns false.
# C is said to be interleaving A and B, if it contains all characters of A and B and
# order of all characters in individual strings is preserved.

###############################################################################

# Is sc interleaving of strings sa and sb?
def is_interleaved(sa, sb, sc):
    for ch in sc:
        if len(sa) > 0 and sa[0] == ch:
            if len(sa) > 1:
                sa = sa[1:]
            else:
                sa = []
        if len(sb) > 0 and sb[0] == ch:
            if len(sb) > 1:
                sb = sb[1:]
            else:
                sb = []
    return len(sa) == 0 and len(sb) == 0


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("YX  X  XXY", False) )
    test_inputs.append( ("XY X XXY", True) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [s for s in inputs.split()]
        print(f'{arr}')
        rv = is_interleaved(arr[0], arr[1], arr[2])
        print(f"{rv} expected: {results}")

