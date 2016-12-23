#!/usr/bin/env python
# encoding: utf-8


"""
@description:

@version: 1.0
@author: BaoQiang
@license: Apache Licence
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: myrequest.py
@time: 2016/11/17 20:03
"""
import requests


def main():
    r = requests.get(
        "https://api.github.com",
        auth=(
            'mailbaoqiang@gmail.com',
            '******'))

    print(r.status_code)
    print(r.headers['content-type'])

if __name__ == '__main__':
    main()
