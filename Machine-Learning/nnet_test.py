import numpy as np
import pandas as pd
from os.path import join
import sys

"""
X           Input dataset matrix where each row is a training example
y           Output dataset matrix where each row is a training example
l0          First Layer of the network, specified by the input data
l1          Second Layer of the network, otherwise known as the hidden layer
syn0        First layer of weights, Synapse 0, connecting l0 to l1
 *          Elementwise multiplication, so two vectors of equal size are multiplying
            corresponding values 1-to-1 to generate a final vector of identical size.
 -          Elementwise subtraction, so two vectors of equal size are subtracting
            corresponding values 1-to-1 to generate a final vector of identical size.
x.dot(y)    If x and y are vectors, this is a dot product. If both are matrices, it's a
            matrix-matrix multiplication. If only one is a matrix, then it's vector-matrix
            multiplication.
"""

# sigmoid function
def nonlin(x, deriv=False):
    if (deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

def nn_calc(X, syn0):
    return nonlin(np.dot(X,syn0))

def nn_calc_all(X, weights):
    result = []
    for i in range(len(weights)):
        l1 = nn_calc(X, weights[i])
        result.append(round(l1[0][0]))
    return result

def get_hits(df, ix, lookback=10):
    hit = []
    for i in range(lookback, 0, -1):
        hit.extend(df.loc[ix-i].values[4:13].tolist())
    return hit

# X is input (list of lists)
# y is output (list)
# Returns syn0 (synapse 0) which contains the weights for our neural net
def nn_build(X, y):
    X = np.array(X)
    y = np.array([y]).T
    # initialize weights randomly with mean 0
    #syn0 = 2*np.random.random((3,1)) - 1
    input_count = len(X[0])
    syn0 = 2*np.random.random((input_count,1)) - 1

    for iter in xrange(10000):
        # forward propagation
        l0 = X
        #l1 = nonlin(np.dot(l0,syn0))
        l1 = nn_calc(l0, syn0)

        # how much did we miss?
        l1_error = y - l1

        # multiply how much we missed by the
        # slope of the sigmoid at the values in l1
        l1_delta = l1_error * nonlin(l1, True)

        # update weights
        syn0 += np.dot(l0.T, l1_delta)
    return syn0

########################################################################################################################

# seed random numbers to make calculation deterministic (just a good practice)
np.random.seed(1)

#-------------------------------------------------------------------------------
# Initial NN Example
in_data = [ [0,0,1], [0,1,1], [1,0,1], [1,1,1] ]    # input dataset
out_data = [0,0,1,1]                                # output dataset

syn0 = nn_build(in_data, out_data)                  # build the nn to return a set of weights (syn0 = synapse0)
l1 = nn_calc(in_data, syn0)                         # use the generated synapse weights to calculate

print "Output after training:"
print l1

# inputs : output
# 0 0 1  : 0
# 1 1 1  : 1
# 1 0 1  : 1
# 0 1 1  : 0
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Trial AND NN Example
in_data = [ [0,0], [0,1], [1,0], [1,1] ]            # input dataset
out_data = [0,0,0,1]                                # output dataset

syn0 = nn_build(in_data, out_data)                  # build the nn to return a set of weights (syn0 = synapse0)
l1 = nn_calc(in_data, syn0)                         # use the generated synapse weights to calculate

print "Output after training:"
print l1
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Trial OR NN Example
in_data = [ [0,0], [0,1], [1,0], [1,1] ]            # input dataset
out_data = [0,1,1,1]                                # output dataset

syn0 = nn_build(in_data, out_data)                  # build the nn to return a set of weights (syn0 = synapse0)
l1 = nn_calc(in_data, syn0)                         # use the generated synapse weights to calculate

print "Output after training:"
print l1
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Trial XOR NN Example
in_data = [ [0,0], [0,1], [1,0], [1,1] ]            # input dataset
out_data = [0,1,1,0]                                # output dataset

syn0 = nn_build(in_data, out_data)                  # build the nn to return a set of weights (syn0 = synapse0)
l1 = nn_calc(in_data, syn0)                         # use the generated synapse weights to calculate

print "Output after training:"
print l1
#-------------------------------------------------------------------------------

# read the ES/VIX quartile data into a dataframe
folder = r"B:\Users\mhatmaker\Dropbox\alvin\data\vix_es"
filename = "es_vix_quartiles (10-day lookback).csv"
pathname = join(folder, filename)
df_all = pd.read_csv(pathname, parse_dates=['DateTime'])

row_count = df_all.shape[0]

# Remove any rows that contain the value -1 (which is our "invalid" value)
df = df_all[(df_all != -1).all(1)]

inputs = []                                     # inputs will be a list of lists
outputs = [[],[],[],[],[],[],[],[],[]]          # one list for each of the available outputs

print "Retrieving training data subset from complete dataset:"
"""
for (ix,row) in df.iterrows():
    # only use the FIRST half of the data
    if ix > (row_count/2):
        break
    hit_ratios = row.values[13:22]
    days_to_hit = row.values[22:31]
    inputs.append(hit_ratios.tolist())
    for i in range(9):
        outputs[i].append(days_to_hit[i])
"""
df = df_all
# only use the FIRST half of the data
for ix in range(10, row_count/2):
    hits = get_hits(df, ix, 10)
    days_to_hit = df.loc[ix].values[4:13]
    inputs.append(hits)
    for i in range(9):
        outputs[i].append(days_to_hit[i])

print "Calculating a set of synapse weights for each output:"
weights = []
for i in range(9):
    print "Calculating for output {0}...".format(i)
    weights.append(nn_build(inputs, outputs[i]))

print "Testing calculated synapse weights for accuracy:"
for ix in range(row_count/2, row_count):
    print ix
    hits = get_hits(df, ix, 10)
    days_to_hit = df.loc[ix].values[4:13]
    l1 = nn_calc_all([hits], weights)
    print l1




"""
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1
for j in xrange(60000):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(11,syn1))))
    l2_delta = (y - 12)*(12*(1-12))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)
"""

