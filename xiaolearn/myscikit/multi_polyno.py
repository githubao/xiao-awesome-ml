#!/usr/bin/env python
# encoding: utf-8

"""
@description: 多元多项式回归

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: multi_polyno.py
@time: 2016/11/29 20:31
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def ont_liner():
    plt.figure()
    plt.title('single variable')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis([30, 400, 100, 400])
    plt.grid(True)

    X = [[50], [100], [150], [200], [250], [300]]
    Y = [[150], [200], [250], [280], [310], [330]]

    X_test = [[250], [300]]
    Y_test = [[310], [330]]

    plt.plot(X, Y, 'k.')

    model = LinearRegression()
    model.fit(X, Y)
    x2 = [[30], [400]]
    y2 = model.predict(x2)

    plt.plot(x2, y2, 'g-')

    #     二项回归
    xx = np.linspace(30, 400, 100)
    quadratic_featurizer = PolynomialFeatures(degree=2)
    x_train_quadratic = quadratic_featurizer.fit_transform(X)
    xx_quadratic = quadratic_featurizer.transform(xx.reshape(xx.shape[0], 1))

    regressor_quadratic = LinearRegression()
    regressor_quadratic.fit(x_train_quadratic, Y)
    plt.plot(xx, regressor_quadratic.predict(xx_quadratic), 'r-')

    print('一元线性回归 r-squared {}'.format(model.score(X_test, Y_test)))
    X_test_quadratic = quadratic_featurizer.transform(X_test)
    print('二元线性回归 r-squared {}'.format(regressor_quadratic.score(X_test_quadratic, Y_test)))

    #   三次回归
    cubic_featurizer = PolynomialFeatures(degree=3)
    x_train_cubic = cubic_featurizer.fit_transform(X)
    xx_cubic = cubic_featurizer.transform(xx.reshape(xx.shape[0],1))

    regressor_cubic = LinearRegression()
    regressor_cubic.fit(x_train_cubic,Y)
    plt.plot(xx,regressor_cubic.predict(xx_cubic))

    X_test_cubic = cubic_featurizer.transform(X_test)
    print('三元线性回归 r-squared {}'.format(regressor_cubic.score(X_test_cubic,Y_test)))

    plt.show()


def main():
    ont_liner()


if __name__ == '__main__':
    main()
