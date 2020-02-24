import sys
import math

# https://www.techiedelight.com/add-two-numbers-without-using-addition-operator/

# Add two numbers without using addition operator (4 methods)

# using subtraction
def add1(a, b):
    return a - (-b)

# using logarithm and exponential function
def add2(a, b):
    return int(math.log(math.exp(a) * math.exp(b)))

# half adder logic
def add3(a, b):
    if b == 0: return a
    sum = a ^ b
    carry = (a & b) << 1
    return add3(sum, carry)

# repeated addition/subraction using increment/decrement (++/--)
def add4(a, b):
    while (a > 0):  # handle positive a
        a -= 1
        b += 1      # kind of cheating since python doesn't have ++
    while (a < 0):  # handle negative a
        a += 1
        b -= 1
    return b


if __name__ == "__main__":

    li = [(5, 8), (5, -8), (-5, -8)]

    for a,b in li:
        print('\n', a, b)
        print(add1(a, b))
        print(add2(a, b))
        print(add3(a, b))
        print(add4(a, b))
