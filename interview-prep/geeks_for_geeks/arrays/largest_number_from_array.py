import sys

# https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0


# TODO: this is SO UGLY -- there's got to be a better algorithm for this!

# Given a list of non negative integers, arrange them in such a manner that they
# form the largest number possible.The result is going to be very large, hence
# return the result in the form of a string.

def cmp(x, y):
    sx = str(x)
    sy = str(y)
    if sx[0] < sy[0]:
        return -1
    elif sy[0] < sx[0]:
        return 1
    else:
        if len(sx) < len(sy):
            sx += '0' * (len(sy)-len(sx))
        elif len(sy) < len(sx):
            sy += '0' * (len(sx)-len(sy))
        if sx < sy:
            return -1
        elif sy < sx:
            return 1
        else:
            return 0

def largest_number(arr_unsorted):
    arr = [arr_unsorted[0]]
    for x in arr_unsorted[1:]:
        ix = -1
        for i, y in enumerate(arr):
            if cmp(x,y) == 1:
                ix = i
                break
        if ix == -1:
            arr.append(x)
        else:
            arr.insert(ix, x)
    return arr


if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("3 30 34 5 9", "9534330") )
    test_inputs.append( ("54 546 548 60", "6054854654") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(arr)
        largest = largest_number(arr)
        print(f"{largest} expected: {results}\n")

