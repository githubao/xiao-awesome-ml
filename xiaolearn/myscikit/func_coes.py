#!/usr/bin/env python
# encoding: utf-8


"""
@description: 求解函数的系数 coefficient

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: func_coes.py
@time: 2016/12/16 13:16
"""

import numpy as np
from scipy.optimize import leastsq
import pylab as pl
from scipy.optimize import fsolve


def fitting_func(input_x, co_array):
    co_a, co_b, co_c = co_array
    return co_a * input_x * input_x + co_b * input_x + co_c


def residuals(co_array, input_x, input_y):
    return input_y - fitting_func(input_x, co_array)


def optimize():
    input_x = np.array([0, 1 / 2, 1])
    input_y = np.array([0, 2 / 5, 1])
    co_first = np.array([1, 1, 1])
    lst_result = leastsq(residuals, co_first, args=(input_x, input_y))
    print(lst_result[0])


def func(coes):
    a, b, c = coes

    return [c, a + b + c - 1, a + 2 * b + 4 * c - 1.6]


def solve():
    param = [1, 1, 1]
    result = fsolve(func, param)
    print(result)
    print(func(result))


def main():
    optimize()
    # solve()


if __name__ == '__main__':
    main()
