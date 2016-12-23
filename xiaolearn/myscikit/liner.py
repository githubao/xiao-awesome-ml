#!/usr/bin/env python
# encoding: utf-8


#
"""
@description:线性回归

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: liner.py
@time: 2016/11/23 20:19
"""
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def main():
    x1 = [[1],[2],[3],[4],[5],[6]]
    y1 = [[1],[2.1],[2.9],[4.2],[5.1],[5.8]]
    model = LinearRegression()
    model.fit(x1,y1)

    x2 = [[0],[2.5],[5.3],[9.1]]
    y2 = model.predict(x2)

    variance = np.var(x1,ddof=1)
    covariance =np.cov([item[0] for item in x1],[item[0] for item in y1])[0][1]
    score = model.score([1.0],[1.2])

    print("variance: {}, covariance: {}".format(variance,covariance))
    print("score: {}".format(score))

    plt.figure()
    plt.title('liner sample')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([0,10,0,10])
    plt.grid(True)
    plt.plot(x1,y1,'k.')
    plt.plot(x2,y2,'g-')
    plt.show()


if __name__ == '__main__':
    main()

