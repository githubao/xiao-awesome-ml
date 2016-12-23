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
@file: merge_same.py
@time: 2016/11/13 20:23
"""

from collections import Counter


def main():
    f_in = open("C:\\Users\\BaoQiang\\Desktop\\chat.txt", 'r', encoding="utf-8")
    f_out = open("C:\\Users\\BaoQiang\\Desktop\\chat_out.txt", 'w', encoding="utf-8")

    lines = f_in.readlines()

    mul_set = set()

    single_chat = ''
    # for line in lines:
    #     if 'http://tieba.baidu.com' in line:
    #         continue
    #     elif '*' * 50 in line:
    #         if single_chat  in all_set:
    #             mul_set.add(single_chat)
    #         else:
    #             all_set.add(single_chat)
    #
    #         single_chat = ''
    #     else:
    #         single_chat += line

    for line in lines:
        if 'http://tieba.baidu.com' in line:
            if single_chat not in mul_set:
                f_out.write(single_chat)
                f_out.write(line)
                f_out.write('{}\n'.format('*' * 50))

                mul_set.add(single_chat)
        elif '*' * 50 in line:
            single_chat = ''
        else:
            single_chat += line

    f_in.close()
    f_out.close()


if __name__ == '__main__':
    main()
