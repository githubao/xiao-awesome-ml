#!/usr/bin/env python
# encoding: utf-8

"""
@description: sqlite的接口

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: mysqlite.py
@time: 2016/12/7 13:56
"""

import sqlite3

from xiaolearn.util.settings import FILE_PATH

__all__ = [
    'get_sql'
]


class SqlLite():
    def __init__(self, input_file):
        self.conn = sqlite3.connect(input_file)

    def get_sql(self, sql):
        cur = self.conn.cursor()

        cur.execute(sql)
        data = cur.fetchall()
        return data

    def close(self):
        self.conn.close()


def hello():
    sql = "select name from sqlite_master where type = 'table' order by name"
    tables = "[('comment',), ('forum',), ('post',), ('thread',), ('user',)]"

    s = "[('comment', 'CREATE TABLE comment (\n\tid INTEGER NOT NULL, \n\tpid INTEGER, \n\tauthor VARCHAR(64), \n\tcontent TEXT, \n\ttime TIMESTAMP, \n\treply VARCHAR(64), \n\tupdate_time TIMESTAMP, \n\tPRIMARY KEY (id)\n)')]"
    # sql = 'select * from comment limit 10'


if __name__ == '__main__':
    hello()
