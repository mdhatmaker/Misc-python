import sys

# https://practice.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not/0
# https://wiki.python.org/moin/BitwiseOperators


# Given a number N and a bit number K, check if Kth bit of N is set or not.
# A bit is called set if it is 1. Position of set bit '1' should be indexed starting
# with 0 from RSB side in binary representation of the number.
# Consider N = 4(100):  0th bit = 0, 1st bit = 0, 2nd bit = 1.

###############################################################################

def is_kth_bit_set(n, k):
    one = 1
    mask = one << k
    return (n & mask != 0)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (4, 0, False) )
    test_inputs.append( (4, 2, True) )
    test_inputs.append( (500, 3, False) )


    """ Run process on sample inputs 
    """
    for n, k, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}, {k}')
        tf = is_kth_bit_set(n, k)
        print(f"{tf} expected: {results}\n")

