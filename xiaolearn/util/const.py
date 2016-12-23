#!/usr/bin/env python
# encoding: utf-8


"""
@description: const 类

@version: 1.0
@author: BaoQiang
@license: Apache Licence
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: const.py
@time: 2016/11/17 20:58
"""


class _const:

    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError('Can\'t change const: {}'.format(key))
        if not key.isupper():
            raise self.ConstCaseError(
                'const name "{}" is not all upper case'.format(key))

        self.__dict__[key] = value


import sys

sys.modules[__name__] = _const()
