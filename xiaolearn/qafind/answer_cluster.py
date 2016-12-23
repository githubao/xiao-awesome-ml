#!/usr/bin/env python
# encoding: utf-8

"""
@description: 聚类答案

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: answer_cluster.py
@time: 2016/12/8 20:19
"""

import logging
import sys
import traceback
from collections import defaultdict

from xiaolearn.cluster.vectorizer_paragraph import cluster_paragraphs
from xiaolearn.qarank.preprocess import rm_line_punc
from xiaolearn.util.timer import log_time

# TRAIN_FILE = FILE_PATH + 'qafind/smoothy_f_corpus.txt'
# OUT_FILE = FILE_PATH + 'qafind/clustered_sf_corpus.txt'

DEFAULT_SCORE = 0.4


@log_time
def cluster():
    dic = defaultdict(set)

    TRAIN_FILE = sys.argv[1]
    OUT_FILE = sys.argv[2]

    f = open(TRAIN_FILE, 'r', encoding='utf-8')
    fw = open(OUT_FILE, 'w', encoding='utf-8')

    lines = f.readlines()
    lines = [line.strip() for line in lines]

    for line in lines:
        (myid, ques, *_) = line.split('\t')
        dic[ques].add(line)

    logging.info('{} items to cluster'.format(len(dic)))
    cnt = 0
    for key, lines in dic.items():
        answers = {line.split('\t')[2] for line in lines}
        answers = {rm_line_punc(answer) for answer in answers}

        cluster_num = 0
        ans_len = len(answers)

        # 少于三个，不需要聚类
        if ans_len <= 3:
            logging.info('{} less than 3 answers'.format(ans_len))
            cluster_num = 1
            for line in lines:
                fw.write("{}\t{}\t{:0.5f}\n".format(line, cluster_num, DEFAULT_SCORE))
            continue

        try:
            cluster_num = get_cluster_cnt(ans_len)
            logging.info('{} cluster {} classes'.format(ans_len, cluster_num))
            clustered_answer = cluster_paragraphs(answers, num_clusters=cluster_num)
            sorted_answer = sorted(clustered_answer, key=lambda x: len(x), reverse=True)
        except:
            traceback.print_exc()
            logging.error('err occur while cluster data')
            sorted_answer = [[]]

        for line in lines:
            # 每一条数据，默认的分值
            score = 0

            answer = rm_line_punc(line.split('\t')[2])
            for idx, cluster in enumerate(sorted_answer):
                if answer in cluster:
                    decrease = idx
                    x = 1 - decrease / cluster_num
                    score = func(x)
                    break

            else:
                logging.error('not found {} in cluster'.format(answer))

            fw.write("{}\t{}\t{:0.5f}\n".format(line, cluster_num, score))

        cnt += 1
        if cnt % 1000 == 0:
            logging.info('cluster processing data: {}'.format(cnt))


def main():
    cluster()


def get_cluster_cnt(cluster_nums):
    if 3 < cluster_nums <= 10:
        cnt = 3
    elif 10 < cluster_nums <= 20:
        cnt = 5
    else:
        cnt = 8
    return cnt


def print_cluster(clusters):
    for i, cluster in enumerate(clusters):
        print('cluster: {}'.format(i + 1))
        print('\n'.join(cluster))


def func(x):
    return 0.4 * x * x + 0.6 * x


def test():
    clustered_answer = [[1, 2, 3], [1, 2], [1, 2, 3, 4]]

    sorted_answer = sorted(clustered_answer, key=lambda x: len(x), reverse=True)

    print(sorted_answer)


if __name__ == '__main__':
    main()
