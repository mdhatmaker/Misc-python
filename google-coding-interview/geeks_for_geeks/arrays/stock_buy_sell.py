import sys

# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0


# The cost of stock on each day is given in an array A[] of size N.
# Find all the days on which you buy and sell the stock so that in between
# those days your profit is maximum.

# is this just looking for subarrays of non-decreasing values?
def stock_buy_sell(arr):
    ret = []
    i1 = 0
    i2 = 0
    
    return ret


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("100 180 260 310 40 535 695", "(0 3) (4 6)") )
    test_inputs.append( ("23 13 25 29 33 19 34 45 65 67", "(1 4) (5 9)") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        buy_sell = stock_buy_sell(arr)
        print(f"{buy_sell} expected: {results}\n")

