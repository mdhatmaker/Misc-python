import sys
import math

# TODO: this needs to be fixed!!!

# Find a triplet a, b, c such that a^2 = b^2 + c^2. Variations of this problem like
# find a triplet with sum equal to 0. Find a pair with given sum.
# All such questions are efficiently solved using hashing.


def find_triplets_pythagorean(arr):
    print(arr)
    N = len(arr)
    found = False
    for i in range(N-1):
        if found: break
        bag = {}
        for j in range(i, N):
            x = (arr[i]**2 + arr[j]**2)
            #print(x, bag)
            if x in bag:
                print(x, "found pythagorean triplets!!!")
                found = True
                break
            else:
                bag[arr[j]] = True
    if found == False:
        print("NO PYTHAGOREAN TRIPLETS")

# using hashing
def find_triplets_zerosum(arr):
    print(arr)
    N = len(arr)
    found = False
    for i in range(N-1):
        if found: break
        bag = {}
        for j in range(i, N):
            #print(bag)
            x = -(arr[i] + arr[j])
            if x in bag:
                print("found zero sum!!!")
                found = True
                break
            else:
                bag[arr[j]] = True
    if found == False:
        print("NO ZERO SUM TRIPLETS")

# using sorting
def find_triplets_zerosumB(arr):
    print(arr)
    arr.sort()
    N = len(arr)

    found = False
    for i in range(N):
        if found: break
        l = i+1
        r = N-1
        while l < r:
            x = arr[i]
            if (x + arr[l] + arr[r]) == 0:
                print("found zero sum!!!")
                found = True
                break
            elif (x + arr[l] + arr[r]) < 0:
                l += 1
            else:
                r -= 1
    if found == False:
        print("NO ZERO SUM TRIPLETS")


if __name__ == "__main__":

    find_triplets_pythagorean([1, 3, 2, 5, 4, 6])
    find_triplets_pythagorean([11, 13, 12, 15, 14, 16])
    find_triplets_pythagorean([5, 12, 13])

    sys.exit()

    find_triplets_zerosumB([1, -3, 2, -5, 4, 6])
    find_triplets_zerosumB([1, 3, 2, 5, 4, 6])
