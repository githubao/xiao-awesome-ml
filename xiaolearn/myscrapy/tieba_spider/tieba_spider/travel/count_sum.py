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
@file: count_sum.py
@time: 2016/11/14 10:40
"""

import os

files1 = [
    "/home/kongdeqian/conversation/original_conversation/3.23/conversation.3.23.txt",
    "/home/kongdeqian/conversation/original_conversation/3.24/conversation.3.24.txt",
    "/home/kongdeqian/conversation/original_conversation/3.25/conversation.3.25.txt",
    "/home/kongdeqian/conversation/original_conversation/3.27/conversation.3.27.txt",
    "/home/kongdeqian/conversation/original_conversation/3.28/conversation.3.28.txt",
    "/home/kongdeqian/conversation/original_conversation/4.1/conversation.4.1.txt",
    "/home/kongdeqian/conversation/original_conversation/4.11/conversation.4.11.txt",
    "/home/kongdeqian/conversation/original_conversation/4.15/conversation.4.15.txt",
    "/home/kongdeqian/conversation/original_conversation/4.21/conversation.4.21.txt",
    "/home/kongdeqian/conversation/original_conversation/4.23/conversation.4.23.txt",
    "/home/kongdeqian/conversation/original_conversation/4.5/conversation.4.5.txt"
]

files = [
    # 'C:\\Users\\BaoQiang\\Desktop\\test\\聊天\\1.txt',
    # 'C:\\Users\\BaoQiang\\Desktop\\test\\聊天\\2.txt',
    '/home/baoqiang/test/1/1.txt',
    '/home/baoqiang/test/2/2.txt',
]


def main():
    cnt = 0
    for file in files:
        res = os.system('wc -l {}'.format(file))

        cnt += int(res.split('\t')[0])


if __name__ == '__main__':
    main()
