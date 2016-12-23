#!/usr/bin/env python
# encoding: utf-8


"""
@description: 利用lstm网络预测学习“加法”运算

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: predict_add.py
@time: 2016/11/5 18:49
"""

import copy, numpy as np

np.random.seed(0)


# compute sigmoid non linearity
def sigmoid(x):
    output = 1 / (1 + np.exp(-x))
    return output


# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output * (1 - output)


# training data set generation
int2binary = {}
binary_dim = 8

largest = pow(2, binary_dim)
binary = np.unpackbits(
        np.array([range(largest)], dtype=np.uint8).T, axis=1)

for i in range(largest):
    int2binary[i] = binary[i]

# input variables
alpha = 0.1
input_dim = 2
hidden_dim = 16
output_dim = 1

# initialize neural network weights
# from [0,1] to [-1,1]
synapse_0 = 2 * np.random.random((input_dim, hidden_dim)) - 1
synapse_1 = 2 * np.random.random((hidden_dim, output_dim)) - 1
synapse_h = 2 * np.random.random((hidden_dim, hidden_dim)) - 1

# 更新参数
synapse_0_update = np.zeros_like(synapse_0)
synapse_1_update = np.zeros_like(synapse_1)
synapse_h_update = np.zeros_like(synapse_h)

# training logic
# 一共进行多少次迭代
for j in range(100000):
    # generate a simple addition problem(a+b=c)
    a_int = np.random.randint(largest / 2)
    a = int2binary[a_int]

    b_int = np.random.randint(largest / 2)
    b = int2binary[b_int]

    c_int = a_int + b_int
    c = int2binary[c_int]

    # where we will store our best guess
    d = np.zeros_like(c)

    # 全局误差
    overallError = 0

    layer_2_deltas = []
    layer_1_values = []
    layer_1_values.append(np.zeros(hidden_dim))

    for position in range(binary_dim):
        # generate input and output
        x = np.array([[a[binary_dim - position - 1],
                       b[binary_dim - position - 1]]])

        y = np.array([[c[binary_dim - position - 1]]]).T

        # hidden layer
        # WO*X + Wh*Ct-1
        layer_1 = sigmoid(np.dot(x, synapse_0) + np.dot(layer_1_values[-1], synapse_h))

        # output layer
        # W1*C1
        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # miss loss
        layer_2_error = y - layer_2
        layer_2_deltas.append(layer_2_error * sigmoid_output_to_derivative(layer_2))

        # 记录总误差，便于后续观察模型的效果
        overallError += np.abs(layer_2_error[0])

        # decode estimate
        d[binary_dim - position - 1] = np.round(layer_2[0][0])

        # store hidden layer
        layer_1_values.append(copy.deepcopy(layer_1))

    # 用于记忆下一个时间周期用到的隐藏层的历史记忆值
    future_layer_1_delta = np.zeros(hidden_dim)

    for position in range(binary_dim):
        x = np.array([[a[position], b[position]]])
        layer_1 = layer_1_values[-position - 1]
        prev_layer_1 = layer_1_values[-position - 2]

        # error at output layer
        layer_2_delta = layer_2_deltas[-position - 1]

        # error at hidden layer
        layer_1_delta = (future_layer_1_delta.dot(synapse_h.T) + layer_2_delta.dot(
                synapse_1.T)) * sigmoid_output_to_derivative(layer_1)

        synapse_1_update += np.atleast_2d(layer_1).T.dot(layer_2_delta)
        synapse_h_update += np.atleast_2d(prev_layer_1).T.dot(layer_1_delta)
        synapse_0_update += x.T.dot(layer_1_delta)

        future_layer_1_delta = layer_1_delta

    synapse_0 += synapse_0_update * alpha
    synapse_1 += synapse_1_update * alpha
    synapse_h += synapse_h_update * alpha

    synapse_0_update *= 0
    synapse_1_update *= 0
    synapse_h_update *= 0

    if (j % 1000 == 0):
        print("Error: {}".format(overallError))
        print("Pred: {}".format(d))
        print("True: {}".format(c))

        out = 0
        for index, x in enumerate(reversed(d)):
            out += x * pow(2, index)

        print("{}+{}={}".format(a_int, b_int, out))
        print("-" * 30)


def main():
    print("do sth")


if __name__ == '__main__':
    main()
