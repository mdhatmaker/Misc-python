import sys

# https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins/0


# Given a value N, total sum you have. You have to make change for Rs. N, and there
# is infinite supply of each of the denominations in Indian currency, i.e., you have
# infinite supply of { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000} valued coins/notes,
# Find the minimum number of coins and/or notes needed to make the change for Rs N.

###############################################################################

def min_coins(n):
    denoms = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    counts = {}
    for d in denoms:
        counts[d] = 0
    target = n
    while target > 0:
        for i, d in enumerate(denoms):
            if d > target:
                break
        dd = denoms[i-1]
        counts[dd] += 1
        target -= dd
    rv = [(k, v) for k, v in counts.items() if v > 0]
    return rv

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (43, "20 20 2 1") )

    """ Run process on sample inputs 
    """
    for n, results in test_inputs:
        #arr = [int(s) for s in inputs.split()]
        print(f'{n}')
        mincoins = min_coins(n)
        print(f"{mincoins} expected: {results}\n")

