import sys



# https://www.techiedelight.com/swap-two-numbers-without-using-third-variable/

# Swap two numbers without using third variable

# python way
def swap1(a, b):
    a, b = b, a     # python way
    return a, b

# using xor
def swap2(a, b):
    a = a ^ b
    return a ^ (a ^ b), a ^ b

# using addition and subtraction
def swap3(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# using multiplication and division
def swap4(a, b):
    a = a * b
    b = a / b
    a = a / b
    return a, b

if __name__ == "__main__":

    x = 2
    y = 3

    print(swap1(x, y))
    print(swap2(x, y))
    print(swap3(x, y))
    print(swap4(x, y))
