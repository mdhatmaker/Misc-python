# machine learning: 
import tensorflow as tf


### https://www.youtube.com/watch?v=lEljKc9ZtU8
### bit.ly/mini-dream
### tensorflow.org/alpha/tutorials/generative/style_transfer

# Neural Machine Translation
### bit.ly/mini-nmt
### tensorflow.org/alpha/tutorials/text/nmt_with_attention

# Best-Fit Line
### bit.ly/tf_linear
### tensorflow.org/alpha/tutorials/quickstart/beginner



###############################################################################

"""
## TensorFlow 1.0 Style
x = tf.placeholder(tf.float32, [None, 200])

W = tf.Variable(tf.zeros([200, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# ...

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    tf.train.start_queue_runners(sess)

    example_batch = tf.train.batch([x], batch_size=10, num_threads=4, capacity=10)

    max_steps = 1000
    for step in range(max_steps):
        x_in = sess.run(example_batch)
        sess.run(train_step, feed_dict={x: train_data, y_: train_labels})
        if (step % 100) == 0:
            print(step, sess.run(accuracy, feed_dict={x: test_data, y_:test_labels}))
"""

## TensorFlow 2.0 Style

# tf.keras as the recommended high-level API.
# Eager execution by default. tf.add(2,3) -> immediate response
 
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)


