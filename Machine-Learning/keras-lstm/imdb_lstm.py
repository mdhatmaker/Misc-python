'''
Trains an LSTM model on the IMDB sentiment classification task.
The dataset is actually too small for LSTM to be of any advantage
compared to simpler, much faster methods such as TF-IDF + LogReg.
Notes:
- RNNs are tricky. Choice of batch size is important,
choice of loss and optimizer is critical, etc.
Some configurations won't converge.
- LSTM loss decrease patterns during training can be quite different
from what you see with CNNs/MLPs/etc.
'''

from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb
from keras.models import model_from_json

max_features = 20000
maxlen = 80     # cut texts after this number of words (among top max_features most common words)
batch_size = 32
epoch_count = 5     #15


print("Loading data...")
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
print(len(x_train), "train sequences")
print(len(x_test), "test sequences")

print("Pad sequences (sample x time)")
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
print("x_train shape:", x_train.shape)
print("x_test shape:", x_test.shape)

print("Build model...")
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print("Train...")
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epoch_count,
          validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test, batch_size=batch_size)

print("Test score:", score)
print("Test accuracy:", acc)






# prints a summary representation of your model
print(model.summary())

# returns dictionary containing the configuration of the model
config = model.get_config()

"""
# reinstantiate model from its config
config = model.get_config()
model = Model.from_config(config)
# or, for Sequential:
#model = Sequential.from_config(config)
"""

# returns a list of all weight tensors in the model, as Numpy arrays
model_weights = model.get_weights()

"""
# sets the values of the weights of the model, from a list of Numpy arrays
# (arrays in list should have the same shape as those returned by get_weights())
model.set_weights(model_weights)
"""

# returns a representation of the model as a JSON string
# NOTE: does NOT include the weights, only the architecture
str_json = model.to_json()
filepath = "./imdb_lstm.model.json"
with open(filepath, "w") as text_file:
    text_file.write(str_json)

"""
# reinstantiate the same model (with reinitialized weights) from the JSON string
str_json = model.to_json()
model = model_from_json(str_json)
# same thing but with YAML:
from keras.models import model_from_yaml

yaml_string = model.to_yaml()
model = model_from_yaml(yaml_string)
"""

# saves the weights of the model as a HDF5 file
filepath = "./imdb_lstm.model-weights.hdf5"
model.save_weights(filepath)

"""
# by default, architecture is expected to be unchanged
# to load weights into different architecture (with some layers in common), use by_name=True
model.load_weights(filepath, by_name=False)
"""











