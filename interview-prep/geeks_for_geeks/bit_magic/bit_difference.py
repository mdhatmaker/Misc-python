import sys

# https://practice.geeksforgeeks.org/problems/bit-difference/0
# https://wiki.python.org/moin/BitwiseOperators


# You are given two numbers A and B. Write a program to count number of bits
# needed to be flipped to convert A to B.

###############################################################################

# This is kind of a simp way to do it, but it should work.
def bit_flip_count_simp(m, n):
    count = 0
    for i in range(32):
        mask = 1 << i
        mm = m & mask           # mask on only one bit in each number
        nn = n & mask
        if mm ^ nn != 0:        # XOR to see if bits are different
            count += 1
    return count

# This is slightly better (one XOR then count the bits).
def bit_flip_count(m, n):
    xor = m ^ n
    count = 0
    while xor > 0:
        count += (xor & 1)
        xor = xor >> 1          # keep shifting xor value right until it's zero
    return count
    

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (10, 20, 4) )

    """ Run process on sample inputs 
    """
    for m, n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{m}, {n}')
        bitcount = bit_flip_count(m, n)
        print(f"{bitcount} expected: {results}\n")

