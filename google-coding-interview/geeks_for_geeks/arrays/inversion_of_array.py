import sys

# https://practice.geeksforgeeks.org/problems/inversion-of-array/0/


# Given an array of positive integers. The task is to find inversion count of array.

# TODO: can this be optimized? is this currently O(n^2)

# Inversion Count : For an array, inversion count indicates how far (or close) the array
# is from being sorted. If array is already sorted then inversion count is 0. If array
# is sorted in reverse order that inversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

def inversion_count(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            # so i < j for all these values; now just compare a[i] to a[j]
            if arr[i] > arr[j]:
                count += 1
    return count


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("2 4 1 3 5", 3) )
    
    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        count = inversion_count(arr)
        print(count, "  expected:", results)

