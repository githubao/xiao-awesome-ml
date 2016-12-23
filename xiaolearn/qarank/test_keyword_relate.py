#!/usr/bin/env python
# encoding: utf-8

"""
@description: # 测试关键词相关度

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: test_keyword_relate.py
@time: 2016/12/21 15:56
"""

from xiaolearn.qarank.qa_relate import get_keyword_score
from xiaolearn.util.settings import MY_PATH


def score_qa():
    f = open(MY_PATH + 'qa.txt', 'r', encoding='utf-8')
    fw = open(MY_PATH + 'qa_out.txt', 'w', encoding='utf-8')
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        score = get_keyword_score(line)
        fw.write('{}\t{}\n'.format(line, score))

    f.close()
    fw.close()


def main():
    score_qa()


if __name__ == '__main__':
    main()
