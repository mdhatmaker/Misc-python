import numpy as np
import pandas as pd
import tensorflow as tf

# Given the size of a desired batch
# Return randomly sampled data points from the provided x and y
def batch_creator(batch_size, x, y):
    n_samples = x.shape[0]
    assert n_samples == y.shape[0]
    ids = np.random.choice(range(n_samples), batch_size)
    batch_x = x[ids]
    batch_y = y[ids]
    return batch_x, batch_y

# Given some x, weights and biases
# Return a calculated out_layer (after propagating through the hidden layers)
def multilayer_perceptron(x, weights, biases):
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

################################################################################

column_names=['Sex','Length','Diam','Height','Whole','Shucked','Viscera','Shell','Rings']
DATA = pd.read_csv('abalone.data', names=column_names)
CATEGORICAL_COLS = ['Sex']
for c in CATEGORICAL_COLS:
    types = np.unique(DATA[c])
    id_maker = {v: k for k,v in enumerate(types)}
    DATA[c] = [id_maker[x] for x in DATA[c]]
train_x = DATA[DATA.columns[:-1]].values
train_y = DATA[DATA.columns[-1]].values[:, np.newaxis]

LEARNING_RATE = 0.001
TRAINING_EPOCHS = 70
BATCH_SIZE = 100
DISPLAY_STEP = 1

N_HIDDEN_1 = 64
N_HIDDEN_2 = 64
N_INPUT = train_x.shape[1]


X = tf.placeholder('float', [None, N_INPUT])
Y = tf.placeholder('float', [None, 1])
weights = {
    'h1': tf.Variable(tf.random_normal([N_INPUT, N_HIDDEN_1])),
    'h2': tf.Variable(tf.random_normal([N_HIDDEN_1, N_HIDDEN_2])),
    'out': tf.Variable(tf.random_normal([N_HIDDEN_2, 1]))
    }
biases = {
    'b1': tf.Variable(tf.random_normal([N_HIDDEN_1])),
    'b2': tf.Variable(tf.random_normal([N_HIDDEN_2])),
    'out': tf.Variable(tf.random_normal([1]))
    }


pred = multilayer_perceptron(X, weights, biases)
cost = tf.reduce_mean(tf.squared_difference(pred, Y))
optimizer = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE).minimize(cost)
init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    for epoch in range(TRAINING_EPOCHS):
        avg_cost = 0
        n_batches = int(train_x.shape[0]/BATCH_SIZE)
        for i in range(n_batches):
            batch_x, batch_y = batch_creator(BATCH_SIZE, train_x, train_y)
            _,c = sess.run([optimizer,cost], feed_dict={X: batch_x, Y: batch_y})
        avg_cost += c / n_batches

        if epoch % DISPLAY_STEP == 0:
            print ('Epoch: %04d\tcost=%.9f' % (epoch+1, avg_cost))
    print('Optimization Finished!')
    predictions = pred.eval({X: train_x})

print('correlation: %.1f%%' % (np.corrcoef(train_y[:,0], predictions[:,0])[0][1]*100))

