#!/usr/bin/env python
# encoding: utf-8

"""
@description: pythonic code

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: pythonic_code.py
@time: 2016/12/22 20:16
"""
from collections import Counter


class ReversedCompare():
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return other.value.__gt__(self.value)

def check_is_admin(func):
    def wrapper(*args,**kwargs):
        (self,*_) = args
        if not isinstance(self,User):
            raise TypeError('sorry, only User instance is allowed to use this func')
        if self.username is not 'admin':
            raise ValueError('sorry, your are not allowed to do so')
        return func(*args,**kwargs)
    return wrapper

class User():
    def __init__(self,username):
        self.username = username

    @check_is_admin
    def get_password(self):
        return 'secret'

@check_is_admin
def get_password(username='default'):
    return 'secret'

def test_user():
    admin = User('admin')
    someone = User('someone')

    print(admin.get_password())
    print(someone.get_password())

def test_auth():
    print(get_password('admin'))
    # print(get_password('someone'))

def test_compare():
    one = ReversedCompare(1)
    two = ReversedCompare(2)
    print(one > two)

# 多次打印
def multi_printer():
    words = ['i', 'love', 'you']
    times = [1, 2, 3]
    for c, w in zip(times, words):
        print(c * w, end=' ')  # i lovelove youyouyou

# 多次打印
def multi_printer():
    words = ['i', 'love', 'you']
    times = [1, 2, 3]
    for c, w in zip(times, words):
        print(c * w, end=' ')  # i lovelove youyouyou

# 计数器
def test_counter():
    from collections import Counter
    nums = [4,2,6,7,5,9,0,6,2,6,7]
    counter = Counter(nums)
    print(counter)  # Counter({6: 3, 2: 2, 7: 2, 0: 1, 4: 1, 5: 1, 9: 1})


users = [
{'first_name': 'a', 'last_name': 'd', 'uid': 1},
{'first_name': 'b', 'last_name': 'a', 'uid': 4},
{'first_name': 'D', 'last_name': 'C', 'uid': 2},
{'first_name': 'c', 'last_name': 'b', 'uid': 3}
]

# 按照字段排序
def sort_by_field():
    from operator import itemgetter
    rows_by_first_name = sorted(users, key=itemgetter('first_name'))
    rows_by_last_name_nocase = sorted(users, key=lambda x: x['last_name'].lower(), reverse=True)
    print([item['first_name'] for item in rows_by_first_name])  # ['D', 'a', 'b', 'c']
    print([item['last_name'] for item in rows_by_last_name_nocase]) # ['d', 'C', 'b', 'a']


def main():
    # test_compare()
    # test_user()
    # test_auth()
    multi_printer()
    test_counter()
    sort_by_field()


if __name__ == '__main__':
    main()
