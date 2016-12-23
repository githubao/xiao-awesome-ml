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
@file: settings.py
@time: 2016/11/1 18:17
"""

import logging
import platform
from os.path import dirname, abspath

ROOT_PATH = dirname(dirname(abspath(__file__))) + '/'
FILE_PATH = ROOT_PATH + 'file/'

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

MY_PATH = None

logger = None
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='myapp.log',
                    # filemode='a'
                    )


def get_logger():
    global logger
    if logger:
        return logger

    default_logger = 'default'
    logger = logging.getLogger(default_logger)
    logger.setLevel(logging.INFO)

    # handler = logging.StreamHandler()
    # formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    # # formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d]')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    # logger.addHandler(handler)

    return logger

def load_my_path():
    global MY_PATH

    plt = platform.platform()
    if 'Windows' in plt:
        MY_PATH = "C:\\Users\\BaoQiang\\Desktop\\"
    else:
        MY_PATH = '/mnt/home/baoqiang/'

if not MY_PATH:
    load_my_path()