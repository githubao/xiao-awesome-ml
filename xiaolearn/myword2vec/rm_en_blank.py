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
@file: rm_en_blank.py
@time: 2016/10/31 22:31
"""

import logging
import os.path
import sys
import re

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

    with open(inp, 'r',encoding='utf-8') as f:
        line = f.readline()
        rule = re.compile(r'[ a-zA-Z]')

        while line:
            res = rule.sub('',line)
            output.write(res)

            i += 1
            if i % 10000 == 0:
                logging.info('Saved {} lines'.format(i))

            line = f.readline()

    output.close()
    logging.info('Finished Saved {} lines'.format(i))



if __name__ == '__main__':
    main()

