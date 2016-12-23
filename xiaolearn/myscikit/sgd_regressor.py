#!/usr/bin/env python
# encoding: utf-8

"""
@description: 随机梯度下降 线性拟合

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sgd_regressor.py
@time: 2016/11/29 20:59
"""

import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler


def sgd_predict():
    plt.figure('single variable')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    x_scaler = StandardScaler()
    y_scaler = StandardScaler()

    X = [[50], [100], [150], [200], [250], [300]]
    y = [[150], [200], [250], [280], [310], [330]]

    X = X * 10
    y = y * 10

    X = x_scaler.fit_transform(X)
    y = y_scaler.fit_transform(y)

    X_test = [[40], [400]]
    X_test = x_scaler.transform(X_test)

    plt.plot(X, y, 'k.')

    model = SGDRegressor()
    model.fit(X, y.ravel())

    y_result = model.predict(X_test)
    plt.plot(X_test, y_result, 'g-')

    plt.show()


def main():
    sgd_predict()


if __name__ == '__main__':
    main()
