#!/usr/bin/env python
# encoding: utf-8


"""
@description: 多元线性回归

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: muti_liner.py
@time: 2016/11/23 20:40
"""

from numpy.linalg import inv,lstsq
from numpy import dot,transpose
from sklearn.linear_model import LinearRegression

def main():
    x = [[1,1,1],[1,1,2],[1,2,1]]
    y = [[6],[9],[8]]

    print(dot(inv(dot(transpose(x),x)), dot(transpose(x),y)))

    print(lstsq(x,y)[0])

    model = LinearRegression()
    model.fit(x,y)
    x2 = [[1,3,5]]
    y2 = model.predict(x2)
    print(y2)

if __name__ == '__main__':
    main()

