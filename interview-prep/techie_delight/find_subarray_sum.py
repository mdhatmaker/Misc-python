import sys

# https://www.techiedelight.com/check-subarray-with-0-sum-exists-not/


# unsorted array
def subarray_with_sum_naive(arr, n):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if sum(arr[i:j+1]) == n:
                return True
    return False

"""def subarray_with_zero_sum(arr):
    cache = { arr[0]: True }
    for i in range(1, len(arr)-1):
        print(cache)
        if (n - arr[i]) in cache:
            return True
        cache[n - arr[i]] = True
    return False"""

# confusing as fuck...but it works
# (if any previous sum exists such that adding the current element would make it zero...)
def subarray_with_zero_sum(arr):
    bag = {}
    bag[0] = 1
    sum_so_far = 0
    for i in range(len(arr)):
        sum_so_far += arr[i]
        if sum_so_far in bag:
            return True
        else:
            bag[sum_so_far] = 1
    return False     
    
###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (0, "4, 2, -3, -1, 0, 4", True ) )

    """ Run process on sample inputs 
    """
    for n, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split(',')]
        print(f'{n}   {inputs}')
        rv = subarray_with_sum_naive(arr, n)
        rv = subarray_with_zero_sum(arr)
        print(f"{rv} expected: {results}\n")