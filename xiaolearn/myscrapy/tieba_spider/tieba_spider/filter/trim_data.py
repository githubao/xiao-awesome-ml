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
@file: trim_data.py
@time: 2016/11/7 17:28
"""

import logging

from xiaolearn.myscrapy.tieba_spider.tieba_spider.filter.filter_module import FilterModule
from xiaolearn.util import settings
import traceback

logging.basicConfig(level=logging.INFO)

FILE_NAME = 'test'
FILE_PATH = settings.FILE_PATH + 'tieba/test.txt'

ERR_PATH = settings.FILE_PATH + 'tieba/err.txt'
fw = open(ERR_PATH, 'a', encoding='utf-8')


def main():
    f = open(FILE_PATH, 'r', encoding='utf-8')
    cnt = 0
    line = f.readline()

    while line:
        cnt += 1
        try:
            module = FilterModule(FILE_NAME,cnt)
            module.process_data(line)
            module.format_sql()
            module.save_sql()
            # module.print_sql()
        except:
            traceback.print_exc()
            fw.write(line)
            fw.flush()

        line = f.readline()

        if cnt % 1000 == 0:
            logging.info('processing data: {}'.format(cnt))

    logging.info('total process data: {}'.format(cnt))
    f.close()
    fw.close()


if __name__ == '__main__':
    main()
