import sys
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import tensorflow as tf

from sklearn.metrics import mean_squared_error
from math import sqrt
import ta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))








# Step 1 - Import price data
filename = "gold-train.csv"
filepath = os.path.join(SCRIPT_DIR, "..", "data", filename)
df = pd.read_csv(filepath)

df.Timestamp = pd.to_datetime(df.Date,format='%Y/%m/%d')
df.index = df.Timestamp

df.drop(['Date'], axis=1, inplace=True)


# Step 2 - Split into training and testing set
count = df.shape[0]
cutoff = int(0.85 * count)
train = df[0:cutoff]
test = df[cutoff:]





# Step 3 - Reinforcement Learning
# https://www.youtube.com/watch?v=05NqKJ0v7EE
# https://github.com/llSourcell/Reinforcement_Learning_for_Stock_Prediction
# frame market as Markov decision process
# neural-net output -> decision buy/sell -> (a) make money = positive reinforcement (b) lose money = negative reinforcement
prices = test.copy()
actions = ['Buy', 'Sell', 'Hold']
hist = 200

class DecisionPolicy:
        def select_action(self, current_state, step):
            pass

        def update_q(self, state, action, reward, next_state):
            pass

class RandomDecisionPolicy(DecisionPolicy):
    def __init__(self, actions):
        self.actions = actions

    def select_action(self, current_state, step):
        action = self.actions[random.randint(0, len(self.actions)-1)]
        return action

class QLearningDecisionPolicy(DecisionPolicy):
    def __init__(self, actions, input_dim):
        self.epsilon = 0.5
        self.gamma = 0.001
        self.actions = actions
        output_dim = len(actions)
        h1_dim = 200

        #3 layer neural network
        self.x = tf.placeholder(tf.float32, [None, input_dim])
        self.y = tf.placeholder(tf.float32, [output_dim])
        W1 = tf.Variable(tf.random_normal([input_dim, h1_dim]))
        b1 = tf.Variable(tf.constant(0.1, shape=[h1_dim]))
        h1 = tf.nn.relu(tf.matmul(self.x, W1) + b1)
        W2 = tf.Variable(tf.random_normal([h1_dim, output_dim]))
        b2 = tf.Variable(tf.constant(0.1, shape=[output_dim]))
        self.q = tf.nn.relu(tf.matmul(h1, W2) + b2)

        # measuring error
        loss = tf.square(self.y - self.q)
        # updating weights
        self.train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

    def select_action(self, current_state, step):
        threshold = min(self.epsilon, step / 1000.)
        if random.random() < threshold:
            # Exploit best option with probability epsilon
            action_q_vals = self.sess.run(self.q, feed_dict={self.x:current_state})
            action_idx = np.argmax(action_q_vals)   # TODO: replace w/ tensorflow's argmax
            action = self.actions[action_idx]
        else:
            # Explore random option with probability 1-epsilon
            action = self.actions[random.randint(0, len(self.actions) - 1)]
        return action   



policy = RandomDecisionPolicy(actions)
# policy = QLearningDecisionPolicy(actions)
budget = 1000.0
num_stocks = 0
avg, std = run_simulations(policy, budget, num_stocks, prices, hist)
print(avg, std)


# Momentum
#ta.momentum.RSIIndicator(pd_series_close, n=14)
# Volatility
#ta.volatility.bollinger_hband(close, n=20, ndev=2)
#ta.volatility.bollinger_hband(close, n=20, ndev=2)
# Trend
#ta.trend.adx(high, low, close, n=14)


