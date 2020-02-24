import sys

# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0


# Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array
# in ascending order.

# returns the number of zeros, ones and twos (results can be constructed using these counts)
# O(n) since we only iterate the array once
def sort_it(arr):
    count0 = count1 = count2 = 0
    for x in arr:
        if x == 0:
            count0 += 1
        elif x == 1:
            count1 += 1
        elif x == 2:
            count2 += 1
    return (count0, count1, count2)

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("0 2 1 2 0", "0 0 1 2 2") )
    test_inputs.append( ("0 1 0", "0 0 1") )
    
    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        n0, n1, n2 = sort_it(arr)
        s = '0 ' * n0 + '1 ' * n1 + '2 ' * n2
        print(s, "  expected:", results)


