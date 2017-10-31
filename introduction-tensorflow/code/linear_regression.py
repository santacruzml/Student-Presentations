"""
This code is based on the 'Getting Started with TensorFlow' tutorial,
see the tutorial for more examples/details:

https://www.tensorflow.org/get_started/get_started
"""
from __future__ import print_function

import tensorflow as tf


# Build the graph.
with tf.name_scope('inputs'):
    # Placeholders allow a graph to accept external
    # inputs, they are a promise to provide a value
    # later i.e. post graph creation.
    x = tf.placeholder(tf.float32, name='x')
    y = tf.placeholder(tf.float32, name='y')

with tf.name_scope('model'):
    # Variables allow us to add trainable parameters
    # to a graph.
    W = tf.Variable([.3], name='W')
    b = tf.Variable([-.3], name='b')

    predicted_y = W * x + b

with tf.name_scope('loss'):
    # Sum of squares.
    loss = tf.reduce_sum(tf.square(predicted_y - y))

learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train = optimizer.minimize(loss)

summary_op = tf.summary.scalar('loss', loss)

# Run the graph.
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# To evaluate the nodes, we must run the computation graph
# within a session.
with tf.Session() as sess:
    # Write graph to file for TensorBoard visualization.
    writer = tf.summary.FileWriter("logs", sess.graph)

    # Variables are not initialized when you call
    # tf.Variable. To initialize all the variables
    # in a TensorFlow program, we must explicitly
    # call tf.global_variables_initializer.
    sess.run(tf.global_variables_initializer())

    # Training loop.
    for i in range(1000):
        # Run the train and summary_op nodes.
        # Feed x_train and y_train into the
        # placeholder nodes, as well.
        feed_dict = {x: x_train, y: y_train}
        _, loss_summary = sess.run([train, summary_op], feed_dict)

        # Write loss to file for TensorBoard visualization.
        writer.add_summary(loss_summary, i)

    # Evaluate the final training loss, W, and b.
    curr_W, curr_b, curr_loss = sess.run([W, b, loss], feed_dict)
    print('W: {} b: {} loss: {}'.format(curr_W, curr_b, curr_loss))
