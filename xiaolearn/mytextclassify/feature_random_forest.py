#!/usr/bin/env python
# encoding: utf-8

"""
@description: 特征提取

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: feature_random_forest.py
@time: 2016/11/29 18:17
"""

import logging

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from simi import similarity
from xiaolearn.util.settings import FILE_PATH

TRAIN_FILE = FILE_PATH + 'qarank/random_forest/train.txt'
ORIGIN_FILE = FILE_PATH + 'qarank/random_forest/origin.txt'


def demo():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.75
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    df.head()

    train, test = df[df['is_train'] == True], df[df['is_train'] == False]

    features = df.columns[:4]
    clf = RandomForestClassifier(n_jobs=2)
    y, _ = pd.factorize(train['species'])
    clf.fit(train[features], y)

    preds = iris.target_names[clf.predict(test[features])]
    res = pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])
    print(res)


def my_demo():
    my_feature_names = ['feature_{}'.format(i + 1) for i in range(0, 400)]
    # my_feature_names = ['feature_{}'.format(i + 1) for i in range(0, 4)]

    # my_target_names = ['target_{}'.format(i + 1) for i in range(0, 400)]
    # my_target_names = ['dirty', 'obscure','sexy','violent']
    # my_target_names = ['a', 'b','c','d']

    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=my_feature_names)
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.75
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    df.head()

    train, test = df[df['is_train'] == True], df[df['is_train'] == False]

    features = df.columns[:400]
    clf = RandomForestClassifier(n_jobs=2)
    y, _ = pd.factorize(train['species'])
    clf.fit(train[features], y)

    preds = iris.target_names[clf.predict(test[features])]
    res = pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])
    print(res)


def init_data():
    d = [ 'dirty', 'obscure','sexy','violent']

    f = open(ORIGIN_FILE, 'r', encoding='utf-8')
    fw = open(TRAIN_FILE, 'w', encoding='utf-8')

    lines = f.readlines()

    fw.write('{},{},{}\n'.format("#{num}", 400, ','.join(d)))
    for line in lines:
        line = line.strip('\n')
        data, feature = line.split('\t')

        vec_seq = similarity.get_setence_vec(data)
        if vec_seq is None:
            logging.error('get vec seq failed: {}'.format(data))
            continue

        index = -1
        for idx, cls in enumerate(d):
            if cls == feature:
                index = idx
                break

        fw.write('{},{}\n'.format(','.join('%s' % s for s in vec_seq), index))

    fw.close()
    f.close()


def main():
    # demo()
    my_demo()
    # init_data()


if __name__ == '__main__':
    main()
