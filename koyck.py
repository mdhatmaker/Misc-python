import random
from matlib import matzero, matInsertConstCol, matprint

def koyckZmatrix(Y, X, withconstcol=True):
    n = len(Y)
    if n != len(X):
        raise ValueError, "in koyckmatrix():Y,X have different lengths!"
    Z = matzero(n-1, 2)
    for i in range(n-1):    # one less due to lag
        Z[i][0], Z[i][1] = X[i+1], Y[i]
    if withconstcol:
        matInsertConstCol(Z, 0, 1)
    return Y[1:], Z

Y = [random.random() for i in range(10)]
X = range(10)

print "The input Y, X vectors"
for i in range(len(X)):
    print i, Y[i], X[i]

Y, Z = koyckZmatrix(Y, X)
print "The Input Koyck Y and Z matrix."
matprint(Z)

