import sys

# https://practice.geeksforgeeks.org/problems/toggle-bits-given-range/0
# https://wiki.python.org/moin/BitwiseOperators
# https://www.geeksforgeeks.org/set-bits-given-range-number/


# Given a non-negative number N and two values L and R. The problem is to toggle
# the bits in the range L to R in the binary representation of N, i.e, to toggle
# bits from the rightmost Lth bit to the rightmost Rth bit. A toggle operation
# flips a bit 0 to 1 and a bit 1 to 0.

###############################################################################

def toggle_bit_range(n, l, r):
    bitrange = (((1 << (l - 1)) - 1) ^ ((1 << (r)) - 1))
    #print(bitrange, "{0:b}".format(bitrange))
    return n ^ bitrange

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (17, 2, 3, 23) )
    test_inputs.append( (50, 2, 5, 44) )

    """ Run process on sample inputs 
    """
    for n, l, r, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}, {l}, {r}')
        toggled = toggle_bit_range(n, l, r)
        print(f"{toggled} expected: {results}\n")

