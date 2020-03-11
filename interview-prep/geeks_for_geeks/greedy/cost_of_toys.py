import sys

# https://practice.geeksforgeeks.org/problems/maximize-toys/0


# Given an array containing dollar cost of toys. Given an integer K depicting the dollars
# you possess. Maximize the number of different toys you can buy with K dollars.

###############################################################################

def maximum_toys(arr, k):
    toys = sorted(arr)
    sum = 0
    for i in range(len(arr)):
        if sum + arr[i] > k: break
        sum += arr[i]
    return 0 if sum == 0 else i+1


###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( (50, "1 12 5 111 200 1000 10", 4) )
    test_inputs.append( (150, "1 12 5 111 200 1000 10", 5) )
    test_inputs.append( (350, "1 12 5 111 200 1000 10", 6) )
    test_inputs.append( (3500, "1 12 5 111 200 1000 10", 7) )
    test_inputs.append( (7, "2 12 5 111 200 1000 10", 2) )
    test_inputs.append( (1, "2 12 5 111 200 1000 10", 0) )

    """ Run process on sample inputs 
    """
    for k, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{k} {arr}')
        rv = maximum_toys(arr, k)
        print(f"{rv} expected: {results}")


