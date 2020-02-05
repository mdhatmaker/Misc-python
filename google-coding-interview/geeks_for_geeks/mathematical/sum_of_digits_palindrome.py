import sys

# https://practice.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not/0

# Write a program to check if the sum of digits of a given number N is a palindrome
# number or not.

###############################################################################

def get_digits(N):
    s = str(N)
    res = []
    for ch in s:
        res.append(int(ch))
    return res

def is_palindrome(s):
    n = len(s)
    for i in range(int(n/2)):
        if s[i] != s[n-i-1]: return False
    return True

def is_sum_of_digits_palindrome(N):
    digits = get_digits(N)
    sum_of_digits = sum(digits)
    return is_palindrome(str(sum_of_digits))

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (56, True) )
    test_inputs.append( (98, False) )

    """ Run process on sample inputs 
    """
    for N, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = is_sum_of_digits_palindrome(N)
        print(f"{rv} expected: {results}")
    

