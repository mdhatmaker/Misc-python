import sys
import heapq

# https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream/0


# Given an input stream of n integers, find the kth largest element for each element in the stream.

###############################################################################

def kth_largest_of_stream(arr, k):
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
    test_inputs.append( (4, "1 2 3 4 5 6", "-1 -1 -1 1 2 3") )
    test_inputs.append( (1, "3 4", "3 4") )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        rv = kth_largest_of_stream(arr, k)
        print(f"{rv} expected: {results}\n")

