import sys
import heapq


# using Max/Min heap: O(n) to create heap + O(klogn) to retrieve max/min k elements = O(n + klogn)

def kth_smallest(arr, k):
    heapq.heapify(arr)
    rv = []
    while k:
        rv.append(heapq.heappop(arr))
        k -= 1
    return rv

def kth_largest(arr, k):
    arr = [-x for x in arr]
    heapq.heapify(arr)
    rv = []
    while k:
        rv.append(-heapq.heappop(arr))
        k -= 1
    return rv


if __name__ == "__main__":

    arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45 ]  # largest for k=4: 96 88 50 45
    print(kth_largest(arr, 4))
    print(kth_smallest(arr, 4))

    arr = [ 1, 23, 12, 9, 30, 2, 50 ]   # largest for k=3: 50 30 23
    print(kth_largest(arr, 3))
    print(kth_smallest(arr, 3))

