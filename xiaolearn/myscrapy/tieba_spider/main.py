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
@file: main.py
@time: 2016/11/2 20:00
"""

from scrapy import cmdline

def main():
    cmdline.execute('scrapy crawl tieba_spider -L INFO'.split())


if __name__ == '__main__':
    main()

