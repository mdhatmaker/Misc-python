import sys

# https://practice.geeksforgeeks.org/problems/reverse-array-in-groups/0

# Given an array arr[] of positive integers of size N. Reverse every sub-array
# of K group elements.


def reverse_subarray_groups(arr, k):
    i1 = 0
    while i1 < len(arr):
        i2 = min(i1 + k - 1, len(arr)-1)
        reverse(arr, i1, i2)
        i1 += k
    return

def reverse(arr, l, r):
    while l < r:
        tmp = arr[l]
        arr[l] = arr[r]
        arr[r] = tmp
        l += 1
        r -= 1
    return

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (3, "1 2 3 4 5", "3 2 1 5 4") )
    test_inputs.append( (2, "10 20 30 40 50 60", "20 10 40 30 60 50") )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        reverse_subarray_groups(arr, k)
        print(f"{arr} expected: {results}\n")

