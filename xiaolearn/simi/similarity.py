#!/usr/bin/env python
# encoding: utf-8


"""
@description: 计算两个句子的相似度

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: qarank.py
@time: 2016/11/29 14:44
"""

import logging
import math
import sys
from operator import itemgetter

import numpy as np

from xiaolearn.mytfidf import tfidf
from xiaolearn.myword2vec import vec
from xiaolearn.qarank.preprocess import uniform_text
from xiaolearn.seg import segment
from xiaolearn.util.settings import FILE_PATH

logging.basicConfig(level=logging.INFO)

word_count = {}
all_count = 0

__all__ = [
    'two_seq_distance',
    'get_setence_vec'
]

TMP_VECTOR_FILE = FILE_PATH + 'qarank/qa_relate/tmp_vec.txt'


# 获取句子的向量
def get_setence_vec(line=None, seq=None):
    if not seq and not line:
        return

    if not seq and not isinstance(line, str):
        logging.error('use origin line request get_seq_vec')
        sys.exit(-1)

    if not seq:
        seq = segment.get_seg_list(line)

    # v = np.array([[0.1 for i in range(400)] for word in seq])
    # tmp_v = open(TMP_VECTOR_FILE, 'r', encoding='utf-8').readline().strip('\n')
    # v = [np.array(json.loads(tmp_v)) for word in seq]
    v = [vec.get_vec(word) for word in seq]

    w = tfidf.get_tfidf(seq)

    if v is None or w is None:
        return

    seq_vec = np.sum([a * b for a, b in zip(w, v)], axis=0)

    seq_vec = [float('{:0.3f}'.format(v)) for v in seq_vec]

    return seq_vec


def get_tfidf_vec(line=None, seq=None):
    if not seq and not line:
        return

    if not seq and not isinstance(line, str):
        logging.error('use origin line request get_seq_vec')
        sys.exit(-1)

    if not seq:
        seq = segment.get_seg_list(line)

    # v = np.array([[0.1 for i in range(400)] for word in seq])
    # tmp_v = open(TMP_VECTOR_FILE, 'r', encoding='utf-8').readline().strip('\n')
    # v = [np.array(json.loads(tmp_v)) for word in seq]
    v = [vec.get_vec(word) for word in seq]

    w = tfidf.get_tfidf(seq)

    if v is None or w is None:
        return

    # tfidf_vec = [(float('{:0.5f}'.format(a)), float('{:0.5f}'.format(b))) for a, b in zip(w, v)]

    # 按照tfidf分值的排序
    tfidf_vec = sorted(zip(w, v, seq), key=itemgetter(0), reverse=True)

    logging.debug('tf-idf info: {}'.format(['{}({})'.format(item[2], item[0]) for item in tfidf_vec]))

    return tfidf_vec


def two_seq_distance(line1=None, line2=None, seq1=None, seq2=None, v1=None, v2=None):
    if not seq1 and not line1:
        return

    if not seq2 and not seq2:
        return

    if not seq1:
        seq1 = segment.get_seg_list(line1)
        seq1 = uniform_text(seq1)
    if not seq2:
        seq2 = segment.get_seg_list(line2)
        seq2 = uniform_text(seq2)

    if not v1:
        v1 = [vec.get_vec(word) for word in seq1]
    if not v2:
        v2 = [vec.get_vec(word) for word in seq2]

    weight1 = tfidf.get_tfidf(seq1)
    weight2 = tfidf.get_tfidf(seq2)

    # v1 = np.array([[0.1 for i in range(100)] for word in seq1])
    # v2 = np.array([[0.1 for i in range(100)] for word in seq2])

    # weight1 = [0.2, 0.6, 0.2]
    # weight2 = [0.15, 0.1, 0.6, 0.15]

    if not (weight1 and weight2):
        logging.info('cal weight, err occur')
        return 0.0

    vec1 = np.array(np.sum([a * b for a, b in zip(weight1, v1)], axis=0)).reshape(1, -1)
    vec2 = np.array(np.sum([a * b for a, b in zip(weight2, v2)], axis=0)).reshape(-1, 1)

    if not vec1.all() or not vec2.all():
        logging.info('cal vec, err occur')
        return 0.0

    # qarank = np.dot(preprocessing.scale(vec1), preprocessing.scale(vec2))
    return two_seq_distance(vec1, vec1)


def numpy_vec_distance(vec1, vec2):
    # if isinstance(vec1, list):
    #     max = vec2.shape(1)
    #     vec1 = np.array([0.0 for _ in range(max)]).reshape(1, -1)

    try:
        simi = np.dot(vec1, vec2) / (vec_sqrt(vec1) * vec_sqrt(vec2))
    except:
        # traceback.print_exc()
        # logging.error("")
        return 0.0

    if simi:
        return float('{:0.3f}'.format(simi[0][0]))

    return 0.0


def vec_sqrt(vec):
    all = 0

    for line in vec:
        for item in line:
            all += item * item

    return math.sqrt(all)


def similarity(v1, v2):
    simi = dot_product(v1, v2) / (magnitude(v1) * magnitude(v2))
    if simi:
        return float('{:0.3f}'.format(simi))

    return 0.0


def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))


def magnitude(vector):
    return math.sqrt(dot_product(vector, vector))


def main():
    # print(seq(['我', '喜欢', '你'], ['我', '真的', '喜欢', '你']))
    s1 = '我喜欢你'
    s2 = '我真的喜欢你'

    simi = two_seq_distance(s1, s2)

    print('[{}] and [{}] qarank is {}'.format(s1, s2, simi))


if __name__ == '__main__':
    main()
