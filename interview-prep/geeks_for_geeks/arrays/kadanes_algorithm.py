import sys

# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
# https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6


# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

def kadanes_algo(arr):
    max_so_far = [0] * len(arr)
    max_so_far[0] = maxsum = arr[0]
    for i in range(1, len(arr)):
        max_so_far[i] = max(max_so_far[i-1], 0) + arr[i]
        maxsum = max(max_so_far[i], maxsum)
    return maxsum

# Non-optimized (slow) algorithm to calculate max subarray
def maxsum_subarray(arr):
    maxsum = arr[0]
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            sum = 0
            for k in range(i, j+1):
                sum += arr[k]
            if sum > maxsum:
                maxsum = sum
    return maxsum


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 3 -2 5", 9) )
    test_inputs.append( ("-1 -2 -3 -4", -1) )
    test_inputs.append( ("1 2 3 -2 5 -2 1 -4 3 14", -1) )
    test_inputs.append( ("1 2 3 -2 5 4", 0) )
    test_inputs.append( ("-4 2 3 -2 5 4 -2", 0) )

    
    for inputs, result in test_inputs:
        arr = [int(s) for s in inputs.split()]
        maxsum = kadanes_algo(arr)
        #print(maxsum, "  expected:", result)
        maxsum_slow = maxsum_subarray(arr)
        print(maxsum, "  expected:", maxsum_slow)
