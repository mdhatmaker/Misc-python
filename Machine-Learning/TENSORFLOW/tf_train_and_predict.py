# https://stackoverflow.com/questions/42211833/tensorflow-how-to-predict-with-trained-model-on-a-different-test-dataset

"""
# So the first time, I trained the model and test, then I want to predict on the other test set:
t,p = train_and_predict() #training
t_test2, p_test2 = train_and_predict(restore=True, test_set='./test2')

# Functions load_dataset, create_datasetand reformat give me
# datasets with shape : (nb_pictures, 28, 28, 1)
# labels with shape : (nb_pictures, 10)

# You have everything that you need there. If you just want to predict, you can extract the function:
with tf.Session(graph=graph) as session:
    ckpt = tf.train.get_checkpoint_state('./model/')
    saver.restore(session, ckpt.model_checkpoint_path)
    feed_dict = {tf_train_dataset : batch_data}
    predictions = session.run([test_prediction], feed_dict)
"""

def train_and_predict(restore=False, test_set=None):
    """
    Training of the model, posibility to restore a trained model and predict on another dataset. 
    """
    batch_size = 50
    # Regular datasets for training
    train_dataset, train_labels, test_dataset, test_labels, valid_dataset, valid_labels = load_dataset(dataset_size)
    if restore:
       # change the testset if restoring the trained model
       test_dataset, test_labels = create_dataset(test_set)
       test_dataset, test_labels = reformat(test_dataset, test_labels)
       batch_size = number_predictions

    graph = tf.Graph()
    with graph.as_default():

       # Input data.
       tf_train_dataset = tf.placeholder(tf.float32, shape=(batch_size, image_size, image_size, num_channels))
       tf_train_labels = tf.placeholder(tf.float32, shape=(batch_size, num_labels))
       tf_valid_dataset = tf.constant(valid_dataset)
       tf_test_dataset = tf.constant(test_dataset)

       # Variables.
       K = 32  # first convolutional layer output depth
       L = 64  # second convolutional layer output depth
       N = 1024  # fully connected layer

       W1 = tf.Variable(tf.truncated_normal([5, 5, 1, K], stddev=0.1))  # 5x5 patch, 1 input channel
       B1 = tf.Variable(tf.constant(0.1, tf.float32, [K]))
       W2 = tf.Variable(tf.truncated_normal([5, 5, K, L], stddev=0.1))
       B2 = tf.Variable(tf.constant(0.1, tf.float32, [L]))

       W3 = tf.Variable(tf.truncated_normal([7 * 7 * L, N], stddev=0.1))
       B3 = tf.Variable(tf.constant(0.1, tf.float32, [N]))
       W4 = tf.Variable(tf.truncated_normal([N, 10], stddev=0.1))
       B4 = tf.Variable(tf.constant(0.1, tf.float32, [10]))

       # Model.
       def model(data, train = True):
           stride = 1 
           Y1 = tf.nn.relu(tf.nn.conv2d(data, W1, strides=[1, stride, stride, 1], padding='SAME') + B1)
           Y1 = tf.nn.max_pool(Y1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
           Y2 = tf.nn.relu(tf.nn.conv2d(Y1, W2, strides=[1, stride, stride, 1], padding='SAME') + B2)
           Y2 = tf.nn.max_pool(Y2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
           Y3 = tf.reshape(Y2, [-1, 7*7*64])
           Y4 = tf.nn.relu(tf.matmul(Y3, W3) + B3)
           if train:
               # drop-out during training
               Y4 = tf.nn.dropout(Y4, 0.5)
           return tf.matmul(Y4, W4) + B4

       # Training computation.
       logits = model(tf_train_dataset)
       loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits, tf_train_labels))

       # Optimizer.
       optimizer = tf.train.AdamOptimizer(1e-4).minimize(loss)

       # Predictions for the training, validation, and test data.
       train_prediction = tf.nn.softmax(logits)
       valid_prediction = tf.nn.softmax(model(tf_valid_dataset, False))
       test_prediction = tf.nn.softmax(model(tf_test_dataset, False))

       # Saver
       saver = tf.train.Saver()

     num_steps = 1001
     with tf.Session(graph=graph) as session:
        if restore:
            ckpt = tf.train.get_checkpoint_state('./model/')
            saver.restore(session, ckpt.model_checkpoint_path)
            _, l, predictions = session.run([optimizer, loss, test_prediction])
        else:
            tf.global_variables_initializer().run()
            for step in range(num_steps):
                offset = (step * batch_size) % (train_labels.shape[0] - batch_size)
                batch_data = train_dataset[offset:(offset + batch_size), :, :, :]
                batch_labels = train_labels[offset:(offset + batch_size), :]
                feed_dict = {tf_train_dataset : batch_data, tf_train_labels : batch_labels}
                _, l, predictions = session.run([optimizer, loss, train_prediction], feed_dict=feed_dict)
                if (step % 100 ==0):
                    saver.save(session, './model/' + 'model.ckpt', global_step=step+1)
                if (step % 1000 == 0):
                    print('\nMinibatch loss at step %d: %f' % (step, l))
        test_accuracy = accuracy(test_prediction.eval(), test_labels)
    return test_accuracy , predictions

