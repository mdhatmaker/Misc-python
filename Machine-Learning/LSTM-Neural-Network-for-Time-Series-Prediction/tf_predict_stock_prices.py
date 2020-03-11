from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm, time  # helper libraries
import sys
import pandas as pd


sys.path.append('/Users/michael/Dropbox/alvin/python')
from f_data_folder import *
import f_dataframe as fdf


#Main Run Thread
if __name__=='__main__':
    global_start_time = time.time()
    epochs  = 1
    #seq_len = 50

    print('> Loading data... ')

    use_data_other_than_sp500 = False
    if use_data_other_than_sp500:
        seq_len = 40
        prediction_len = 20
        input_data_filename = "contango.csv"
        df = fdf.read_dataframe(join(data_folder, "vix_es", "es_vix_daily_summary.DF.csv"))
        minx = df.Close_Contango.min()
        if (minx <= 0):
            offset = abs(minx) + 1.0
            print("OFFSET (TO ENSURE NON-ZERO VALUES) = {0}".format(offset))
        else:
            offset = 0.0
        f = open(input_data_filename, 'w')
        for ix,r in df.iterrows():
            # We need to adjust this so there are no ZEROS in the data
            f.write("{0}\n".format(r['Close_Contango'] + offset))
    else:
        seq_len  = 50
        prediction_len = 50
        input_data_filename = 'sp500.csv'

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

    # For now, set our prediction length to our (input) sequnce length
    #prediction_len = seq_len
 
    predictions = lstm.predict_sequences_multiple(model, X_test, seq_len, prediction_len)
    #predicted = lstm.predict_sequence_full(model, X_test, seq_len)
    #predicted = lstm.predict_point_by_point(model, X_test)        

    print('Training duration (s) : ', time.time() - global_start_time)
    lstm.plot_results_multiple(predictions, y_test, prediction_len)






sys.exit()

# Step 1 Load Data
X_train, y_train, X_test, y_test = lstm.load_data('sp500.csv', 50, True)

# Step 2 Build the Model
model = Sequential()
model.add(LSTM(
    input_dim=1,
    output_dim=50,
    return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(
    100,
    return_sequences=False))
model.add(Dropout(0.2))

model.add(Dense(
    output_dim=1))
model.add(Activation('linear'))

start = time.time()
model.compile(loss='mse', optimizer='rmsprop')
print 'compilation time:', time.time() - start

# Step 3 Train the Model
model.fit(
    X_train,
    y_train,
    batch_size=512,
    nb_epoch=1,
    validation_split=0.05)

# Step 4 Plot the Predictions
predictions = lstm.predict_sequences_multiple(model, X_test, 50, 50)
lstm.plot_results_multiple(predictions, y_test, 50)

