from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.models import model_from_json
import numpy as np
import lstm, time  # helper libraries
import sys

#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot as plt

def save_json_model(model, model_filename):
    # serialize model to JSON
    model_json = model.to_json()
    model_filename = "my_predict_model.json"
    with open(model_filename, "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk: '{0}'".format(model_filename))
    return

def load_json_model(model_filename):
    # load json and create model
    #model_filename = "my_predict_model.json"
    json_file = open(model_filename, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("model.h5")
    print("Loaded model from disk: '{0}'".format(model_filename))
    return model

def load_data(filename):
    data = np.loadtxt(filename)
    X = data[:,:-1]
    Y = data[:,-1]
    return (X,Y)

def save_data(X, Y, filename):
    data = np.append(X, Y, axis=1)
    np.savetxt(filename, data)
    return

#Main Run Thread
if __name__=='__main__':

    model_filename = "my_predict_model.json"    ##### MODEL FILENAME #####

    
    model = load_json_model(model_filename)
    
    # split into input (X) and output (Y) variables
    #X = np.random.random((1000,100))
    #Y = np.random.randint(2, size=(1000,1))
    
    # Load the DATA
    (X,Y) = load_data("data.txt")
    predictions = model.predict(X)
    
    # evaluate loaded model on test data
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    score = model.evaluate(X, Y, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))

    sys.exit()

    
    # KERAS - A BASIC EXAMPLE
    data = np.random.random((1000,100))
    labels = np.random.randint(2, size=(1000,1))
    model = Sequential()
    model.add(Dense(32, activation='relu', input_dim=100))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(data,labels,epochs=10,batch_size=32)
    predictions = model.predict(data)

    save_data(data, labels, "data.txt")
    save_json_model(model, model_filename)  # Save the MODEL
    

    sys.exit()
    

    """
    # fix random seed for reproducibility
    np.random.seed(7)
    # load pima indians dataset
    dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")
    # split into input (X) and output (Y) variables
    X = dataset[:,0:8]
    Y = dataset[:,8]
    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=8, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
    sys.exit()
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
    # evaluate the model
    scores = model.evaluate(X, Y, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    """
    

    sys.exit()
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

