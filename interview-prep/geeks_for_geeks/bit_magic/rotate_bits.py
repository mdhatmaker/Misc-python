import sys

# https://practice.geeksforgeeks.org/problems/rotate-bits/0
# https://wiki.python.org/moin/BitwiseOperators


# Given an integer N and an integer D, you are required to write a program to
# rotate the binary representation of the integer N by D digits to the left as well
# as right and print the results in decimal values after each of the rotation.
# Note: Integer N is stored using 16 bits. i.e. 12 will be stored as 0000.....001100.

###############################################################################

# Print integer as binary digits (string)
def bits(n):
    print("{0:b}".format(n))

# Assume 16-bit values when performing rotation
def rotate_bits(n, d):
    mask = (1 << d) - 1
    lowbits = n & mask
    mask = ((1 << (16)) - 1) ^ ((1 << 16-d) - 1)
    hibits = n & mask
    hibits = hibits >> (16-d)
    mask = lowbits << 16-d
    shift_right = (n >> d) | mask
    shift_left = (n << d) & 0xFFFF | hibits
    return (shift_left, shift_right)
    

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (229, 3, (1832, 40988)) )
    test_inputs.append( (28, 2, (112, 7)) )
    test_inputs.append( (50000, 4, (13580, 3125)) )

    """ Run process on sample inputs 
    """
    for n, d, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}, {d}')
        rotated = rotate_bits(n, d)
        print(f"{rotated} expected: {results}\n")

