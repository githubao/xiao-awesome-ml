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
@file: train.py
@time: 2016/10/31 22:36
"""

import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec
from  gensim.models.word2vec import LineSentence


def main():
    program = os.path.basename(sys.argv[0])
    logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logging.info("running {}".format(' '.join(sys.argv)))

    if len(sys.argv) < 4:
        print(globals()['__doc__']) % locals()
        sys.exit(1)

    inp, outp1, outp2 = sys.argv[1:4]

    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())

    model.save(outp1)
    model.save_word2vec_format(outp2, binary=True)


if __name__ == '__main__':
    main()
