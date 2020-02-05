import sys
import math


# https://www.techiedelight.com/implement-power-function-without-using-multiplication-division-operators/

# Implement power function without using multiplication and division operations

# a ^ b
def power1(a, b):
    rv = 1
    for i in range(b):
        rv = mult(rv, a)
    return rv

# multiply using addition and for-loop
def mult(a, b):
    rv = 0
    for i in range(b):
        rv += a
    return rv

# x = e^(b * log(a))
def power2(a, b):
    logx = 0
    for i in range(b):
        logx += math.log(a)
    return math.exp(logx)

# pow(a, b) = pow(a, b-1) * a
def power3(a, b):
    if b == 0: return 1

    res = 0
    power = power3(a, b-1)

    for i in range(a):
        res += power

    return res



if __name__ == "__main__":

    a = 2
    b = 10

    print(power1(a, b))
    print(power2(a, b))
    print(power3(a, b))

