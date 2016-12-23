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
@file: read_csv.py
@time: 2016/11/9 11:24
"""

import pandas as pd


def main():
    data = pd.read_csv('C:/Users/BaoQiang/Downloads/week.csv')
    print(data)


if __name__ == '__main__':
    main()
