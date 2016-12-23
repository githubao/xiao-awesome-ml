#!/usr/bin/env python
# encoding: utf-8

"""
@description: tf 入门

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: step_into_tf.py
@time: 2016/11/28 19:17
"""

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
from xiaolearn.util.settings import FILE_PATH


def tf_toy_func():
    matrix1 = tf.constant([[3, 3]])
    matrix2 = tf.constant([[2], [2]])

    product = tf.matmul(matrix1, matrix2)

    with tf.Session() as sess:
        with tf.device('/gpu:1'):
            result = sess.run(product)
            print(result)

            pass


def tf_add():
    state = tf.Variable(0, name='counter')

    one = tf.constant(1)
    new_value = tf.add(state, one)
    update = tf.assign(state, new_value)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        print(sess.run(state))

        for _ in range(3):
            sess.run(update)
            print(sess.run(state))


def tf_feed():
    input1 = tf.placeholder(tf.float32)
    input2 = tf.placeholder(tf.float32)
    output = tf.mul(input1, input2)

    with tf.Session() as sess:
        print(sess.run([output], feed_dict={
            input1: [7],
            input2: [2],
        }))


def tf_line_fit():
    x_data = np.random.random_sample(100).astype('float32')
    y_data = x_data * 0.1 + 0.3

    W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    b = tf.Variable(tf.zeros([1]))
    y = W * x_data + b

    loss = tf.reduce_mean(tf.square(y - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)

    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init)

    for step in range(201):
        sess.run(train)

        if step % 20 == 0:
            print(step, sess.run(W), sess.run(b))


def tf_mnist_learn():
    mnist = input_data.read_data_sets(FILE_PATH + "mnist/", one_hot=True)
    print('Download complete')

    x = tf.placeholder(tf.float32, [None, 784])

    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    y = tf.nn.softmax(tf.matmul(x, W) + b)
    y_ = tf.placeholder(tf.float32, [None, 10])

    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init)

    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={
            x: batch_xs,
            y_: batch_ys
        })

    correct_prediction = tf.equal(tf.arg_max(y, 1), tf.arg_max(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))

    print('Accuracy on test-dataSet: {:.3f}'.format(sess.run(accuracy, feed_dict={
        x: mnist.test.images,
        y_: mnist.test.labels
    })))


def main():
    # tf_toy_func()
    # tf_add()
    # tf_feed()
    # tf_line_fit()
    tf_mnist_learn()


if __name__ == '__main__':
    main()
