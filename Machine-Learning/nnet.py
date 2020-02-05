import numpy as np
import pandas as pd
from os.path import join
import sys
from pybrain.structure import FeedForwardNetwork, RecurrentNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

########################################################################################################################

# seed random numbers to make calculation deterministic (just a good practice)
np.random.seed(1)

# Make a new FeedForwardNetwork object:
n = FeedForwardNetwork()

# Next, construct the input, hidden and output layers:
inLayer = LinearLayer(2)
hiddenLayer = SigmoidLayer(3)
outLayer = LinearLayer(1)

# In order to use these layers, we have to add them to the network:
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

# The net has to know which of its modules are input and output modules in order to forward
# propagate input and to back propagate errors.

# To determine how layers are connected, we use the most common connection type, which produces
# a full connectivity between layers, by connecting each neuron of one layer with each neuron of
# the other. This is implemented by the FullConnection class:
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)

# As with modules, we have to add these connections to the network:
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

# All the elements are now in place, so we can do the final step that makes our MLP usable, which
# is to call the .sortModules() method. This call does some internal initialization which is necessary
# before the net can finally be used: for example, the modules are sorted topologically:
n.sortModules()

# We can print networks and examine their structure:
print n

# One way of using the network is to call its 'activate()' method with an input to be transformed:
n.activate([1, 2])

# We can access the trainable parameters (weights) of a connection directly, or read all weights
# of the network at once:
print in_to_hidden.params
print hidden_to_out.params

# The network encapsulating the modules actually holds the parameters too. You can check them out here:
print n.params

# The RecurrentNetwork is different from FeedForwardNetwork in a substantial way: the complete history is saved.
# This is memory-consuming but necessary for some learning algorithms.
n = RecurrentNetwork()
n.addInputModule(LinearLayer(2, name='in'))
n.addModule(SigmoidLayer(3, name='hidden'))
n.addOutputModule(LinearLayer(1, name='out'))
n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

# A recurrent connection looks back in time one timestep. We can add one from the hidden to the hidden layer:
n.addRecurrentConnection(FullConnection(n['hidden'], n['hidden'], name='c3'))

# If we now activate the network, we will get different outputs each time:
n.sortModules()
n.activate((2, 2))
n.activate((2, 2))
n.activate((2, 2))

# Clear the history of the network by calling the reset method (this will get the same outputs as
# just after the objects creation):
n.reset()
n.activate((2, 2))
n.activate((2, 2))
n.activate((2, 2))

# AND
x_train = [[0,0], [0,1], [1,0], [1,1]]
y_train = [[0], [0], [0], [1]]
# OR
x_train = [[0,0], [0,1], [1,0], [1,1]]
y_train = [[0], [1], [1], [1]]
# XOR
x_train = [[0,0], [0,1], [1,0], [1,1]]
y_train = [[0], [1], [1], [0]]
# A NEURAL NETWORK IN 11 LINES OF PYTHON (https://iamtrask.github.io/2015/07/12/basic-python-network/)
x_train = [ [0,0,1], [0,1,1], [1,0,1], [1,1,1] ]    # input dataset
y_train = [ [0], [0], [1], [1] ]                    # output dataset

# Prepare a dataset
input_size = 3
target_size = 1
ds = SupervisedDataSet(input_size, target_size)
ds.setField('input', x_train)
ds.setField('target', y_train)

# Apparently Y needs to be of shape (n,1) as opposed to (n,) so first we reshape it:
#y_train = y_train.reshape(-1, 1)

# And to train a network:
hidden_size = 100           # arbitrarily chosen

net = buildNetwork(input_size, hidden_size, target_size, bias=True)
trainer = BackpropTrainer(net, ds)

trainer.trainUntilConvergence(verbose=True, validationProportion=0.15, maxEpochs=1000, continueEpochs=10)

# Producing predictions, especially for regression taks, is quite easy:
p = net.activateOnDataset(ds)
print p



sys.exit()



#-------------------------------------------------------------------------------
# Initial NN Example
in_data = [ [0,0,1], [0,1,1], [1,0,1], [1,1,1] ]    # input dataset
out_data = [0,0,1,1]                                # output dataset

syn0 = nn_build(in_data, out_data)                  # build the nn to return a set of weights (syn0 = synapse0)
l1 = nn_calc(in_data, syn0)                         # use the generated synapse weights to calculate

print "Output after training:"
print l1
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

