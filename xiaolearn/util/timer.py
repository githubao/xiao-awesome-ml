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
@file: timer.py
@time: 2016/11/1 14:21
"""

import time
import functools

import logging

def log_time(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        tick = time.time()
        logging.error('@{}， {{{}}} start'.format(time.strftime('%X',time.localtime()),func.__name__))
        res = func(*args,**kwargs)
        logging.error('@{}， {{{}}} end'.format(time.strftime('%X',time.localtime()),func.__name__))
        logging.error('@{:.3f}s， taken for {}'.format(time.time() - tick,func.__name__))

        return res

    return wrapper

