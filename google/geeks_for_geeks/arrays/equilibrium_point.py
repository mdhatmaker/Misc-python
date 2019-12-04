import sys

# https://practice.geeksforgeeks.org/problems/equilibrium-point/0


# Given an array A of N positive numbers. The task is to find the position where
# equilibrium first occurs in the array. Equilibrium position in an array is a position
# such that the sum of elements before it is equal to the sum of elements after it.

def equilibrium(arr):
    i1 = 0
    i2 = len(arr)-1
    asum = arr[i1]
    bsum = arr[i2]
    while i1 < i2:
        #print(i1, i2, asum, bsum)
        if asum < bsum:
            i1 += 1
            asum += arr[i1]
        else:
            i2 -= 1
            bsum += arr[i2]
    ix = i1 if asum == bsum else -1
    return ix

"""def binary_search(arr, l, r, key):
    print(l, r)
    if l > r:
        return -1
    mid = int((l + r) / 2)
    if arr[mid] == key:
        return mid
    else:
        if key < mid:
            return binary_search(arr, l, mid-1, key)
        else:
            return binary_search(arr, mid+1, r, key)"""

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1", 0) )
    test_inputs.append( ("1 3 5 2 2", 2) )
    test_inputs.append( ("1 4 5 2 2", -1) )
    test_inputs.append( ("1 4 3 2 7 2 2 6", 4) )
    test_inputs.append( ("1 1 1 1 8 4", 4) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        ix = equilibrium(arr)
        value = arr[ix] if ix > -1 else -1
        print(f"A[{ix}]={value}     {ix} expected: {results}\n")

