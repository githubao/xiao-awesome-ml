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
@file: tra2sim.py
@time: 2016/10/31 23:26
"""
import opencc
import sys
import logging
import os.path


def main():
    cc = opencc.OpenCC('t2s')

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

    output = open(outp, 'w', encoding='utf-8')
    with open(inp, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            output.write(cc.convert(line))

            i += 1
            if i % 10000 == 0:
                logging.info('Convert {} lines'.format(i))

            line = f.readline()

    output.close()
    logging.info('Finished Convert {} lines'.format(i))


def tmp():
    inp, outp = sys.argv[1:3]
    space = " "
    i = 0

    output = open(outp, 'w', encoding='utf-8')
    with open(inp, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            if not '\n' == line:
                output.write(line)

            i += 1
            if i % 10000 == 0:
                logging.info('Convert {} lines'.format(i))

            line = f.readline()

    output.close()
    logging.info('Finished Saved {} articles'.format(i))


if __name__ == '__main__':
    # main()
    tmp()
