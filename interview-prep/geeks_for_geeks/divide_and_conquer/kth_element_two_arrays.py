import sys

# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array/0


# Given two sorted arrays A and B of size M and N respectively and an element k.
# The task is to find the element that would be at the kth position of the final
# sorted array.

###############################################################################

def kth_element_in_merged(arr1, arr2, k):
    i1 = 0
    i2 = 0
    while (i1+1) + (i2+1) < k:
        #print(arr1, '   ', arr2)
        if arr1[i1] < arr2[i2]:
            i1 += 1
        else:
            i2 += 1
    #print(i1, i2)
    return max(arr1[i1], arr2[i2])  # arr1[i1] if i1 > i2 else arr2[i2]   

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (5, "2 3 6 7 9", "1 4 8 10", 6) )
    test_inputs.append( (5, "1 4 8 10", "2 3 6 7 9", 6) )

    """ Run process on sample inputs 
    """
    for k, inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        print(f'{k}, {arr1}, {arr2}')
        kth = kth_element_in_merged(arr1, arr2, k)
        print(f"{kth} expected: {results}\n")

