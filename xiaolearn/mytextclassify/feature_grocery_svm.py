#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用tgrocery 实现的分类

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: feature_grocery_svm.py
@time: 2016/12/5 16:51
"""

from tgrocery import Grocery
from xiaolearn.util.settings import FILE_PATH
import numpy as np
import random

data_file = FILE_PATH + "mytextclassify/train.txt"
train_file = FILE_PATH + "mytextclassify/train.txt"
test_file = FILE_PATH + "mytextclassify/train.txt"


def train():
    grocery = Grocery("sample")

    train_data = []
    test_data = []

    f = open(data_file, 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        if random.random() > 0.8:
            test_data.append(tuple(line))
        else:
            train_data.append(tuple(line))

    grocery.train(train_data)

    grocery.test(test_data)


def my_train():
    grocery = Grocery("sample")
    grocery.train(train_file)
    print(grocery.test(test_file))


def main():
    # train()
    my_train()


if __name__ == '__main__':
    main()
