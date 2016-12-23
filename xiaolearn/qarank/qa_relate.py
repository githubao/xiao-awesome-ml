#!/usr/bin/env python
# encoding: utf-8

"""
@description: 问答相关度判断

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: qa_relate.py
@time: 2016/11/30 14:43
"""

import hashlib
import json
import math
import os
import sys
import traceback
from operator import itemgetter
from time import time

import numpy as np

from xiaolearn.qarank.gen_idx import ROOT_PATH
from xiaolearn.qarank.preprocess import uniform_text
from xiaolearn.seg import segment
from xiaolearn.seg.segment import *
from xiaolearn.simi.similarity import get_setence_vec, get_tfidf_vec, numpy_vec_distance
from xiaolearn.util.settings import FILE_PATH
from xiaolearn.util.timer import log_time

VECTOR_FILE = FILE_PATH + 'qarank/qa_relate/vector/{:02d}.txt'
OUT_PATH = FILE_PATH + 'qarank/qa_relate/out/{}/'

QA_VEC_MAP = {}

Q_THRESHOLD = 0.5
A_THRESHOLD = 0.6

MAX_KEYWORD_SCORE = 0.6
DEFAULT_RELATED_SCORE = 0.1

STOP_WORDS = {'说', 'Face', '、', '2', '元', 'QQ', '：', '个', '1', '！', '我', '好', '娱乐', '-', '在', '】', '呢', '是', '不', '。',
              '一', '要', '？', '.', '什么', '=', '就', ':', 'F', '你', '【', '3', '?', '的', '][', '那', '吧', '[', '了', '有', '啊',
              '="', '8', '，', '5', '给', '吗', ']', '他'}

REAL_POS = {'n', 'v', 'a', 'd'}


@log_time
def train(num):
    input_file = sys.argv[1]

    vector_file = VECTOR_FILE.format(num)
    out_file = '{}{:02d}.txt'.format(OUT_PATH, num)

    f = open(input_file, 'r', encoding="utf-8")
    fw = open(out_file, 'w', encoding="utf-8")

    global QA_VEC_MAP
    if not QA_VEC_MAP:
        load_train_data(vector_file)

    logging.info('load vector_file end: {}'.format(num))
    while 1:
        line = f.readline()

        cnt = 0
        if line:
            line = line.strip('\n')

            try:
                ranked_score = rank_qa(line, num)
            except:
                logging.error(line)
                traceback.print_exc()
                continue

            if ranked_score:
                for item in ranked_score:
                    single, score = item
                    fw.write('{}\t{}\t{:.5f}\n'.format(line, '\t'.join('%s' % item for item in single[:3]), score))

                    # 只取分值最高的一条就好了
                    break
            else:
                score = get_keyword_score(line)
                final_score = score if score > 0 else DEFAULT_RELATED_SCORE
                fw.write('{}\t{}\t{:.5f}\n'.format(line, '\t'.join('none' for _ in range(3)), final_score))

            cnt += 1

        else:
            break

        if cnt % 1000 == 0:
            logging.info('{} file,qa relate processing data: {}'.format(num, cnt))


# @log_time
def rank_qa(line, num):
    if not line:
        return None

    global QA_VEC_MAP

    line = line.strip('\n')
    (flag, q, a, state, *_) = line.split('\t')
    if '0' == state:
        logging.debug("{} state is 0".format(line))
        return None

        # 问题句子向量
    test_q_vec = get_setence_vec(q)

    # 索引数据
    q_seg, q_pos = segment.get_seg_post_list(q)
    # 归一化
    q_seg = uniform_text(q_seg)

    q_simi_idx = get_most_simi(q_seg, q_pos, num)
    if not q_simi_idx:
        logging.debug('no qa rank question was found'.format(line))
        return

    # 问题的相关度
    logging.info("{} simi question to cal".format(len(q_simi_idx)))
    q_list = []
    for idx in q_simi_idx:
        if not idx in QA_VEC_MAP:
            continue

        q_vec = QA_VEC_MAP[idx][3]
        score = vector_distance(test_q_vec, q_vec)
        if score >= Q_THRESHOLD:
            l = [idx, score]
            q_list.append(l)

    # 答案句子向量
    test_a_vec = get_setence_vec(a)
    if not q_list:
        logging.debug('{}, no qa rank question was found in train data'.format(q))

    # 答案的相关度
    a_list = []
    for item in q_list:
        (idx, q_score) = item
        a_vec = QA_VEC_MAP[idx][4]

        score = vector_distance(test_a_vec, a_vec)
        if score > A_THRESHOLD:
            l = [QA_VEC_MAP[idx], q_score * score]
            a_list.append(l)

    if not a_list:
        logging.debug('{}, no qa rank answer was found in train data'.format(a))

    rank = sorted(a_list, key=itemgetter(1), reverse=True)
    return rank


# 不同的线程取不同的交集索引的数据
# @log_time
# 如果大于10，索引文件的路径需要修改一下
def get_most_simi(seq, pos, num):
    if not seq:
        return []

    id_cnt = {}
    for word, pos in zip(seq, pos):
        if word in STOP_WORDS:
            continue

        if not pos in REAL_POS:
            continue

        md5 = hashlib.md5(word.encode()).hexdigest()
        path = '{}/{}/{}/{}.txt'.format(ROOT_PATH, hex(num).replace('0x', ''), md5[0], md5)

        if not os.path.exists(path):
            continue

        f = open(path, 'r', encoding='utf-8')
        lines = f.readlines()
        for idx in lines:
            idx = int(idx.strip('\n'))

            if idx in id_cnt:
                id_cnt[idx] += 1
            else:
                id_cnt[idx] = 1

        f.close()

    if not id_cnt:
        return []

    sorted_tuple = sorted(id_cnt.items(), key=itemgetter(1), reverse=True)
    if not sorted_tuple:
        return

    max_count = sorted_tuple[0][1]
    logging.debug("{} has {} simi words with {} item(s)".format(seq, max_count, len(sorted_tuple)))

    # 只有一个相同词语，而且句子超过1000个
    if max_count == 1 and len(sorted_tuple) > 1000:
        logging.info("question: {} simis is {}".format(q, [QA_VEC_MAP[idx][1] for idx in sorted_tuple]))

        logging.debug("{} only one simi word with {} item(s)".format(seq, len(sorted_tuple)))
        return

    sorted_filtered = filter(lambda x: x[1] >= max_count, sorted_tuple)

    return [item[0] for item in sorted_filtered]


@log_time
def load_train_data(vector_file):
    global QA_VEC_MAP

    f = open(vector_file, 'r', encoding='utf-8')
    lines = f.readlines()

    for line in lines:
        line = line.strip('\n')

        items = line.split('\t')
        single = [items[0], items[1], items[2], json.loads(items[3]), json.loads(items[4])]

        QA_VEC_MAP[int(items[0])] = single

    f.close()


# def sentence2vec():
#     f = open(QUES_FILE, 'r', encoding='utf-8')
#     fw = open(VECTOR_FILE, 'w', encoding='utf-8')
#
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip('\n')
#
#         (flag, ques, ans) = line.split('\t')
#         ques_vec = get_seq_vec(ques)
#         ans_vec = get_seq_vec(ans)
#
#         if ques_vec is not None and ans_vec is not None:
#             fw.write('{}\t{}\t{}\n'.format(line, list(ques_vec), list(ans_vec)))
#
#     f.close()
#     fw.close()


def vector_sqrtlen(vector):
    len = 0
    for item in vector:
        len += item * item

    len = math.sqrt(len)
    return len


# @log_time
def vector_distance(v1, v2):
    if not v1 or not v2:
        return 0

    if len(v1) != len(v2):
        logging.error('{} and {} length not equal'.format(v1, v2))
        return 0

    sqrt_vec1 = vector_sqrtlen(v1)
    sqrt_vec2 = vector_sqrtlen(v2)
    value = 0

    if not sqrt_vec1 or not sqrt_vec2:
        return 0

    for item1, item2 in zip(v1, v2):
        value += item1 * item2

    return value / (sqrt_vec1 * sqrt_vec2)


def merge_file():
    out_file = sys.argv[2]

    score_dic = {}
    for file_name in os.listdir(OUT_PATH):
        full_path = os.path.join(OUT_PATH, file_name)
        with open(full_path, 'r', encoding='utf-8') as f:
            while 1:
                line = f.readline()
                if not line:
                    break

                line = line.strip('\n')
                if not line:
                    continue

                uid, *_, score = line.split('\t')
                if uid not in score_dic:
                    score_dic[uid] = line
                else:
                    origin_line = score_dic.get(uid)
                    *_, origin_score = origin_line.split('\t')
                    if score > origin_score:
                        score_dic[uid] = line

    fw = open(out_file, 'w', encoding='utf-8')
    for value in score_dic.values():
        fw.write('{}\n'.format(value))

    fw.close()


# 如果说相关度判断没有结果，使用关键词实现实现的分值判断
def get_keyword_score(line):
    line = line.strip('\n')
    (flag, q, a, state, *_) = line.split('\t')
    if '0' == state:
        logging.debug("{} state is 0".format(line))
        return 0

    q_tf_vec = get_tfidf_vec(q)
    a_tf_vec = get_tfidf_vec(a)

    if not q_tf_vec or not a_tf_vec:
        return 0

    weight_sum = 0
    word_sum = 0
    score_sum = 0.0

    sentence_len = len(q_tf_vec)

    for item in q_tf_vec:
        weight = item[0]
        q_vec = np.array(item[1]).reshape(1, -1)

        most_simi = max(numpy_vec_distance(q_vec, np.array(a_item[1]).reshape(-1, 1)) for a_item in a_tf_vec)

        if most_simi >= 0.8:
            score_sum += weight * most_simi

        word_sum += 1
        weight_sum += weight

        if word_sum >= 5 or weight_sum > 0.75:
            break

    # 根据词语长度，那么这句话一般很长，粗暴一点做*2加权处理
    final_score = MAX_KEYWORD_SCORE * score_sum * double_sentence(sentence_len)

    return final_score if final_score <= MAX_KEYWORD_SCORE else MAX_KEYWORD_SCORE


def double_sentence(length):
    if 5 < length <= 15:
        return 2
    return 1


def test():
    # s = '你还认识我的妹妹呀'
    # s = segment.get_seg_list(s)
    # print(get_most_simi(s))
    # vector_distance([0, 0, 0], [0, 0, 0])
    pass


def generate_outpath():
    global OUT_PATH
    OUT_PATH = OUT_PATH.format(int(time()))
    if os.path.exists(OUT_PATH):
        logging.error('{} file path exists, exit'.format(OUT_PATH))
        sys.exit(-1)
    else:
        os.mkdir(OUT_PATH)


def main():
    # sentence2vec()
    global QA_VEC_MAP

    generate_outpath()

    for i in range(0, 16):
        QA_VEC_MAP.clear()
        train(i)

    # 合并文件
    merge_file()


if __name__ == '__main__':
    main()
