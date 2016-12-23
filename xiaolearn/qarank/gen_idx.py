#!/usr/bin/env python
# encoding: utf-8

"""
@description: 根据关键词的权重，生成问题和答案的索引文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: gen_idx.py
@time: 2016/12/1 15:59
"""

from xiaolearn.util.settings import FILE_PATH
from xiaolearn.mytfidf.tfidf import get_tfidf, get_max_words
from xiaolearn.seg import segment
import hashlib
import os
import sys
import logging
from xiaolearn.qarank.preprocess import uniform_text

"""
索引文件在 /mnt/home/baoqiang/qa_index/
300W聊天数据对应的词向量文件在 filePath + /qarank/qa_relate/vector
"""

logging.basicConfig(level=logging.INFO)

ROOT_PATH = '/mnt/home/baoqiang/qa_index/'

VECTOR_FILE = FILE_PATH + 'qarank/qa_relate/vector.txt'
VECTORS_OUT_FILE = FILE_PATH + 'qarank/qa_relate/vector/{:02d}.txt'

MAX_WORDS_COUNT = 3


def idx_file():
    f = open(VECTOR_FILE, 'r', encoding='utf-8')
    outer = []
    for i in range(16):
        name = VECTORS_OUT_FILE.format(i)
        outer.append(open(name, 'w', encoding='utf-8'))

    while 1:
        line = f.readline()

        if line:
            line = line.strip('\n')

            items = line.split('\t')
            if len(items) != 5:
                continue

            q = items[1]

            q_seg = segment.get_seg_list(q)
            q_seg = uniform_text(q_seg)
            max_word_list = get_max_words(q_seg)

            logging.debug('line: {}'.format(line))
            logging.debug('max words: {}'.format(max_word_list))

            if not max_word_list:
                continue

            q_md5 = hashlib.md5(q.encode()).hexdigest()
            outer[int(q_md5[0],16)].write(line + '\n')

            for word in max_word_list:
                md5 = hashlib.md5(word.encode()).hexdigest()
                out_path = '{}/{}/{}'.format(ROOT_PATH, q_md5[0], md5[0])

                out_file = '{}/{}.txt'.format(out_path, md5)
                if not os.path.exists(out_path):
                    os.makedirs(out_path)
                    fw = open(out_file, 'w', encoding='utf-8')
                else:
                    fw = open(out_file, 'a', encoding='utf-8')

                fw.write(items[0] + '\n')
                fw.close()


        else:
            break

    for i in range(16):
        outer[i].close()


# def get_idx_path(max_word_list):
#     if not max_word_list:
#         return None
#
#     path = []
#     for idx, word in enumerate(max_word_list):
#         path.append(hashlib.md5(word.encode()).hexdigest())
#
#         if idx == MAX_WORDS_COUNT - 1:
#             break
#
#     out_path = '{}/{}'.format(ROOT_PATH, '/'.join(path))
#
#     return out_path


if __name__ == '__main__':
    idx_file()
