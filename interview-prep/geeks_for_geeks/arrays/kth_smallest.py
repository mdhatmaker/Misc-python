import sys

# https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
# Time complexity of various Python operations (list, collections.deque, set, dict):
# https://wiki.python.org/moin/TimeComplexity


# TODO: does the use of max(smallest) make this worse than O(n)?

# Given an array arr[] and a number K where K is smaller than size of array,
# the task is to find the Kth smallest element in the given array.
# It is given that all array elements are distinct.
#
# Expected Time Complexity: O(n)

def kth_smallest(arr, k):
    max_smallest = 0
    smallest = {}
    for x in arr:
        if len(smallest) < k:
            smallest[x] = 1
            max_smallest = max(x, max_smallest)
        elif x < max_smallest:
            smallest.pop(max_smallest)
            smallest[x] = 1
            max_smallest = max(smallest)
    return max_smallest

def kth_smallest_slow(arr, k):
    smallest = []
    for x in arr:
        if len(smallest) < k:
            smallest.append(x)
        elif x < max(smallest):
            smallest.remove(max(smallest))
            smallest.append(x)
    return max(smallest)


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (3, "7 10 4 3 20 15", 7) )
    test_inputs.append( (4, "7 10 4 20 15", 15) )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(k, arr)
        kth = kth_smallest_slow(arr, k)
        print(f"{kth} expected: {results}")
        kth = kth_smallest(arr, k)
        print(f"{kth} expected: {results}\n")
