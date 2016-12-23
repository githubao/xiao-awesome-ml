#!/usr/bin/env python
# encoding: utf-8


"""
@description: 二分类问题

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: two_part.py
@time: 2016/11/4 23:01
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression

X = []
X.append("fuck you")
X.append("fuck you all")
X.append("hello everyone")

X.append("fuck me")
X.append("hello boy")

Y = [1, 1, 0]


def main():
    vectorizer = TfidfVectorizer()
    x_train = vectorizer.fit_transform(X[:-2])
    x_test = vectorizer.transform(X[-2:])

    classifier = LogisticRegression()
    classifier.fit(x_train, Y)

    predictions = classifier.predict(x_test)
    print(predictions)

if __name__ == '__main__':
    main()
