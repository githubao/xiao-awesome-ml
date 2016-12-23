#!/usr/bin/env python
# encoding: utf-8

"""
@description: 测试tensorflow 是否安装成功

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: test_demo.py
@time: 2016/11/27 22:19
"""

import tensorflow as tf
import platform


def demo():
    print(platform.platform())

    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))
    a = tf.constant(10)
    b = tf.constant(32)
    print(sess.run(a + b))


if __name__ == '__main__':
    demo()
