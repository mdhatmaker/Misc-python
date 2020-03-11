import sys

# https://practice.geeksforgeeks.org/problems/reverse-digit/0

# Write a program to reverse digits of a number N.

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

def is_palindrome(s):
    n = len(s)
    for i in range(int(n/2)):
        if s[i] != s[n-i-1]: return False
    return True

def reverse_digits(N):
    d = get_digit_chars(N)
    n = len(d)
    for i in range(int(n/2)):
        d[i],d[n-i-1] = d[n-i-1],d[i]
    s = ''.join(d)
    return int(s)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (200, 2) )
    test_inputs.append( (122, 221) )

    """ Run process on sample inputs 
    """
    for N, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = reverse_digits(N)
        print(f"{rv} expected: {results}")
    

