import random
from matlib import matzero, matInsertConstCol, matprint

### https://en.wikipedia.org/wiki/Distributed_lag
### https://www.rhayden.us/regression-models/the-koyck-approach-to-distributedlag-models.html
### http://www.globalacademicgroup.com/journals/nigerian%20journal%20of%20research%20and%20production%20/ESTIMATION%20OF%20LINEAR%20DISTRIBUTED%20LAG.pdf
### https://core.ac.uk/download/pdf/6456722.pdf
### https://astro.temple.edu/~buck/notes/distdlags/Lags1.HTM
### https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3191524/


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

