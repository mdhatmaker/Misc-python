import sys

# https://practice.geeksforgeeks.org/problems/find-first-set-bit/0
# https://wiki.python.org/moin/BitwiseOperators

# Given an integer an N. The task is to print the position of first set bit found
# from right side in the binary representation of the number.

###############################################################################

def find_first_set_bit(n):
    one = 1
    for i in range(32):
        testbits = one << i
        if n & testbits != 0:
            return i+1
    return -1

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (18, 2) )
    test_inputs.append( (12, 3) )
    test_inputs.append( (0, -1) )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        pos = find_first_set_bit(n)
        print(f"{pos} expected: {results}\n")

