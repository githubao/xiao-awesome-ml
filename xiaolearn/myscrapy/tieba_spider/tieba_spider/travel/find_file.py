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
@file: find_file.py
@time: 2016/11/10 22:46
"""

import os
import json
import time

# ROOT_PATH = '/home/kongdeqian/conversation/original_conversation'
# OUT_PATH = '/home/qiumowu/out.txt'
ROOT_PATH = 'C:\\Users\\BaoQiang\\Desktop\\test'
OUT_PATH = '/mnt/baoqiang/out.txt'
SHENGHUO1 = '生活吧'
SHENGHUO2 = '生活'

fw = open(OUT_PATH, 'w', encoding='utf-8')


def travel():
    print('start')
    for parent, dirnames, _ in os.walk(ROOT_PATH):
        print('dirnames: {}'.format(dirnames))
        for dir in dirnames:
            print('dir: {}'.format(dir))
            for _, _, filenames in os.walk(parent + '/' + dir):
                print('filenames: {}'.format(filenames))
                for file in filenames:
                    print('file: {}'.format(file))
                    print('process [{}] file'.format(file))
                    cnt = 0
                    if file.endswith('txt') and 'processed' not in file:
                        f = open(parent + '/' + dir + '/' + file, 'r', encoding='utf-8')
                        line = f.readline()
                        while line:
                            # print(line)

                            try:

                                data = json.loads(line)
                                source = data["source"]
                                if SHENGHUO1 == source or SHENGHUO2 == source:
                                    fw.write(line)
                                    fw.flush()
                            except:
                                pass

                            while not line:
                                try:
                                    line = f.readline()

                                except:
                                    line = ''

                            cnt += 1

                            if cnt % 10000 == 0:
                                print('processed {} data'.format(cnt))

                        f.close()

                    print('[{}] end'.format(file))
                print('[{}] end'.format(filenames))
            print('[{}] end'.format(dir))
        print('[{}] end'.format(dirnames))

    fw.close()


def test():
    start = time.time()
    f = open('C:\\Users\\BaoQiang\\Desktop\\test.txt', encoding='utf-8')

    cnt = 0
    for i in range(0, 1000000):
        line = f.readline()

        if not line:
            f.seek(0)
            line = f.readline()

        cnt += 1
        if cnt % 10000 == 0:
            print(cnt)
            print(line)

        data = json.loads(line)
        source = data["source"]
        if SHENGHUO1 == source or SHENGHUO2 == source:
            fw.write(line)
            fw.flush()

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    test()
    # travel()
