import sys

# https://practice.geeksforgeeks.org/problems/minimize-the-sum-of-product/0

# You are given two arrays, A and B, of equal size N. The task is to find the minimum
# value of A[0] * B[0] + A[1] * B[1] + ... + A[N-1] * B[N-1], where shuffling of elements
# of arrays A and B is allowed.

###############################################################################

def minimize(arr1, arr2):
    A = sorted(arr1)
    B = sorted(arr2, reverse=True)  # pair smallest of A with largest of B
    N = len(A)
    sum = 0
    for i in range(N):     # assume A and B are same length arrays
        sum += A[i] * B[i]
    return sum

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("3 1 1", "6 5 4", 23) )
    test_inputs.append( ("6 1 9 5 4", "3 4 8 2 4", 80) )

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        print(f'{inputs1}     {inputs2}')
        rv = minimize(arr1, arr2)
        print(f"{rv} expected: {results}")
