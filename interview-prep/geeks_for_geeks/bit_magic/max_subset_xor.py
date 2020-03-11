import sys

# https://practice.geeksforgeeks.org/problems/maximum-subset-xor/1
# https://wiki.python.org/moin/BitwiseOperators


# Given a set of positive integers. The task is to complete the function
# maxSubarrayXOR which returns an integer denoting the maximum XOR subset
# value in the given set.

###############################################################################

# Kinda tired, so I'll do a simp version for now...
def max_subarray_xor(arr):
    maxsa = ()
    maxxor = 0
    for i1 in range(len(arr)-1):
        for i2 in range(i1+1, len(arr)):
            xor = 0
            """for j in range(i1, i2+1):
                print(j, end=' ')
                xor = xor ^ arr[j]
            if xor > maxxor:
                maxxor = xor
                maxsa = (i1, i2)
            print('    ', xor, maxxor)"""
            if arr[i1] ^ arr[i2] > maxxor:
                maxxor = arr[i1] ^ arr[i2]
                maxsa = (i1, i2)
    #print(maxxor, maxsa)
    return arr[maxsa[0]] + arr[maxsa[1]]

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("2 4 5", 7) )
    test_inputs.append( ("9 8 5", 13) )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        msx = max_subarray_xor(arr)
        print(f"{msx} expected: {results}\n")

