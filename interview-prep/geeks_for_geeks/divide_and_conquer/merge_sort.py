import sys

# https://practice.geeksforgeeks.org/problems/merge-sort/1


# The task is to complete merge() function which is used to implement Merge Sort.

###############################################################################

def merge(arr1, arr2):
    #print(arr1, ', ', arr2)
    rv = []
    """if arr1 == None:
        return arr2
    elif arr2 == None:
        return arr1"""
    i1 = i2 = 0
    while i1 < len(arr1) or i2 < len(arr2):
        if i1 >= len(arr1):
            rv.append(arr2[i2])
            i2 += 1
        elif i2 >= len(arr2):
            rv.append(arr1[i1])
            i1 += 1
        elif arr1[i1] <= arr2[i2]:
            rv.append(arr1[i1])
            i1 += 1
        else: #arr2[i2] < arr1[i1]:
            rv.append(arr2[i2])
            i2 += 1
    return rv

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    first_half = merge_sort(arr[0:mid])
    second_half = merge_sort(arr[mid:])
    print(arr, len(arr), mid, first_half, second_half)
    arr = merge(first_half, second_half)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("4 1 3 9 7", "1 3 4 7 9") )
    test_inputs.append( ("10 9 8 7 6 5 4 3 2 1", "1 2 3 4 5 6 7 8 9 10") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        sorted = merge_sort(arr)
        print(f"{sorted} expected: {results}\n")

