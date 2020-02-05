from iqapi import historicData
from datetime import datetime, timedelta
from dateutil import relativedelta
import pandas as pd
from pandas.tseries.offsets import BDay
import numpy as np
import os.path
import math
import sys
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm, time  # helper libraries


#-------------------------------------------------------------------------------
# Add to the PYTHONPATH the folder containing python function modules
li = ["C:\\Users\\Trader\\Dropbox\\alvin\\python", "D:\\Users\\mhatmaker\\Dropbox\\alvin\\python", "/Users/michael/Dropbox/alvin/python"]
sys.path.extend( [path for path in li if os.path.exists(path)] )

from f_data_folder import *
from f_chart import *
import f_dataframe as fdf

#-------------------------------------------------------------------------------

def STOP(x=None):
    print x
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
df = pd.read_csv('@ES_quartile_hit_ratios.DF.csv', parse_dates=['DateTime'])
start_col = df.columns.get_loc('d4')
end_col = df.columns.get_loc('u4')

bit_count = None
f = open('LSTM_INPUT.csv', 'w')
for ix,r in df.iterrows():
    b,bstr = get_binary(r)
    if bit_count == None: bit_count = len(bstr)
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
    value = b
    f.write("{0}\n".format(value))
f.close()
print "bit count: {0}".format(bit_count)




global_start_time = time.time()
epochs  = 5

#seq_len = 50
seq_len = 20
prediction_len = 1
input_data_filename = 'LSTM_INPUT.csv'

normalise_window = True

f = open(input_data_filename, 'rb').read()
data = f.decode().split('\n')

sequence_length = seq_len + 1
result = []
for index in range(len(data) - sequence_length):
    result.append(data[index: index + sequence_length])

result0 = result

if normalise_window:
    result = lstm.normalise_windows(result)

result = np.array(result)

row = round(0.9 * result.shape[0])
train = result[:int(row), :]
np.random.shuffle(train)
x_train = train[:, :-1]
y_train = train[:, -1]
x_test = result[int(row):, :-1]
y_test = result[int(row):, -1]

sys.exit()

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))  

print [x_train, y_train, x_test, y_test]







X_train, y_train, X_test, y_test = lstm.load_data(input_data_filename, seq_len, True)

print("TRAINING ROWS: {0}     TEST ROWS: {1}".format(X_train.shape[0], X_test.shape[0]))

print('> Data Loaded. Compiling...')

#model = lstm.build_model([1, 50, 100, 1])
# Don't hardcode "50" but use seq_len instead because seq_len is the lookback length
# original model layers were [1, 50, 100, 1]
model = lstm.build_model([1, seq_len, seq_len*2, 1])

model.fit(
    X_train,
    y_train,
    batch_size=512,
    nb_epoch=epochs,
    validation_split=0.05)

# For now, set our prediction length to our (input) sequence length
#prediction_len = seq_len

predictions = lstm.predict_sequences_multiple(model, X_test, seq_len, prediction_len)
#predicted = lstm.predict_sequence_full(model, X_test, seq_len)
#predicted = lstm.predict_point_by_point(model, X_test)        

print('Training duration (s) : ', time.time() - global_start_time)

#lstm.plot_results_multiple(predictions, y_test, prediction_len)

predict = lstm.predict_point_by_point(model, X_test)
lstm.plot_results(predict, y_test)


