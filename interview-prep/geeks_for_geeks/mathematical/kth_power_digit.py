import sys

# https://practice.geeksforgeeks.org/problems/print-the-kth-digit/0

# Given two numbers A and B, find Kth digit from right of A^B.

###############################################################################

def get_digits(N):
    s = str(N)
    res = []
    for ch in s:
        res.append(int(ch))
    return res

def get_digit_chars(N):
    s = str(N)
    res = []
    for ch in s:
        res.append(ch)
    return res

# return Kth digit from right of A^B
def kth_digit(A, B, K):
    d = get_digits(A**B)
    n = len(d)
    return d[n-K]
    

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (3, 3, 1, 7) )
    test_inputs.append( (5, 2, 2, 2) )

    """ Run process on sample inputs 
    """
    for A, B, K, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = kth_digit(A, B, K)
        print(f"{rv} expected: {results}")
    

