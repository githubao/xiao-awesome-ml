#!/usr/bin/env python
# encoding: utf-8

"""
@description: 利用词向量封装的一些方法

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: vec.py
@time: 2016/11/26 14:35
"""

from xiaolearn.util import timer
from xiaolearn.util.settings import FILE_PATH

model = None
import gensim
import traceback
import logging
import numpy as np

@timer.log_time
def load_model():
    return gensim.models.Word2Vec.load_word2vec_format(FILE_PATH + 'myword2vec/zh_wiki_vectors.bin', binary=True)


def get_vec(word):
    if not word:
        return None

    global model
    if not model:
        model = load_model()

    try:
        vec = model[word]
    except KeyError as e:
        logging.debug('{} not found in dict'.format(word))
        vec = np.zeros(model.vector_size)
    except:
        traceback.print_exc()
        return None

    vec = [float('{:0.3f}'.format(f)) for f in vec]

    return np.array(vec)


def seq_simi(a,b):
    global model
    if not model:
        model = load_model()

    return model.n_similarity(a,b)

def main():
    # print(seq_simi(['我','爱','你'],['我','真的','爱','你']))
    print(get_vec("喜欢"))


if __name__ == '__main__':
    main()

