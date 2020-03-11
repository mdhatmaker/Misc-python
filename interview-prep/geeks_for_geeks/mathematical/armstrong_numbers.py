import sys

# https://practice.geeksforgeeks.org/problems/armstrong-numbers/0

# For a given 3 digit number, find whether it is armstrong number or not. An Armstrong
# number of three digits is an integer such that the sum of the cubes of its digits is
# equal to the number itself.
#
# For example, 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371
# Also, 1634 is an Armstrong number since 1^4 + 6^4 + 3^4 + 4^4 = 1634
#
# armstrong numbers:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, ...
#
# Are these the same as "narcissistic numbers"?
# In number theory, a narcissistic number in a given number base is a number that
# is the sum of its own digits each raised to the power of the number of digits.

###############################################################################

def get_digits(N):
    s = str(N)
    res = []
    for ch in s:
        res.append(int(ch))
    return res

def is_armstrong_number(N):
    digits = get_digits(N)
    power = len(digits)
    sum = 0
    for d in digits:
        sum += d**power
    return sum == N

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (371, True) )
    test_inputs.append( (1, True) )
    test_inputs.append( (5, True) )
    test_inputs.append( (12, False) )
    test_inputs.append( (1634, True) )

    """ Run process on sample inputs 
    """
    for N, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        #print(f'N={N}   {inputs}')
        rv = is_armstrong_number(N)
        print(f"{rv} expected: {results}")
    

