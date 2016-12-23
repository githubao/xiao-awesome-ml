#!/usr/bin/env python
# encoding: utf-8

"""
@description: 网格搜索

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: grid_search.py
@time: 2016/11/29 21:45
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

X = ['fuck you', 'fuck you all', 'hello everyone', 'fuck me', 'hello boy']
y = [1, 0, 1, 0, 1]


def search():
    global X,y

    X = X * 5
    y = y * 5

    pipeline = Pipeline([
        ('vec', TfidfVectorizer(stop_words='english')),
        ('clf', LogisticRegression())
    ])

    parameters = {
        'vec__max_features': (3, 5),
    }

    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1, scoring='accuracy', cv=3)
    grid_search.fit(X, y)

    print('最佳效果： {:0.3f}'.format(grid_search.best_score_))
    print('最优参数组合： ')
    best_parameters = grid_search.best_estimator_.get_params()

    for param_name in sorted(parameters.keys()):
        print('\t{}: {}'.format(param_name, best_parameters[param_name]))


def main():
    search()


if __name__ == '__main__':
    main()
