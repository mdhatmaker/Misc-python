import sys

# https://practice.geeksforgeeks.org/problems/rightmost-different-bit/0
# https://wiki.python.org/moin/BitwiseOperators


# Given a number N. The task is to find the length of the longest consecutive 1s
# in its binary representation.

###############################################################################

def consecutive_ones(n):
    maxones = 0
    b = n
    count = 0
    while b > 0:
        if b & 1:
            count += 1
        else:
            maxones = max(maxones, count)
            count = 0
        b = b >> 1
    maxones = max(maxones, count)
    return maxones
    

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (14, 3) )
    test_inputs.append( (222, 4) )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        ones = consecutive_ones(n)
        print(f"{ones} expected: {results}\n")

