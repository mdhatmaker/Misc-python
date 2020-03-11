import tensorflow as tf

# first, create a TensorFlow constant
const = tf.constant(2.0, name='const')

# create TensorFlow variables
b = tf.Variable(2.0, name='b')
c = tf.Variable(1.0, name='c')

# now create some operations
d = tf.add(b, c, name='d')
e = tf.add(c, const, name='e')
a = tf.multiply(d, e, name='a')

# setup the variable initialization
init_op = tf.global_variables_initializer()

# start the session
with tf.Session() as sess:
    # initialize the variables
    sess.run(init_op)
    # comput the output of the graph
    a_out = sess.run(a)
    print("Variable a is {}".format(a_out))

