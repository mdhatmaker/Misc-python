import sys

# https://practice.geeksforgeeks.org/problems/missing-number-in-array/0

# Given an array C of size N-1 and given that there are numbers from 1 to N with
# one element missing, the missing number is to be found.


def missing_number(arr, N):
    total = triangle_number(N)
    mysum = sum(arr)
    return total - mysum

# Function to calculate Triangle Numbers (like balls in pool rack: 5 + 4 + 3 + 2 + 1)
def triangle_number(n):
    return int(n * (n+1) / 2)

def missing_number_slow(arr, N):
    li = [x for x in range(1, N+1)]
    for x in arr:
        li.remove(x)
    print(li)
    return li[0]


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (5, "1 2 3 5", 4) )
    test_inputs.append( (10, "1 2 3 4 5 6 7 8 10", 9) )

    for n, inputs, result in test_inputs:
        arr = [int(s) for s in inputs.split()]
        missing = missing_number(arr, n)
        missing_slow = missing_number_slow(arr, n)
        print(missing, "  expected:", missing_slow)
