import sys

# https://practice.geeksforgeeks.org/problems/number-is-sparse-or-not/0
# https://wiki.python.org/moin/BitwiseOperators


# Given a number N, check whether it is sparse or not. A number is said to be
# a sparse number if in the binary representation of the number no two or more
# consecutive bits are set.

###############################################################################

def is_sparse_number(n):
    maxones = 0
    b = n
    count = 0
    while b > 0:
        if b & 1:
            count += 1
            if count >= 2:
                return False
        else:
            count = 0
        b = b >> 1
    return True


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (2, True) )
    test_inputs.append( (3, False) )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        tf = is_sparse_number(n)
        print(f"{tf} expected: {results}\n")

