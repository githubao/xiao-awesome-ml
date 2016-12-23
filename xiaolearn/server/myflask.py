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
@file: myflask.py
@time: 2016/11/17 19:48
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'i am using flask'
    return open('C:\\Users\\BaoQiang\\Downloads\\201612-Python最佳编码实践.html',encoding='utf-8').read()

def main():
    app.run()


if __name__ == '__main__':
    main()

