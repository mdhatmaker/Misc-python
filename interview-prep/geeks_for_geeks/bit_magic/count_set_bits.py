import sys

# https://practice.geeksforgeeks.org/problems/count-total-set-bits/0
# https://wiki.python.org/moin/BitwiseOperators


# You are given a number N. Find the total count of set bits for all numbers
# from 1 to N (both inclusive).

###############################################################################

def count_set_bits(n):
    b = n
    count = 0
    while b > 0:
        count += (b & 1)
        b = b >> 1
    return count

def total_set_bits(n):
    total = 0
    for i in range(n+1):
        total += count_set_bits(i)
    return total
    

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (4, 5) )
    test_inputs.append( (17, 35) )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        setbits = total_set_bits(n)
        print(f"{setbits} expected: {results}\n")

