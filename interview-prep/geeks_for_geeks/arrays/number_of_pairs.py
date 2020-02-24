import sys
import math

# https://practice.geeksforgeeks.org/problems/number-of-pairs/0/
# http://mathforum.org/library/drmath/view/70271.html


# Given two arrays X and Y of positive integers, find number of pairs 
# such that x^y > y^x (raised to power of) where x is an element from X
# and y is an element from Y.

# TODO: could sort both arrays, and do quicker processing for cases where both values > e

# Now, as long as both numbers are larger than e, putting the smaller 
# one as the base and the larger one as the exponent will always 
# produce the larger power.  Therefore, let's call this the normal 
# case.  What we're looking for are special cases where
#
#  a < b   but   a^b < b^a
#
# As mathematicians like to do, I'll give a name to such a pair of 
# numbers; what strikes my fancy at the moment is to call it 
# a "retrograde pair", meaning that the comparison goes backward from 
# the usual.
#
# If you use only whole numbers, then if they are both larger than 2, 
# they will behave normally.
#
# If a=1, then certainly 1^b < b^1 for any (larger) whole number b, so 
# it is always retrograde in this trivial case. 
#
# If a=2, then the only "retrograde" case will be when b=3: 2^3 < 3^2.

def count_pairs_slow(arr1, arr2):
    count = 0
    for x in arr1:
        for y in arr2:
            if x**y > y**x:
                #if x > math.exp(1) and y > math.exp(1):
                #if x > 2 and y > 2:
                #    print(x, y)        # in these cases, smaller number as base is always greater
                count += 1
    return count


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("2 1 6", "1 5", 3) )
    test_inputs.append( ("2 1 3 5 6 4 7 8", "1 5 3 2 7 9", 3) )

    print(math.exp(1))

    """ Run process on sample inputs 
    """
    for inputs1, inputs2, results in test_inputs:
        arr1 = [int(s) for s in inputs1.split()]
        arr2 = [int(s) for s in inputs2.split()]
        print(arr1, arr2)
        count = count_pairs_slow(arr1, arr2)
        print(count, "  expected:", results)


