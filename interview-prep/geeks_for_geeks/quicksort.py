import sys

# https://stackoverflow.com/questions/18262306/quicksort-with-python


###############################################################################

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

def qsort(array=[12,4,5,6,7,3,1,15]):
    """Sort the array by using quicksort."""
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return qsort(less)+equal+qsort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

def qs_kth_largest(array, k, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _kth_largest(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        print(pivot, end=' ')
        if k > pivot:
            _kth_largest(array, begin, pivot-1)
        else:
            _kth_largest(array, pivot+1, end)
    return _kth_largest(array, begin, end)

###############################################################################

if __name__ == "__main__":

    arr1 = [15, 17, 11, 14, 19, 21, 13, 24, 29, 16]
    print(arr1)
    #quicksort(arr)
    k = 5
    qs_kth_largest(arr1, k)
    print('-->', arr1[k-1])

    arr2 = [15, 17, 11, 14, 19, 21, 13, 24, 29, 16, 6, 5, 4, 3, 2]
    k = 5
    qs_kth_largest(arr2, k)
    print('-->', arr2[k-1])

    quicksort(arr1)
    print('\n', arr1)

    print(qsort(arr2))




