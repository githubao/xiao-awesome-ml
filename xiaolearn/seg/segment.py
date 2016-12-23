#!/usr/bin/env python
# encoding: utf-8


"""
@description: //TODO 

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: segment.py
@time: 2016/10/31 23:26
"""
import logging

from jieba import cut
from jieba import posseg

logging.basicConfig(level=logging.INFO)


def seg(inp, outp):
    i = 0

    output = open(outp, 'w', encoding='utf-8')
    with open(inp, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            seg_list = cut(line)
            output.write(' '.join(seg_list))

            i += 1
            if i % 10000 == 0:
                logging.info('Convert {} lines'.format(i))

            line = f.readline()

    output.close()
    logging.info('Finished Convert {} lines'.format(i))


def get_seg_list(line):
    if not line:
        return None

    return list(cut(line))


def get_seg_post_list(line):
    if not line:
        return None

    seg_pos = posseg.cut(line)

    words = []
    poss = []

    for word, pos in seg_pos:
        words.append(word)
        poss.append(pos)
    return (words, poss)
