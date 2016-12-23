#!/usr/bin/env python
# encoding: utf-8

"""
@description: 统计元音个数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: vowel_counter.py
@time: 2016/12/22 20:09
"""


def count_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    def vowel_counter(letter):
        return 1 if letter in vowels else 0

    def word_counter(word):
        return sum(map(vowel_counter, word))

    return map(word_counter, words)


def test_count_vowels():
    words = ['find', 'hello', 'world']
    print(list(count_vowels(words)))  # [1, 2, 1]


def main():
    test_count_vowels()


if __name__ == '__main__':
    main()
