#!/usr/bin/env python
# encoding: utf-8


"""
@description: lstm word2vec seq2seq 生成聊天对话语料

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: one_lstm_sequence_generate.py
@time: 2016/11/26 16:04
"""

import math
import os
import sys

import numpy as np
import tflearn

from xiaolearn.seg import segment
from xiaolearn.util import timer
from xiaolearn.util.settings import FILE_PATH
import gensim

seq = []
max_w = 50
float_size = 4
# word_vector_dict = {}

model = None

ZHENHUAN_FILE = FILE_PATH + 'chatbot/zhenghuanti.segment'
# VECTOR_FILE = FILE_PATH + 'myword2vec/zh_wiki_vectors.bin'
VECTOR_FILE = FILE_PATH + 'myword2vec/zh_wiki_vectors.bin.test'

TRAIN_FILE = FILE_PATH + 'chatbot/zhenghuanti.txt'
SEGMENT_FILE = FILE_PATH + 'chatbot/zhenghuanti.segment'
OUTPUT_FILE = FILE_PATH + 'chat_bot/chat_bot.model'


@timer.log_time
def load_vectors():
    # print(get_vec('你'))
    global model
    model = gensim.models.Word2Vec.load_word2vec_format(FILE_PATH + 'myword2vec/zh_wiki_vectors.bin', binary=True)


@timer.log_time
def init_seq():
    global model

    file_object = open(ZHENHUAN_FILE, 'r', encoding='utf-8')
    vocab_dict = {}

    while 1:
        line = file_object.readline()
        if line:
            for word in line.split(' '):
                if word in model.index2word:
                    seq.append(model[word])
        else:
            break

    file_object.close()


def vector_sqrtlen(vector):
    len = 0
    for item in vector:
        len += item * item

    return math.sqrt(len)


def vector_consin(v1, v2):
    if len(v1) != len(v2):
        sys.exit(-1)

    sqrt_len1 = vector_sqrtlen(v1)
    sqrt_len2 = vector_sqrtlen(v2)

    value = 0
    for item1, item2 in zip(v1, v2):
        value += item1 * item2

    return value / (sqrt_len1 * sqrt_len2)


def vector2word(vector):
    global model

    max_cos = -10000
    match_word = ''

    for word in model.index2word:
        v = model[word]
        cosine = vector_consin(vector, v)
        if cosine > max_cos:
            max_cos = cosine
            match_word = word

    return (match_word, max_cos)


@timer.log_time
def seg_word():
    if not os.path.exists(SEGMENT_FILE):
        segment.seg(TRAIN_FILE, SEGMENT_FILE)
    else:
        print('segment file exits')


@timer.log_time
def train():
    seg_word()
    load_vectors()
    init_seq()

    x_list = []
    y_list = []
    test_X = None

    for i in range(10):
        sequence = seq[i:i + 20]
        x_list.append(sequence)
        y_list.append(seq[i + 20])
        if test_X is None:
            test_X = np.array(sequence)
            (match_word, max_cos) = vector2word(seq[i + 20])
            print('right answer: {},{}'.format(match_word, max_cos))

    X = np.array(x_list)
    Y = np.array(y_list)

    net = tflearn.input_data([None, 20, 200])
    net = tflearn.lstm(net, 200)
    net = tflearn.fully_connected(net, 200, activation='linear')
    net = tflearn.regression(net, optimizer='sgd', learning_rate=0.1, loss='mean_square')

    model = tflearn.DNN(net)
    model.fit(X, Y, n_epoch=500, batch_size=10, snapshot_epoch=False, show_metric=True)
    model.save(OUTPUT_FILE)

    predict = model.predict([test_X])

    (match_word, max_cos) = vector2word((predict[0]))
    print('predict: {},{}'.format(match_word, max_cos))


def main():
    train()


if __name__ == '__main__':
    main()

    # @timer.log_time
# def load_vectors():
#     print('begin load vectors')
#
#     input_file = open(VECTOR_FILE, 'rb')
#
#     words_and_size = input_file.readline()
#     words_and_size = words_and_size.strip()
#     words = int(words_and_size.split(b' ')[0])
#     size = int(words_and_size.split(b' ')[0])
#
#     print('words num: {}, vec size: {}'.format(words, size))
#
#     for b in range(words):
#         a = 0
#         word = bytes()
#         while 1:
#             c = input_file.read(1)
#             word = word + c
#             if not c.decode().strip():
#                 break
#             if a < max_w and c != '\n':
#                 a = a + 1
#         word = word.decode().strip()
#
#         vector = []
#         for index in range(0, size):
#             m = input_file.readline(float_size)
#             (weight,) = struct.unpack('f', m)
#             vector.append(weight)
#
#         word_vector_dict[word] = vector
#
#     input_file.close()
#     print('load vectors finish')
