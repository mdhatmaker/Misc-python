import sys
import heapq

# https://practice.geeksforgeeks.org/problems/rearrange-characters/0


# TODO: Complete this exercise!!!

# Given a string S with repeated characters (only lowercase). The task is to
# rearrange characters in a string such that no two adjacent characters are same.
# Note : It may be assumed that the string has only lowercase English alphabets.

###############################################################################

# disallow any two adjacent chars being the same
def rearrange_chars(arr):
    return -1
    rv = []
    h = []
    heapq.heapify(h)
    for x in arr:
        heapq.heappush(h, x)
        largest = heapq.nlargest(k, h)
        if len(largest) >= k:
            rv.append(largest[-1])
        else:
            rv.append(-1)
    return rv

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("geeksforgeeks", True) )
    test_inputs.append( ("bbbabaaacd", True) )
    test_inputs.append( ("bbbbb", False) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'{arr}')
        print(f'{inputs}')
        #rv = rearrange_chars(arr)
        rv = rearrange_chars(inputs)
        print(f"{rv} expected: {results}\n")

