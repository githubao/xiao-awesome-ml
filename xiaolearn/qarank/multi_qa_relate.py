#!/usr/bin/env python
# encoding: utf-8

"""
@description: 分布式执行计算

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: multi_qa_relate.py
@time: 2016/12/1 14:25
"""
from xiaolearn.util.settings import FILE_PATH
from xiaolearn.qarank import qa_relate
from xiaolearn.util.timer import log_time
import threading

VECTOR_FILE = FILE_PATH + 'qarank/qa_relate/vector.txt'
OUT_FILE = FILE_PATH + 'qarank/qa_relate/vector/{:03d}.txt'

MAX_LINE = 100000


# MAX_LINE = 10


class MultiRelate(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        qa_relate.train(self.num)


@log_time
def multi_related():
    threads = []

    for i in range(4):

        for j in range(4):
            threads.append(MultiRelate(i * 4 + j))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


def split_file():
    cnt = 0
    file_cnt = 1

    f = open(VECTOR_FILE, 'r', encoding='utf-8')
    fw = open(OUT_FILE.format(file_cnt), 'w', encoding='utf-8')

    while 1:
        line = f.readline()

        if line:
            fw.write(line)
            cnt += 1

            if cnt >= MAX_LINE:
                fw.close()

                file_cnt += 1
                cnt = 0

                fw = open(OUT_FILE.format(file_cnt), 'w', encoding='utf-8')
        else:
            break


if __name__ == '__main__':
    multi_related()
