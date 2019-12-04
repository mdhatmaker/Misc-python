import sys
import heapq

# https://practice.geeksforgeeks.org/problems/heap-sort/1
# https://www.geeksforgeeks.org/heap-sort/
# https://en.wikipedia.org/wiki/Heapsort


# TODO: Complete this exercise!!!

# Given an array of size N. The task is to sort the array elements by completing
# functions heapify() and buildHeap() which are used to implement Heap Sort.

# Why array based representation for Binary Heap?
# Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array
# and array based representation is space efficient. If the parent node is stored at
# index I, the left child can be calculated by 2 * I + 1 and right child by 2 * I + 2
# (assuming the indexing starts at 0).

# Heap Sort Algorithm for sorting in increasing order:
# 1. Build a max heap from the input data.
# 2. At this point, the largest item is stored at the root of the heap. Replace it
# with the last item of the heap followed by reducing the size of heap by 1. Finally,
# heapify the root of tree.
# 3. Repeat above steps while size of heap is greater than 1.

# iParent(i)     = floor((i-1) / 2) where floor functions map a real number to the smallest leading integer.
# iLeftChild(i)  = 2*i + 1
# iRightChild(i) = 2*i + 2

###############################################################################

def heapify():
    return

def build_heap():
    return

def heap_sort(arr):
    rv = []
    h = [x for x in arr]
    heapq.heapify(h)
    while len(h) > 0:
        x = heapq.heappop(h)
        rv.append(x)
    return rv

###############################################################################

if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("4 1 3 9 7", "1 3 4 7 9") )
    test_inputs.append( ("10 9 8 7 6 5 4 3 2 1", "1 2 3 4 5 6 7 8 9 10") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(f'{arr}')
        rv = heap_sort(arr)
        print(f"{rv} expected: {results}\n")

