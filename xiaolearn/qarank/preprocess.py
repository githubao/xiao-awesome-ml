#!/usr/bin/env python
# encoding: utf-8

"""
@description: 数据预处理

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: preprocess.py
@time: 2016/12/6 14:23
"""

import re


def not_empty(s):
    return s and s.strip()


def rm_line_punc(line):
    return re.sub('[,.?";:\-!@#$%^&*()，。？‘’“”：！ ]', '', line)


def rm_punc(text_vector):
    """Removes special characters from text."""
    no_punc_list = [re.sub('[,.?";:\-!@#$%^&*()，。？‘’“”：！ ]', '', word) for word in text_vector]
    return list(filter(not_empty, no_punc_list))


def uniform_text(text_vector):
    """Takes in text, processes it, and vectorizes it."""

    def remove_common_words(text_vector):
        """Removes 50 most common words in the uk english.

        source: http://www.bckelk.ukfsn.org/words/uk1000n.html

        """
        # common_words = {'the', 'and', 'to', 'of', 'a', 'I', 'in', 'was', 'he', 'that', 'it', 'his', 'her', 'you', 'as',
        #                 'had', 'with', 'for', 'she', 'not', 'at', 'but', 'be', 'my', 'on', 'have', 'him', 'is', 'said',
        #                 'me', 'which', 'by', 'so', 'this', 'all', 'from', 'they', 'no', 'were', 'if', 'would', 'or',
        #                 'when', 'what', 'there', 'been', 'one', 'could', 'very', 'an', 'who'}

        common_words = {'的', '了'}

        return [word for word in text_vector if word not in common_words]

    lower_text = [word.lower() for word in text_vector]
    no_punc_text = rm_punc(lower_text)
    words_list = remove_common_words(no_punc_text)

    return words_list
