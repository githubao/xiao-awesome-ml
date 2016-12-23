#!/usr/bin/env python
# encoding: utf-8

"""
@description: tf-idf的一些接口

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: tfidf.py
@time: 2016/12/2 18:06
"""

import logging
import math
import sys
import traceback
from operator import itemgetter

from xiaolearn.util import timer
from xiaolearn.util.settings import FILE_PATH

min_sum = 3

word_count = {}
all_count = 0


def get_word_cnt(word):
    global word_count
    word_cnt = word_count.get(word, 0)
    return word_cnt


@timer.log_time
def load_tfidf():
    global word_count
    global all_count

    f = open(FILE_PATH + 'mytfidf/word_count.txt', 'r', encoding='utf-8')

    line = f.readline()
    all_count = int(line.strip('\n').split('\t')[1])

    while 1:
        line = f.readline()
        if line:
            try:
                line = line.strip('\n')

                word, count = line.split('\t')

                if int(count) >= min_sum:
                    word_count[word] = int(count)
            except:
                traceback.print_exc()


        else:
            break

    # fw = open(FILE_PATH + 'qarank/word_count_out.txt', 'w', encoding='utf-8')
    # res = sorted(word_count.items(), key=itemgetter(1), reverse=True)
    #
    # for item in res:
    #     fw.write('{}\t{}\n'.format(item[0], item[1]))
    #
    # fw.close()
    f.close()


def get_tfidf(seq_line):
    if not seq_line:
        return None

    if not isinstance(seq_line, list):
        logging.error('use segment list request tf-idf')
        sys.exit(-1)

    global word_count
    global all_count

    if not word_count:
        load_tfidf()

    weights = []

    for word in seq_line:
        word_cnt = word_count.get(word)
        if not word_cnt:
            weights.append(0)
        else:
            weights.append(math.log(all_count / word_cnt))

    if not weights:
        return [0 for _ in weights]

    all = 0
    for weight in weights:
        all += weight
    if all <= 0:
        return [0 for _ in weights]

    res = [float('{:.3f}'.format(weight / all)) for weight in weights]
    # logging.info('{{{}}} tf-idf weight is: {{{}}}'.format(seq_line, res))

    return res


def get_max_words(seq_line):
    if not seq_line:
        return None

    if not isinstance(seq_line, list):
        logging.error('use segment str request get_max_word')
        sys.exit(-1)

    global word_count
    global all_count

    if not word_count:
        load_tfidf()

    weights = {}

    for word in seq_line:
        word_cnt = word_count.get(word)
        if not word_cnt:
            weights[word] = 0
        else:
            weights[word] = math.log(all_count / word_cnt)

    if not weights:
        return None

    sorted_tuple = sorted(weights.items(), key=itemgetter(1), reverse=True)
    sorted_word = [item[0] for item in sorted_tuple]
    # logging.info('{{{}}} sorted weight list is: {{{}}}'.format(seq_line, sorted_word))

    return sorted_word


def main():
    print("do sth")


if __name__ == '__main__':
    main()
