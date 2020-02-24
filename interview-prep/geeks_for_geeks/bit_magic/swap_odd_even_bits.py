import sys

# https://practice.geeksforgeeks.org/problems/swap-all-odd-and-even-bits/0
# https://wiki.python.org/moin/BitwiseOperators


# TODO: this doesn't work yet!!!

# Given an unsigned integer N. The task is to swap all odd bits with even bits.
# For example, if the given number is 23 (00010111), it should be converted
# to 43(00101011). Here, every even position bit is swapped with adjacent bit
# on right side(even position bits are highlighted in binary representation of 23),
# and every odd position bit is swapped with adjacent on left side.

###############################################################################

def sbin(n):
    return "{0:b}".format(n)

# Let's assume 16-bit integer
def swap_odd_even_bits(n):
    mask = int('00000011', 2)
    for i in range(4):
        print(sbin(n), sbin(mask), sbin(n & mask))
        bits = n & mask
        swap = bits ^ mask
        print(sbin(swap))
        mask = mask << 2
    return n

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (23, 43) )
    test_inputs.append( (2, 1) )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        swap = swap_odd_even_bits(n)
        print(f"{swap} expected: {results}\n")

