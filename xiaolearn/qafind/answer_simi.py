#!/usr/bin/env python
# encoding: utf-8

"""
@description:同一句话，句子之间的相似程度

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: answer_simi.py
@time: 2016/12/5 18:28
"""

from operator import itemgetter

from simi import similarity
from xiaolearn.myword2vec import vec
from xiaolearn.seg import segment
from xiaolearn.util.settings import FILE_PATH

TRAIN_FILE = FILE_PATH + 'qafind/train.txt'
OUT_FILE = FILE_PATH + 'qafind/out.txt'

from collections import defaultdict

def cluster():
    f = open(TRAIN_FILE, 'r', encoding='utf-8')
    fw = open(OUT_FILE, 'w', encoding='utf-8')

    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]

    # line_vec = {}
    # for line in lines:
    #     vec = seq_vec.get_seq_vec(line)
    #     line_vec[line] = vec

    vec_score = {}
    for idx, line in enumerate(lines):
        fw.write('{}\n'.format(line))

        seq1 = segment.get_seg_list(line)
        vec1 = [vec.get_vec(word) for word in seq1]

        for item in lines:
            dis = similarity.two_seq_distance(line, item, seq1=seq1, v1=vec1)
            if dis and dis >= 0.7:
                vec_score[item] = dis

        sorted_score = sorted(vec_score.items(), key=itemgetter(1), reverse=True)
        for item in sorted_score:
            fw.write('{}\t{}\n'.format(item[0], item[1]))
        vec_score.clear()

        fw.write('\n')

        if idx >= 10:
            break

    f.close()
    fw.close()


def main():
    cluster()


if __name__ == '__main__':
    main()
