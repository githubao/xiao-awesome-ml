#!/usr/bin/env python
# encoding: utf-8

"""
@description: 生成 “所有关于我的” json

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: about_me.py
@time: 2016/11/25 18:25
"""

import json
import configparser
import re
from copy import deepcopy
import pprint

def main():
    path = "D:\\000\\data.cfg"
    out_path = "D:\\000\\data_out.txt"
    reg = '\[(.*)\]'

    with open(path,encoding='utf-8') as f:
        topic = ''
        sub = []
        d = {}

        lines = f.readlines()

        for line in lines:
            line = line.strip('\n')

            if line.startswith('['):
                if topic and sub:
                    d[topic]=deepcopy(sub)

                    sub = []

                m = re.match(reg,line)
                topic = m.group(1)
            else:
                sub.append(line)

        if topic and sub:
            d[topic]=deepcopy(sub)

        j = json.dumps(d,ensure_ascii=False)

        fw = open(out_path,'w',encoding="utf-8")
        json.dump(d,fw,ensure_ascii=False)
        fw.close()

        pprint.pprint(j)


if __name__ == '__main__':
    main()

