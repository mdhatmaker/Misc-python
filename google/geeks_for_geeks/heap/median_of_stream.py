import sys
import heapq

# https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0


# Given an input stream of N integers. The task is to insert these numbers into a new
# stream and find the median of the stream formed by each insertion of X to the new stream.

###############################################################################

def median_of_stream(arr):
    rv = []
    h = []
    heapq.heapify(h)
    for x in arr:
        heapq.heappush(h, x)
        l = len(h)
        if l % 2 == 1:
            median = heapq.nsmallest(int(l/2)+1, h)[-1]
        else:
            median = sum(heapq.nsmallest(int(l/2)+1, h)[-2:]) // 2
        rv.append(median)
    return rv

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("5 15 1 3", "5 10 5 4") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        rv = median_of_stream(arr)
        print(f"{rv} expected: {results}\n")

