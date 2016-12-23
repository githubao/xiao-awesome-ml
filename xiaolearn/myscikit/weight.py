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
@file: weight.py
@time: 2016/11/1 17:49
"""

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from xiaolearn.util.settings import *
from xiaolearn.seg import segment
import json

file_path = ROOT_PATH + 'file/ques.txt'
seg_path = ROOT_PATH + 'file/ques_seg.txt'
out_path = ROOT_PATH + 'file/ques_out.txt'


def train():
    # corpus = [
    #     "我 来到 北京 清华大学",
    #     "他 来到 了 网易 杭研 大厦",
    #     "小明 硕士 毕业 与 中国 科学院",
    #     "我 爱 北京 天安门"
    # ]
    # 文件不存在，才切词
    if not os.path.isfile(seg_path):
        segment.seg(file_path, seg_path)

    fw = open(out_path, 'w', encoding='utf-8')

    with open(seg_path, 'r', encoding='utf-8') as f:
        corpus = f.readlines()

    vec = CountVectorizer()
    trans = TfidfTransformer()
    tf_idf = trans.fit_transform(vec.fit_transform(corpus))
    word = vec.get_feature_names()
    # weight = tf_idf.toarray()
    # for i in range(len(weight)):
    #     uni = uniform(word, weight[i])
    #     print(uni)

    # 取系数矩阵的行列
    # for i in range(tf_idf.shape[0]):
    #     uni = uniform(word,tf_idf[i,:][0].toarray()[0])
    #     print(uni)

    # 取系数矩阵的行列
    for line, row in zip(corpus, range(tf_idf.shape[0])):
        line = line.replace("\n",'').replace(' ',"")
        uni = uniform(word, tf_idf[row, :][0].toarray()[0])
        fw.write(line + '\t' + str(uni) + '\n')

        if row % 1000 == 0:
            print('processing [{}] items'.format(row))

    fw.close()

def uniform(word, weight):
    sum = 0.0
    for w in weight:
        sum += w

    l = []
    for x, y in zip(word, weight):
        if y:
            d = {}
            d['word'] = x
            d['weight'] = round(float(y / sum), 3)
            l.append(d)

    #按照大小排序
    l = sorted(l,key=lambda x:x['weight'],reverse = True)

    return l


if __name__ == '__main__':
    train()
