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
@file: mysort.py
@time: 2016/11/17 19:30
"""

def quick_sort(array):
    less = []; greater = []
    if len(array) <= 1:
        return array
    pivot = array[0]
    for i,x in enumerate(array):
        if i == 0:
            continue

        less.append(x) if x <= pivot else greater.append(x)

    return quick_sort(less) +[pivot]+quick_sort(greater)



def main():
    a = [2,6,3,7,9,1,8,0,4,5]
    # a = [3,6,2]
    s = quick_sort(a)
    print(s)


if __name__ == '__main__':
    main()

