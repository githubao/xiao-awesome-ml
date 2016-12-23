#!/usr/bin/env python
# encoding: utf-8

"""
@description: keras 与 lstm 实现的情感模型分类

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: two_classification.py
@time: 2016/12/6 22:08
"""

import pandas as pd
import numpy as np
import jieba

from keras.preprocessing import sequence
from keras.optimizers import SGD, RMSprop, Adagrad
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM, GRU

from xiaolearn.util.settings import FILE_PATH

POS_FILE_PATH = FILE_PATH + 'mylstm/pos.xls'
NEG_FILE_PATH = FILE_PATH + 'mylstm/neg.xls'
COMMENT_FILE_PATH = FILE_PATH + 'mylstm/sum.xls'
RESULT_FILE_PATH = FILE_PATH + 'mylstm/result.xls'


def train_my():
    pos = pd.read_excel(POS_FILE_PATH, header=None, index=None)
    neg = pd.read_excel(NEG_FILE_PATH, header=None, index=None)

    pos['mark'] = 1
    neg['mark'] = 0

    pn = pd.concat([pos, neg], ignore_index=True)

    pos_len = len(pos)
    neg_len = len(neg)

    cw = lambda x: list(jieba.cut(x))

    pn['words'] = pn[0].apply(cw)

    comment = pd.read_excel(COMMENT_FILE_PATH)
    comment = comment[comment['rateContent'].notnull()]
    comment['words'] = comment['rateContent'].apply(cw)

    d2v_train = pd.concat([pn['words'], comment['words']], ignore_index=True)

    w = []
    for i in d2v_train:
        w.extend(i)

    dic = pd.DataFrame(pd.Series(w).value_counts())
    del w, d2v_train
    dic['id'] = list(range(1, len(dic) + 1))

    get_sent = lambda x: list(dic['id'][x])
    pn['sent'] = pn['words'].apply(get_sent)

    max_len = 50
    print('Pad sequences (sample x time)')
    pn['sent'] = list(sequence.pad_sequences(pn['sent'], maxlen=max_len))

    x = np.array(list(pn['sent']))[::2]
    y = np.array(list(pn['mark']))[::2]
    xt = np.array(list(pn['sent']))[1::2]
    yt = np.array(list(pn['mark']))[1::2]
    xa = np.array(list(pn['sent']))
    ya = np.array(list(pn['mark']))

    print('Building model...')
    model = Sequential()
    model.add(Embedding(len(dic) + 1, output_dim=256, input_length=max_len))
    model.add(LSTM(128))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', class_mode='binary')

    model.fit(xa, ya, batch_size=16, nb_epoch=10)

    classes = model.predict_classes(xa)
    acc = np_utils.accuracy(classes, ya)

    print("Test accuracy: {}".format(acc))

    pd.DataFrame(classes).to_excel(RESULT_FILE_PATH)


def train_demo():
    pos = pd.read_excel(POS_FILE_PATH, header=None, index=None)
    neg = pd.read_excel(NEG_FILE_PATH, header=None, index=None)

    pos['mark'] = 1
    neg['mark'] = 0

    pn = pd.concat([pos, neg], ignore_index=True)

    pos_len = len(pos)
    neg_len = len(neg)

    cw = lambda x: list(jieba.cut(x))

    pn['words'] = pn[0].apply(cw)

    comment = pd.read_excel(COMMENT_FILE_PATH)
    comment = comment[comment['rateContent'].notnull()]
    comment['words'] = comment['rateContent'].apply(cw)

    d2v_train = pd.concat([pn['words'], comment['words']], ignore_index=True)

    w = []
    for i in d2v_train:
        w.extend(i)

    dic = pd.DataFrame(pd.Series(w).value_counts())
    del w, d2v_train
    dic['id'] = list(range(1, len(dic) + 1))

    get_sent = lambda x: list(dic['id'][x])
    pn['sent'] = pn['words'].apply(get_sent)

    max_len = 50
    print('Pad sequences (sample x time)')
    pn['sent'] = list(sequence.pad_sequences(pn['sent'], maxlen=max_len))

    x = np.array(list(pn['sent']))[::2]
    y = np.array(list(pn['mark']))[::2]
    xt = np.array(list(pn['sent']))[1::2]
    yt = np.array(list(pn['mark']))[1::2]
    xa = np.array(list(pn['sent']))
    ya = np.array(list(pn['mark']))

    print('Building model...')
    model = Sequential()
    model.add(Embedding(len(dic) + 1, output_dim=256, input_length=max_len))
    model.add(LSTM(128))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', class_mode='binary')

    model.fit(xa, ya, batch_size=16, nb_epoch=10)

    classes = model.predict_classes(xa)
    acc = np_utils.accuracy(classes, ya)

    print("Test accuracy: {}".format(acc))

    pd.DataFrame(classes).to_excel(RESULT_FILE_PATH)


def main():
    train_demo()
    train_my()


if __name__ == '__main__':
    main()
