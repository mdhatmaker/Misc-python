import sys

# https://practice.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays/0


# TODO: I still don't think my in-place merge is optimal

# Given 2 sorted arrays A and B of size N each. Print sum of middle elements of
# the array obtained after merging the given arrays.

###############################################################################

# Approach: merge the two arrays in-place, then sum the last element of A1 and first element of A2 
def sum_middle_elements(arr1, arr2):
    i1 = 0
    i2 = 0
    while i1 < len(arr1) and i2 < len(arr2):
        #print(arr1, '   ', arr2)
        if arr1[i1] <= arr2[i2]:
            i1 += 1
        else:
            arr1[i1], arr2[i2] = arr2[i2], arr1[i1]
            while arr2[i2] > arr2[i2+1]:
                arr2[i2], arr2[i2+1] = arr2[i2+1], arr2[i2]
                i2 += 1
            i2 = 0
    #print('\n', arr1, '\n', arr2)
    return arr1[len(arr1)-1] + arr2[0]

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("1 2 4 6 10", "4 5 6 9 12", 11) )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        print(f'{arr1}, {arr2}')
        midsum = sum_middle_elements(arr1, arr2)
        print(arr1, ' ', arr2)
        print(f"{midsum} expected: {results}\n")

