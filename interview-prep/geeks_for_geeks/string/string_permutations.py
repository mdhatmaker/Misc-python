import sys
import math

# https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0
# https://stackoverflow.com/questions/29042819/heaps-algorithm-permutation-generator


# Given a string S. The task is to print all permutations of a given string.

def get_permutations(s):
    """n = r = len(s)
    #print(permutation_count(n, r))"""
    arr = []
    for ch in s:
        arr.append(ch)
    #heapPermutation(arr, len(arr), 3)
    for x in _heap_perm_(len(arr), arr):
        sper = ''.join(x)
        yield sper
    return

def _heap_perm_(n, A):
    # if size becomes 1 then prints the obtained permutation
    if n == 1: yield A
    else:
        for i in range(n-1):
            for hp in _heap_perm_(n-1, A): yield hp
            # if size is odd, swap first and last element
            # else If size is even, swap ith and last element 
            j = 0 if (n % 2) == 1 else i
            A[j],A[n-1] = A[n-1],A[j]
        for hp in _heap_perm_(n-1, A): yield hp

def permutation_count(n, r):
    return int (math.factorial(n) / math.factorial(n-r))

def combination_count(n, r):
    return int (math.factorial(n) / (math.factorial(n-r) * math.factorial(r)))



if __name__ == "__main__":

    test_inputs = []
    test_inputs.append( ("ABC", "ABC ACB BAC BCA CAB CBA") )
    test_inputs.append( ("ABSG", "ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA") )

    """ Run process on sample inputs 
    """
    for inputs, results in test_inputs:
        print(inputs)
        perms = [x for x in get_permutations(inputs)]            
        for p in perms:
            print(p, end=' ')
        print(f"\n expected: {results}\n")





"""#Prints the array 
def printArr(a, n): 
    for i in range(n):
        print(a[i],end=" ")
    print() 

# Generating permutation using Heap Algorithm 
def heapPermutation(a, size, n): 
    # if size becomes 1 then prints the obtained permutation
    if (size == 1): 
        printArr(a, n) 
        return
  
    for i in range(size): 
        heapPermutation(a,size-1,n); 
  
        # if size is odd, swap first and last element
        # else If size is even, swap ith and last element 
        if size&1: 
            a[0], a[size-1] = a[size-1],a[0] 
        else: 
            a[i], a[size-1] = a[size-1],a[i] 
"""

"""procedure generate(n : integer, A : array of any):
    if n = 1 then
        output(A)
    else
        for i := 1; i ≤ n; i += 1 do
            generate(n - 1, A)
            if n is odd then
                j ← 1
            else
                j ← i
            swap(A[j], A[n])"""