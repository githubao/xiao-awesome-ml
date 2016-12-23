#!/usr/bin/env python
# encoding: utf-8

"""
@description: 把数据向量化，然后请求聚类

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: vectorizer_paragraph.py
@time: 2016/12/6 14:50
"""

from xiaolearn.seg.segment import get_seg_list
from xiaolearn.qarank.preprocess import uniform_text
from xiaolearn.simi.similarity import get_setence_vec
from xiaolearn.cluster.k_means import KMeans

from xiaolearn.util.settings import FILE_PATH
from xiaolearn.util.timer import log_time

TEST_FILE = FILE_PATH + 'cluster/test.txt'


def make_word_lists(paragraphs):
    return [get_seg_list(line) for line in paragraphs]
    # return [uniform_text(seq_line) for seq_line in seg_lists]


# def make_word_set(word_lists):
#     """ """
#     return set(word for words in word_lists for word in words)


def make_word_vectors(word_lists):
    def vectorize(seq_line):
        return get_setence_vec(seq=seq_line)

    return [vectorize(seq_line) for seq_line in word_lists]


def translator(clusters, paragraph_list):
    """Translate vectors back into paragraphs, to make them human-readable."""

    def item_translator(vector):
        for item in paragraph_list:
            if item[0] == str(vector):
                res = item[1]
                paragraph_list.remove(item)
                return res

    def cluster_translator(cluster):
        return list(map(item_translator, cluster))

    return list(map(cluster_translator, clusters))


# @log_time
def cluster_paragraphs(paragraphs, num_clusters=2):
    word_lists = make_word_lists(paragraphs)
    word_vectors = make_word_vectors(word_lists)

    paragraph_list = [(item0,item1) for item0,item1 in zip(map(str, word_vectors),paragraphs)]

    k_means = KMeans(num_clusters, word_vectors)
    k_means.main_loop()
    return translator(k_means.clusters, paragraph_list)


def test():
    f = open(TEST_FILE, 'r', encoding='utf-8')

    texts = f.readlines()
    texts = [line.strip() for line in texts]

    clusters = cluster_paragraphs(texts, num_clusters=10)

    for i, cluster in enumerate(clusters):
        print('cluster: {}'.format(i + 1))
        print('\n'.join(cluster))


def main():
    test()


if __name__ == '__main__':
    main()
