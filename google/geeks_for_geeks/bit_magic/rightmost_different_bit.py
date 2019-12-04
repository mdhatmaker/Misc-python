import sys

# https://practice.geeksforgeeks.org/problems/longest-consecutive-1s/0
# https://wiki.python.org/moin/BitwiseOperators


# Given two numbers M and N. The task is to find the position of rightmost
# different bit in binary representation of numbers.

###############################################################################

def rightmost_different_bit(m, n):
    one = 1
    for i in range(32):
        mask = one << i
        mm = m & mask           # mask on only one bit in each number
        nn = n & mask
        if mm ^ nn != 0:        # XOR to see if bits are different
            return i+1
    return -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (11, 9, 2) )
    test_inputs.append( (52, 4, 5) )

    """ Run process on sample inputs 
    """
    for m, n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{m}, {n}')
        pos = rightmost_different_bit(m, n)
        print(f"{pos} expected: {results}\n")

