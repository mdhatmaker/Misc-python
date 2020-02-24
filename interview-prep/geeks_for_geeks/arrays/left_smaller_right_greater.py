import sys

# https://practice.geeksforgeeks.org/problems/unsorted-array/0


# Given an unsorted array of size N. Find the first element in array such that all
# of its left elements are smaller and all right elements to it are greater than it.
#
# Note: Left and right side elements can be equal to required element. And extreme
# elements cannot be required element.

def find_first_element(arr):
    ret = 0
    i1 = 0
    i2 = len(arr)-1
    xmin = arr[i1]
    xmax = arr[i2]
    while i1 < i2:
        print(f'[{i1}]={arr[i1]}  [{i2}]={arr[i2]}')
        i = i1
        while arr[i] <= xmin:
            i += 1
        i1 = i
        xmin = arr[i1]
        if i1 >= i2:
            continue
        i = i2
        while arr[i] >= xmax:
            i -= 1
        i2 = i
        xmax = arr[i2]
    print(f'[{i1}]={arr[i1]}  [{i2}]={arr[i2]}')
    return ret


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("4 2 5 7", 5) )
    test_inputs.append( ("11 9 12", -1) )
    test_inputs.append( ("4 3 2 7 8 9", 7) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        fe = find_first_element(arr)
        print(f"{fe} expected: {results}\n")

