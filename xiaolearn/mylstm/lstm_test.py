#!/usr/bin/env python
# encoding: utf-8


"""
@description: //TODO 

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: lstm_test.py
@time: 2016/11/5 23:29
"""

import numpy as np
from xiaolearn.mylstm.lstm_impl import LstmParam,LstmNetwork

class ToyLossLayer:
    @classmethod
    def loss(cls,pred,label):
        return (pred[0] - label) ** 2

    @classmethod
    def bottom_diff(cls,pred,label):
        diff = np.zeros_like(pred)
        diff[0] = 2* (pred[0]-label)
        return diff

def example_0():
    np.random.seed(0)

    mem_cell_ct = 100
    x_dim = 50
    concat_len = x_dim + mem_cell_ct
    lstm_param = LstmParam(mem_cell_ct,x_dim)
    lstm_net = LstmNetwork(lstm_param)
    y_list = [-0.5,0.2,0.1,-0.5]
    input_val_arr = [np.random.random(x_dim) for _ in y_list]

    for cur_iter in range(100):
        print("cur iter: {}".format(cur_iter))
        for idx in range(len(y_list)):
            lstm_net.x_list_add(input_val_arr[idx])
            print("y_pred[{}] : {}".format(idx,lstm_net.lstm_node_list[idx].state.h[0]))

        loss = lstm_net.y_list_is(y_list,ToyLossLayer)
        print("loss: {}".format(loss))
        lstm_param.apply_diff(lr = 0.1)
        lstm_net.x_list_clear()


def main():
    example_0()


if __name__ == '__main__':
    main()

