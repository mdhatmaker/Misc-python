import sys
from math import log
import timeit


# Factorial
# n * (n-1) * (n-2) * ... * 3 * 2 * 1
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

# Fibonacci (return nth Fibonacci number)
# 1 1 2 3 5 8 13 21 ...
_fib_cache = {}
def fib(n):
    if n in _fib_cache:
        return _fib_cache[n]
    if n <= 2:
        _fib_cache[n] = 1
        return 1
    else:
        x = fib(n-1) + fib(n-2)
        _fib_cache[n] = x
        return x

# This version of calculating Fibonacci should be slower than the above version which caches 
# calculated values (memoization)
def fib_nocache(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# r items selected from n total items
# Permutation (order matters)
# n! / (n-r)!
def permutation(n, r):
    return int(fact(n) / fact(n-r))
# Combination (order doesn't matter)
# n! / (n-r)!r!
def combination(n, r):
    return int (fact(n) / (fact(n-r) * fact(r)))

# The nth Harmonic Number is the sum of the recipricols of the first n natural numbers
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
# The nth harmonic number is about as large as the natural logarithm of n.
# The reason is that the sum is approximated by the integral 1->n of 1/x dx
# whose value is ln n.
def harmonic(n):
    return log(n)

# A triangular number or triangle number counts objects arranged in an equilateral triangle.
# The nth triangular number is the number of dots in the triangular arrangement with n dots
# on a side, and is equal to the sum of the n natural numbers from 1 to n.
def triangle_number(n):
    # no need to use recursion - simple formula for calculation
    return int(n * (n+1) / 2)

    #if (n <= 0):
    #    return 0
    #else:
    #    return n + triangle_number(n-1)

# Geometric series 1/2 + 1/4 + 1/8 + ... + 1/n
# As n approaches infinity, sn tends to 1.
def geometric_series(n):
    return 1 - (1 / 2**n)

# Gray Numbers (only one bit changes from one number to the next)
def gray_numbers(n):
    gnums = ['1']
    for i in range(n):
        li = []
        for gn in gnums:
            li.append('0' + gn)
        for gn in reversed(gnums):
            li.append('1' + gn)
        gnums = li
    return gnums


if __name__ == "__main__":
    
    gn = gray_numbers(3)
    print(gn)
    sys.exit()

    print(fact(5))
    print(permutation(5,3))
    print(combination(5,3))
    print(harmonic(100))
    print(triangle_number(5))   # like rack of pool balls 5 + 4 + 3 + 2 + 1

    print(geometric_series(18))

    print(fib(8))

    print("Timing Fibonacci functions... ", end=' ')
    exec_time1 = timeit.timeit('tmp = fib(311)', number=1000000, globals=globals())
    exec_time2 = timeit.timeit('tmp = fib_nocache(311)', number=1000000, globals=globals())
    print("cached: %f    no-cache: %f    %6.1f%%" % (exec_time1, exec_time2, exec_time1 / exec_time2 * 100))
