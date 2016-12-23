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
@file: tutorial_nltk.py
@time: 2016/11/2 10:34
"""

from mynltk.corpus import *
from pprint import pprint
from xiaolearn.util.settings import *
from mynltk.corpus import PlaintextCorpusReader

CORPUS_ROOT = FILE_PATH+'/nltk_corpus/'

def main():
    corpus = PlaintextCorpusReader(CORPUS_ROOT,'.*')
    print(corpus.fileids())
    # print(corpus.raw())
    print(corpus.words())
    print(corpus.sents())
    print(corpus.abspaths())
    print(corpus.categories())



if __name__ == '__main__':
    main()

