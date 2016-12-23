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
@file: parse_wiki.py.py
@time: 2016/10/31 22:18
"""

import logging
import os.path
import sys
from gensim.corpora import WikiCorpus


def main():
    program = os.path.basename(sys.argv[0])
    logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logging.info("running {}".format(' '.join(sys.argv)))

    if len(sys.argv) < 3:
        print(globals()['__doc__']) % locals()
        sys.exit(1)

    inp, outp = sys.argv[1:3]
    space = " "
    i = 0

    output = open(outp, 'w',encoding='utf-8')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(space.join([ item.decode("utf-8") for item in text]) + '\n')
        i += 1
        if i % 10000 == 0:
            logging.info('Saved {} articles'.format(i))

    output.close()
    logging.info('Finished Saved {} articles'.format(i))


if __name__ == '__main__':
    main()
