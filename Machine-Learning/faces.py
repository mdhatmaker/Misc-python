import numpy as np
import pandas as pd
from os.path import join
import os
import sys
from sklearn import datasets
from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

########################################################################################################################

# If file exists, we resume from where the training stopped by loading the file; otherwise create the network
def create_or_read_from_file(training_data, filename='oliv.xml'):
    if os.path.isfile(filename):
        nn = NetworkReader.readFrom(filename)
    else:
        nn = buildNetwork(training_data.indim, 64, training_data.outdim, outclass=SoftmaxLayer)
    return nn

# Use this function to write to a file when the script ends
def write_to_file(nn, filename='oliv.xml'):
    NetworkWriter.writeToFile(nn, filename)

########################################################################################################################

# seed random numbers to make calculation deterministic (just a good practice)
np.random.seed(1)


olivetti = datasets.fetch_olivetti_faces()
X, y = olivetti.data, olivetti.target
print "data shape of faces:", X.shape


# Flatten the 64x64 data to one dimensional 4096 and then feed the data our NN classification dataset:
ds = ClassificationDataSet(4096, 1, nb_classes=40)
for k in xrange(len(X)):
    ds.addSample(X.ravel()[k], y.ravel()[k])

# Split the data into 75% training and 25% test data
tstdata, trndata = ds.splitWithProportion(0.25)

# Convert 1 output to 40 binary outputs
trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()

# Check the data inside the neural network:
print trndata['input'], trndata['target'], tstdata.indim, tstdata.outdim

# Now that all data is loaded, build the network and backpropagation trainer:
#fnn = buildNetwork(trndata.indim, 64, trndata.outdim, outclass=SoftmaxLayer)
fnn = create_or_read_from_file(trndata)
trainer = BackpropTrainer(fnn, dataset=trndata, momentum=0.1, learningrate=0.01, verbose=True, weightdecay=0.01)


# We train our network for 50 epochs and compute the percentage error on test data:
trainer.trainEpochs(50)
print 'Percent Error on Test dataset: ', percentError(trainer.testOnClassData(dataset=tstdata), tstdata['class'])



sys.exit()




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

