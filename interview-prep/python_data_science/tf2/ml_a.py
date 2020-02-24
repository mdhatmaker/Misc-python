# machine learning: feature columns, your own layers, your own models
import tensorflow as tf
import numpy as np
import sys


### https://youtu.be/MyYPpmVPed0
### https://rubikscode.net/2019/04/22/ultimate-guide-to-tensorflow-2-0-in-python/


###############################################################################
# Build your own keras layers (or use one of the many built-in layers)
class PoincareNormalize(tf.keras.layers.Layer):
    def __init__(self, axis=1, epsilon=1e-5, **kwargs):
        super(PoinCareNormalize, self).__init__(**kwargs)
        self.axis = axisself.epsilon = epsilon

    def call(self, inputs):
        square_sum = tf.math.reduce_sum(tf.math.square(inputs), self.axis, keepdims=True)
        inv_norm = tf.math.rsqrt(square_sum)
        inv_norm = tf.math.minimum((1. - self.epsilon) * inv_norm, 1.)
        outputs = tf.math.multiply(x, x_inv_norm)
        return outputs

# Build your own keras models
class MyModel(tf.keras.Model):
    def __init__(self, num_classes=10, magic_number=64):
        super(MyModel, self).__init__(name='my_model')
        self.dense_1 = layers.Dense(32, activation='relu')
        self.dense_2 = layers.Dense(num_classes, activation='sigmoid')

    def call(self, inputs):
        # Define your forward pass here.
        x = self.dense_1(inputs) * self.magic_number
        return self.dense_2(x)

###############################################################################
# Enable your models to use TensorBoard (including performance profiling)
tb_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)

model.fit(x_train, y_train, epochs=5, validation_data=[x_test, y_test], callbacks=[tb_callback])


###############################################################################
# use "feature columns" to configure transformations on incoming data
user_id = tf.feature_column.categorical_column_with_identity('user_id', num_buckets=10000)

uid_embedding = tf.feature_column.embedding_column(user_id, 10)

columns = [uid_embedding,
            tf.feature_column.numeric_column('visits'),
            tf.feature_column.numeric_column('clicks')]
            
feature_layer = tf.keras.layers.DenseFeatures(columns)

model = tf.keras.models.Sequential([feature_layer, ...])

###############################################################################
# Allow for parallelization: tf.distribute.Strategy
# Strategy for multiple GPUs
strategy = tf.distribute.MirroredStrategy()
# Strategy for multiple nodes, each with multiple GPUs
#strategy = tf.distribute.MultiWorkerMirroredStrategy()

with strategy.scope():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, input_shape=[10]),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


###############################################################################
# Serialize your model into a "Saved Model"
# Deployment:
# TensorFlow Serving (uses gRPC and REST)
# TensorFlow Lite (mobile)
# TensorFlow JS

#model = kf.keras.models.Sequential([feature_layer, ...])
#...

model.save('/path/to/model', save_format='tf')

new_model = tf.keras.models.load_model('/path/to/model')
new_model.summary()



###############################################################################
model1 = tf.keras.models.Sequential([
    # inputs to neural network (150x150 images x3 color depth)
    tf.keras.layers.Flatten(input_shape=(150, 150, 3)),
    #tf.keras.layers.Dropout(0.5),
    # consider this to be 512 functions (in middle layer?)
    tf.keras.layers.Dense(512, activation='relu'),
    # output 3 "neurons" from neural network (3 outputs i.e. rock, paper, scissors)
    tf.keras.layers.Dense(3, activation='softmax')
])


model.summary()

# loss function determines how well/badly we did in predicting
# based on loss, optimizer function generates the next guess
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

history = model.fit_generator(train_generator, epochs=25, validation_data=validation_generator, verbose=1)

model.fit(..., epochs=100)


#sys.exit()



