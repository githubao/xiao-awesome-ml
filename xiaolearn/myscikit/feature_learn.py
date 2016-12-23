#!/usr/bin/env python
# encoding: utf-8

"""
@description: 从数据中提取特征

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: feature_learn.py
@time: 2016/11/29 21:10
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing
import numpy as np

corpus = [
    'The dog ate a sandwich and i ate a sandwich',
    'The wizard transfigured a sandwich'
]


def extract():
    vectorizer = TfidfVectorizer(stop_words='english')
    vector = vectorizer.fit_transform(corpus).todense()

    print(vector)
    print(vectorizer.vocabulary_)

    print(preprocessing.scale(vector))


def main():
    extract()


if __name__ == '__main__':
    main()
