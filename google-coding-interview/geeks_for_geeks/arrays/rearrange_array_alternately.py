import sys

# https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately/0/


# Given a sorted array of positive integers. Your task is to rearrange the array elements
# alternatively i.e first element should be max value, second should be min value,
# third should be second max, fourth should be second min and so on...

# TODO: is there a way to perform this with the array in-place?

# Note: O(1) extra space is allowed. Also, try to modify the input array as required.

def rearrange(arr):
    ret = []
    i1 = 0
    i2 = len(arr)-1
    while i2 >= i1:
        if (i2 == i1):
            ret.append(arr[i1])
        else:
            ret.append(arr[i2])
            ret.append(arr[i1])
        i1 += 1
        i2 -= 1
    return ret

"""
def rearrange_inplace(arr):
    i1 = 0
    i2 = len(arr)-1
    while i2 >= i1:
        if (i2 == i1):
            ret.append(arr[i1])
        else:
            ret.append(arr[i2])
            ret.append(arr[i1])
        i1 += 1
        i2 -= 1
    return
"""

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 3 4 5 6", "6 1 5 2 4 3") )
    test_inputs.append( ("10 20 30 40 50 60 70 80 90 100 110", "110 10 100 20 90 30 80 40 70 50 60") )
    

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        xarr = rearrange(arr)
        #rearrange_inplace(arr)
        print(xarr, results, '\n')

