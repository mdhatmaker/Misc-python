import sys

# https://practice.geeksforgeeks.org/problems/set-kth-bit/0
# https://wiki.python.org/moin/BitwiseOperators


# Given a number N and a value K. From the right, set the Kth bit in the binary
# representation of N. The position of LSB (or last bit) is 0, second last bit
# is 1 and so on. Also, 0 <= K < X, where X is the number of bits in the binary
# representation of N.

###############################################################################

def set_kth_bit(n, k):
    mask = 1 << k
    return n | mask
    

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (10, 2, 14) )
    test_inputs.append( (15, 3, 15) )

    """ Run process on sample inputs 
    """
    for n, k, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}, {k}')
        modded = set_kth_bit(n, k)
        print(f"{modded} expected: {results}\n")

