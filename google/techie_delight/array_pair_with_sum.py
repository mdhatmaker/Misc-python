import sys

# https://www.techiedelight.com/find-pair-with-given-sum-array/


# unsorted array
def find_naive(arr, n):
    rv = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == n:
                #print(f'({arr[i]} {arr[j]})')
                rv.append((i, j))
    return rv

# sorted array
def find_in_sorted(arr, n):
    low = 0
    high = len(arr)-1
    while low < high:
        add = arr[low] + arr[high]
        if add == n:
            return (low, high)
        if add < n:
            low += 1
        else:
            high -= 1
    return (-1, -1)
    
###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (10, "1, 2, 3, 5, 7, 8", "(1 5) or (2 4)" ) )

    """ Run process on sample inputs 
    """
    for n, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split(',')]
        print(f'{n}   {inputs}')
        #rv = find_in_sorted(arr, n)
        rv = find_naive(arr, n)
        print(f"{rv} expected: {results}\n")
