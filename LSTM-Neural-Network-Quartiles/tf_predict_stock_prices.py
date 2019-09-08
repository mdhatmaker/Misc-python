from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm, time  # helper libraries
import sys

#Main Run Thread
if __name__=='__main__':
    global_start_time = time.time()
    epochs  = 1
    seq_len = 50

    print('> Loading data... ')

    X_train, y_train, X_test, y_test = lstm.load_data('sp500.csv', seq_len, True)

    print('> Data Loaded. Compiling...')

    model = lstm.build_model([1, 50, 100, 1])

    model.fit(
        X_train,
        y_train,
        batch_size=512,
        nb_epoch=epochs,
        validation_split=0.05)

    predictions = lstm.predict_sequences_multiple(model, X_test, seq_len, 50)
    #predicted = lstm.predict_sequence_full(model, X_test, seq_len)
    #predicted = lstm.predict_point_by_point(model, X_test)        

    print('Training duration (s) : ', time.time() - global_start_time)
    lstm.plot_results_multiple(predictions, y_test, 50)





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

