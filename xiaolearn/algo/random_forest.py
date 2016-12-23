#!/usr/bin/env python
# encoding: utf-8


"""
@description: 随机森林的demo实现

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: random_forest.py
@time: 2016/11/23 18:17
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np


def demo():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.75
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    df.head()

    train, test = df[df['is_train'] == True], df[df['is_train'] == False]

    features = df.columns[:4]
    clf = RandomForestClassifier(n_jobs=2)
    y, _ = pd.factorize(train['species'])
    clf.fit(train[features], y)

    preds = iris.target_names[clf.predict(test[features])]
    res = pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])
    print(res)


def main():
    demo()


if __name__ == '__main__':
    main()
