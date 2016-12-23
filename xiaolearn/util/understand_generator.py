#!/usr/bin/env python
# encoding: utf-8



"""
@description: 理解生成器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: understand_generator.py
@time: 2016/11/17 21:23
"""

from itertools import islice
import time

def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b


def gen():
    for i in range(1,5):
        print('i: {}'.format(i))
        yield i*i
        print('i+1: {}'.format(i+1))

if __name__ == '__main__':
    # l = list(islice(fib(),10))
    # print(l)

    res = gen()
    print(res)
    while res:
        print('start')
        print(res.__next__())
        print('end')

        time.sleep(0.2)
