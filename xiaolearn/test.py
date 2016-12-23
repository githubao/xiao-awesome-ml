#!/usr/bin/env python
# encoding: utf-8

"""
@description: 测试java调用Python

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: test.py
@time: 2016/12/16 16:26
"""

import os
import sys
from xiaolearn.util.settings import MY_PATH


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print(list(fib(10)))

def main():
    pass

if __name__ == '__main__':
    main()
