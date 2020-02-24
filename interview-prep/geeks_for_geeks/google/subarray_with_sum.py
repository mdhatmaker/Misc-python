import sys


# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

# Given an unsorted array A of size N of non-negative integers, find a continuous
# sub-array which adds to a given number S.

###############################################################################

def subarray_with_sum(arr, S):
    curr_sum = arr[0]
    n = len(arr)
    start = 0
    for i in range(1, n):
        while curr_sum > S and start < i-1:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == S:
            return (start+1, i) #(start, i-1)

        if i < n:
            curr_sum += arr[i]

    return (-1, -1)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (12, "1 2 3 7 5", "2 4") )
    test_inputs.append( (15, "1 2 3 4 5 6 7 8 9 10", "1 5") )

    """ Run process on sample inputs 
    """
    for S, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{S}   {inputs}')
        rv = subarray_with_sum(arr, S)
        print(f"{rv} expected: {results}")

