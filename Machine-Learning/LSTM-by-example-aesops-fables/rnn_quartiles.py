'''
A Recurrent Neural Network (LSTM) implementation example using TensorFlow..
Next word prediction after n_input words learned from text file.
A story is automatically generated if the predicted word is fed back as input.
Author: Rowel Atienza
Project: https://github.com/roatienza/Deep-Learning-Experiments
'''

from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn
import random
import collections
import time
import os.path
import sys


#-------------------------------------------------------------------------------
# Add to the PYTHONPATH the folder containing python function modules
li = ["C:\\Users\\Trader\\Dropbox\\alvin\\python", "D:\\Users\\mhatmaker\\Dropbox\\alvin\\python", "/Users/michael/Dropbox/alvin/python"]
sys.path.extend( [path for path in li if os.path.exists(path)] )

from f_data_folder import *
from f_chart import *
import f_dataframe as fdf

#-------------------------------------------------------------------------------

start_time = time.time()
def elapsed(sec):
    if sec<60:
        return str(sec) + " sec"
    elif sec<(60*60):
        return str(sec/60) + " min"
    else:
        return str(sec/(60*60)) + " hr"

def STOP(x=None):
    print(x)
    sys.exit()

def to_binary(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def get_binary(row):
    b = []
    b.append(row['d4'])
    b.append(row['d3'])
    b.append(row['d2'])
    b.append(row['d1'])
    b.append(row['unch'])
    b.append(row['u1'])
    b.append(row['u2'])
    b.append(row['u3'])
    b.append(row['u4'])
    return to_binary(b), "".join([str(bit) for bit in b])


################################################################################

# TAKE ANY DATA WE WANT AND PUT IT INTO INDIVIDUAL ROWS IN THE 'LSTM_INPUT.csv' FILE
df = pd.read_csv('../iqfeed/@ES_quartile_hit_ratios.DF.csv', parse_dates=['DateTime'])
start_col = df.columns.get_loc('d4')
end_col = df.columns.get_loc('u4')

bit_count = None
#f = open('LSTM_INPUT.csv', 'w')
f = open('LSTM_INPUT.txt', 'w')
for ix,r in df.iterrows():
    b,bstr = get_binary(r)
    #if bit_count == None: bit_count = len(bstr)
    """
    contango = int(r['contango'] * 100.0)
    if contango < 0:
        cb = 1
    elif contango < 5:
        cb = 2
    elif contango < 10:
        cb = 4
    elif contango < 15:
        cb = 8
    else:
        cb = 16
    value = cb << bit_count | b
    """
    value = bstr
    #f.write("{0}\n".format(value))
    f.write("{0} ".format(value))
f.close()
#print("bit count: {0}".format(bit_count))


# Target log path
logs_path = '~/tmp/tensorflow/rnn_words'
writer = tf.summary.FileWriter(logs_path)

# Text file containing words for training
#training_file = 'belling_the_cat.txt'
training_file = 'LSTM_INPUT.txt'

def read_data(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = [content[i].split() for i in range(len(content))]
    content = np.array(content)
    content = np.reshape(content, [-1, ])
    return content

print("Loading training data ... ", end="")
training_data = read_data(training_file)
print("Done.")


def build_dataset(words):
    count = collections.Counter(words).most_common()
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return dictionary, reverse_dictionary

dictionary, reverse_dictionary = build_dataset(training_data)
vocab_size = len(dictionary)


# Parameters
learning_rate = 0.001
training_iters = 150000
display_step = 500
#n_input = 3
n_input = 20


# number of units in RNN cell
n_hidden = 512

# tf Graph input
x = tf.placeholder("float", [None, n_input, 1])
y = tf.placeholder("float", [None, vocab_size])

# RNN output node weights and biases
weights = {
    'out': tf.Variable(tf.random_normal([n_hidden, vocab_size]))
}
biases = {
    'out': tf.Variable(tf.random_normal([vocab_size]))
}

def RNN(x, weights, biases):

    # reshape to [1, n_input]
    x = tf.reshape(x, [-1, n_input])

    # Generate a n_input-element sequence of inputs
    # (eg. [had] [a] [general] -> [20] [6] [33])
    x = tf.split(x,n_input,1)

    # 2-layer LSTM, each layer has n_hidden units.
    # Average Accuracy= 95.20% at 50k iter
    rnn_cell = rnn.MultiRNNCell([rnn.BasicLSTMCell(n_hidden),rnn.BasicLSTMCell(n_hidden)])

    # 1-layer LSTM with n_hidden units but with lower accuracy.
    # Average Accuracy= 90.60% 50k iter
    # Uncomment line below to test but comment out the 2-layer rnn.MultiRNNCell above
    # rnn_cell = rnn.BasicLSTMCell(n_hidden)

    # generate prediction
    outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)

    # there are n_input outputs but
    # we only want the last output
    return tf.matmul(outputs[-1], weights['out']) + biases['out']

pred = RNN(x, weights, biases)

# Loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(cost)

# Model evaluation
correct_pred = tf.equal(tf.argmax(pred,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf.global_variables_initializer()

#Create a saver object which will save all the variables
saver = tf.train.Saver()

# Launch the graph
#with tf.Session() as session:

session = tf.Session()

load_model = True
# If load_model is True then we will load a previously saved model;
# otherwise, we build a new one and save it.
if load_model:
    #First let's load meta graph and restore weights
    print("Restoring model from save ... ", end="")
    saver = tf.train.import_meta_graph('rnn_words_model-1000.meta')
    saver.restore(session,tf.train.latest_checkpoint('./'))
    print("Done.")
else:
    session.run(init)
    step = 0
    offset = random.randint(0,n_input+1)
    end_offset = n_input + 1
    acc_total = 0
    loss_total = 0

    writer.add_graph(session.graph)

    while step < training_iters:
        # Generate a minibatch. Add some randomness on selection process.
        if offset > (len(training_data)-end_offset):
            offset = random.randint(0, n_input+1)

        symbols_in_keys = [ [dictionary[ str(training_data[i])]] for i in range(offset, offset+n_input) ]
        symbols_in_keys = np.reshape(np.array(symbols_in_keys), [-1, n_input, 1])
        symbols_out_onehot = np.zeros([vocab_size], dtype=float)
        symbols_out_onehot[dictionary[str(training_data[offset+n_input])]] = 1.0
        symbols_out_onehot = np.reshape(symbols_out_onehot,[1,-1])

        _, acc, loss, onehot_pred = session.run([optimizer, accuracy, cost, pred], \
                                                feed_dict={x: symbols_in_keys, y: symbols_out_onehot})
        loss_total += loss
        acc_total += acc
        if (step+1) % display_step == 0:
            print("Iter= " + str(step+1) + ", Average Loss= " + \
                  "{:.6f}".format(loss_total/display_step) + ", Average Accuracy= " + \
                  "{:.2f}%".format(100*acc_total/display_step))
            acc_total = 0
            loss_total = 0
            symbols_in = [training_data[i] for i in range(offset, offset + n_input)]
            symbols_out = training_data[offset + n_input]
            symbols_out_pred = reverse_dictionary[int(tf.argmax(onehot_pred, 1).eval())]
            print("%s - [%s] vs [%s]" % (symbols_in,symbols_out,symbols_out_pred))
            # Save the graph
            saver.save(session, 'rnn_words_model', global_step=1000)
        step += 1
        offset += (n_input+1)
        
        
# To get here, we have either run the training OR loaded a previously saved model

print("READY TO PREDICT!")
print()

print("TRAINING DATA LENGTH: {0}".format(len(training_data)))
print()
print("\ttensorboard --logdir=%s" % (logs_path))
print("Point your web browser to: http://localhost:6006/")
print("(ctrl+c to break out of loop)")



def get_prediction(quartile_hits):
    #while True:
    if len(quartile_hits) != n_input:
        #continue
        pass
    #try:
    sentence = ""
    symbols_in_keys = [dictionary[str(quartile_hits[i])] for i in range(len(quartile_hits))]
    keys = np.reshape(np.array(symbols_in_keys), [-1, n_input, 1])
    onehot_pred = session.run(pred, feed_dict={x: keys})
    onehot_pred_index = int(tf.argmax(onehot_pred, 1).eval(session=session))
    #print("predicted index: {0}".format(onehot_pred_index))
    #print(onehot_pred_index)
    #print("predicted value: {0}".format(reverse_dictionary[onehot_pred_index]))
    #except:
    #    print("Quartile hit sequence is NOT in dictionary")
    return onehot_pred_index, reverse_dictionary[onehot_pred_index]


random_indexes = [500, 201, 3, 705, 2002, 128, 768]


for ix in random_indexes:
    qhits = training_data[ix:ix+n_input]
    actual = training_data[ix+n_input]
    
    print("Quartile Hit Sequence:\n", qhits)
    _, predict = get_prediction(qhits)
    print("PREDICTION:", predict)
    print("    ACTUAL:", actual)
    print()


