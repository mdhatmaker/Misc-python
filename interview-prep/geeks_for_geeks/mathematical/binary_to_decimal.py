import sys

# https://practice.geeksforgeeks.org/problems/binary-number-to-decimal-number/0

# Given a binary number B, print its decimal equivalent.

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

def binary_to_decimal(B):
    d = get_digits(B)
    n = len(d)
    res = 0
    for i in range(n):  
        res += d[n-i-1] * 2**i
    return res
    
###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("10001000", 136) )
    test_inputs.append( ("101100", 44) )

    """ Run process on sample inputs 
    """
    for B, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = binary_to_decimal(B)
        print(f"{rv} expected: {results}")
    

