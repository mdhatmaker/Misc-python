import sys


# Problem: Find peak if one exists.
# e.g. position 2 is a peak if A[2] >= A[1] and A[2] >= A[3]
# (peak always exists when using >= but may not if using >)


def find_peak_simp(arr):
    for i in range(len(arr)):
        found = True
        if i-1 >=0 and arr[i-1] > arr[i]:
            found = False
        if i+1 < len(arr) and arr[i+1] >= arr[i]:
            found = False
        if found: return arr[i]
    return -1

def find_peak_divconq(arr):
    i = int(len(arr)/2)
    #print(i, arr)
    if i-1 >= 0 and arr[i-1] > arr[i]:
        return find_peak_divconq(arr[:i])
    elif i+1 < len(arr) and arr[i] < arr[i+1]:
        return find_peak_divconq(arr[i:])
    else:
        return arr[i]

# Greedy ascent algorithm :: O(mn) -> O(n^2) if m==n
def find_peak_2d_simp(arr):

    return


def find_peak_2d_divconq(arr):
    # pick middle column j = m/2
    # find global max on column j at (i,j)
    # compare (i,j-1), (i,j), (i,j+1)
    # pick the left columns if (i,j-1) > (i,j)  (similarly for right)
    # neither LEFT nor RIGHT condition are True, then (i,j) is a 2D peak
    # solve new problem with half number of columns
    # when you have a single column, find the global max (done!)
    return


if __name__ == "__main__":

    arr = [
        [1,2,3,4,5,6,5,4,3,2,1],
        [7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8]
    ]

    for A in arr:
        print(find_peak_simp(A), find_peak_divconq(A))

    arr = [
        [1,1,1,1,1],
        [1,2,2,2,1],
        [1,2,3,2,1],
        [1,2,2,2,1],
        [1,1,1,1,1]
    ]

    arr = [
        [1,1,1,1,1],
        [1,2,2,2,1],
        [1,2,3,2,1],
        [1,2,2,2,1],
        [1,1,1,1,1]
    ]
    print(find_peak_2d_simp(arr))