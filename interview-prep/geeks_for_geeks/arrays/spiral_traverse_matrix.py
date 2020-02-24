import sys

# https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix/0


# Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.

def matrix(r, c, arr, m, n):
    ix = r * n + c
    return arr[ix]

def traverse_matrix(arr, m, n):
    r1 = c1 = 0
    r2 = m-1
    c2 = n-1
    while r1 <= r2 and c1 <= c2:
        r = r1
        for c in range(c1, c2+1):
            print(arr[r * n + c], end=' ')
        c = c2
        for r in range(r1+1, r2+1):
            print(arr[r * n + c], end=' ')
        if r1 < r2:
            r = r2
            for c in range(c2-1, c1-1, -1):
                print(arr[r * n + c], end=' ')
        if c1 < c2:
            c = c1
            for r in range(r2-1, r1, -1):
                print(arr[r * n + c], end=' ')
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return


if __name__ == "__main__":

    # input tuples: (M, N, matrix_values, correct_result)
    test_inputs = []
    test_inputs.append( (4, 4, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16", "1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10") )
    test_inputs.append( (3, 4, "1 2 3 4 5 6 7 8 9 10 11 12", "1 2 3 4 8 12 11 10 9 5 6 7") )

    """ Run process on sample inputs 
    """
    for M, N, inputs, results in test_inputs:
        arr = [int(s) for s in inputs.split()]
        print(M, N, arr)
        traverse_matrix(arr, M, N)
        print(f" expected: {results}\n")

