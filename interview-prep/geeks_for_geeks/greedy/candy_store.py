import sys

# https://practice.geeksforgeeks.org/problems/shop-in-candy-store/0

# In a candy store there are N different types of candies available and the prices
# of all the N different types of candies are provided to you.
# You are now provided with an attractive offer: You can buy a single candy from the
# store and get at most K other candies (all are different types) for free.
# Now you have to answer two questions. First, what is the minimum amount of money
# you have to spend to buy all the N different candies? Second, what is the maximum
# amount of money you have to spend to buy all the N different candies?
# In both the cases you must utilize the offer (buy one candy and get K other candies for free).
#
# Expected Complexity: O(nlogn)

###############################################################################

# return minimum and maximum amount you must spend to buy all N different candies
def candy_store(arr, N, K):
    A = sorted(arr)
    i = minpay = 0
    n = N
    while i < n:
        minpay += A[i]
        i += 1
        for j in range(K):
            if n <= i: break
            n -= 1
    i = maxpay = 0
    n = N
    while i < n:
        maxpay += A[n-1]
        n -= 1
        for j in range(K):
            if i >= n: break
            i += 1
    return (minpay, maxpay)

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (4, 2, "3 2 1 4", "3 7") )

    """ Run process on sample inputs 
    """
    for N, K, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'N={N} K={K}   {inputs}')
        rv = candy_store(arr, N, K)
        print(f"{rv} expected: {results}")
