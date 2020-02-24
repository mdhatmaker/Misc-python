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

## NOTE: I think this was created for TensorFlow 1.0!

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

    

