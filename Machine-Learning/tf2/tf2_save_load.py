from __future__ import absolute_import, division, print_function, unicode_literals
import os, sys
import tensorflow as tf
from tensorflow import keras

### https://www.tensorflow.org/tutorials/quickstart/beginner
### https://www.tensorflow.org/tutorials/keras/save_and_load


print(tf.version.VERSION)

tf.keras.backend.set_floatx('float64')  # change all layers to have dtype float64 by default

# -----------------------------------------------------------------------------

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0



# These global vars will change (even within function calls)
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)



# -----------------------------------------------------------------------------
# Define a simple sequential model
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10)
  ])

  model.compile(optimizer='adam',
                loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
  return model


''' Set the global vars checkpoint_path and checkpoint_dir '''
def set_checkpoint_path(path):
    global checkpoint_path, checkpoint_dir
    checkpoint_path = path
    checkpoint_dir = os.path.dirname(checkpoint_path)
    print("CHECKPOINT_DIR: '{}'      dir exists? {}".format(checkpoint_dir, os.path.isdir(checkpoint_dir)))
    return


''' Create a tf.keras.callbacks.ModelCheckpoint callback that saves weights only
# during training: '''
def train_and_save_weights(path):
    global checkpoint_path, checkpoint_dir
    set_checkpoint_path(path)

    # Create a basic model instance
    model = create_model()

    # Display the model's architecture
    model.summary()

    # NOTE: The tf.keras.callbacks.ModelCheckpoint callback allows to continually
    # save the model both during and at the end of training.

    # Create a callback that saves the model's weights
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                    save_weights_only=True,
                                                    verbose=1)

    # This may generate warnings related to saving the state of the optimizer.
    # These warnings (and similar warnings throughout this notebook)
    # are in place to discourage outdated usage, and can be ignored.

    # Train the model with the new callback
    model.fit(train_images, train_labels, epochs=10,
                validation_data=(test_images,test_labels),
                callbacks=[cp_callback])    # Pass callback to training                                      
    return model
    

''' Train a new model, and save uniquely named checkpoints once every five epochs: '''
def train_and_save_weights2(path):
    global checkpoint_path, checkpoint_dir
    set_checkpoint_path(path)
    
    # Include the epoch in the file name (uses `str.format`)
    #checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
    #checkpoint_dir = os.path.dirname(checkpoint_path)

    # Create a callback that saves the model's weights every 5 epochs
    cp_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_path, 
        verbose=1, 
        save_weights_only=True,
        period=5)
        
    model = create_model()  # Create a new model instance
    # Save the weights using the `checkpoint_path` format
    model.save_weights(checkpoint_path.format(epoch=0))

    # Train the model with the new callback
    model.fit(train_images, 
                train_labels,
                epochs=50, 
                callbacks=[cp_callback],
                validation_data=(test_images,test_labels),
                verbose=0)
    return model


''' Create a new, untrained model. When restoring a model from weights-only, you
    must have a model with the same architecture as the original model. Since it's
    the same model architecture, you can share weights despite that it's a
    different instance of the model. '''
def load_model_weights(chkpt_path):
    # Now rebuild a fresh, untrained model, and evaluate it on the test set.
    # An untrained model will perform at chance levels (~10% accuracy):
    model = create_model()  # Create a basic model instance
    #print("Untrained model, accuracy: {:5.2f}%\n".format(100*acc))
    evaluate_model(model)
    # Then load the weights from the checkpoint and re-evaluate:
    model.load_weights(chkpt_path)  # Loads the weights
    evaluate_model(model)
    return model


# where path like "training_2/cp-{epoch:04d}.ckpt"
def load_model_weights2(path):
    global checkpoint_path, checkpoint_dir
    set_checkpoint_path(path)

    latest = tf.train.latest_checkpoint(checkpoint_dir)
    print(f"LATEST CHECKPOINT: {latest}")

    # Reset the model and load the latest checkpoint:
    model = create_model()  # Create a new model instance
    model.load_weights(latest)  # Load the previously saved weights
    evaluate_model(model)
    return model

''' MANUALLY SAVE WEIGHTS '''
# where path like './checkpoints/my_checkpoint'
def save_weights(model, path):
    global checkpoint_path, checkpoint_dir
    set_checkpoint_path(path)

    model.save_weights(checkpoint_path) # Save the weights
    return

''' MANUALLY SAVE WEIGHTS '''
# where path like './checkpoints/my_checkpoint'
def load_weights(path):
    global checkpoint_path, checkpoint_dir
    set_checkpoint_path(path)

    model = create_model()  # Create a new model instance
    model.load_weights(checkpoint_path) # Restore the weights
    evaluate_model(model)
    return model


''' Save the entire model to a HDF5 file. '''
# where model_filename like "my_model.h5"
def save_model(model_filename):
    # The '.h5' extension indicates that the model should be saved to HDF5.
    model.save(model_filename) 
    return

''' Load entire model from a HDF5 file. '''
# where model_filename like "my_model.h5"
def load_model(model_filename):
    # Recreate the exact same model, including its weights and the optimizer
    new_model = tf.keras.models.load_model(model_filename)
    new_model.summary()     # Show the model architecture
    return new_model

def evaluate_model(model):
    loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
    print('Restored model, accuracy: {:5.2f}%'.format(100*acc))
    return

# -----------------------------------------------------------------------------


# Uncomment following line if you need to (re)train the model:
#model = train_and_save_weights("training_1/cp.ckpt")

# Load previously saved model weights and evaluate model accuracy
model = load_model_weights("training_1/cp.ckpt")

# Checkpoint callback options
# The callback provides several options to provide unique names for checkpoints
# and adjust the checkpointing frequency.
#model = train_and_save_weights2("training_2/cp-{epoch:04d}.ckpt")

model = load_model_weights2("training_2/cp-{epoch:04d}.ckpt")







sys.exit()




# -----------------------------------------------------------------------------

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# For each example the model returns a vector of "logits" or "log-odds" scores,
# one for each class.
predictions = model(x_train[:1]).numpy()
print(predictions)

# The tf.nn.softmax function converts these logits to "probabilities" for each class:
predictions_probabilities = tf.nn.softmax(predictions).numpy()
print(predictions_probabilities)

# The losses.SparseCategoricalCrossentropy loss takes a vector of logits and
# a True index and returns a scalar loss for each example.
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# This loss is equal to the negative log probability of the the true class: It
# is zero if the model is sure of the correct class.

# This untrained model gives probabilities close to random (1/10 for each class),
# so the initial loss should be close to -tf.log(1/10) ~= 2.3.
print(loss_fn(y_train[:1], predictions).numpy())

model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])

# The Model.fit method adjusts the model parameters to minimize the loss:
model.fit(x_train, y_train, epochs=5)

# The Model.evaluate method checks the models performance, usually on a "Validation-set".
model.evaluate(x_test, y_test, verbose=2)

# If you want your model to return a probability, you can wrap the trained model,
# and attach the softmax to it:
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
probability_model(x_test[:5])







