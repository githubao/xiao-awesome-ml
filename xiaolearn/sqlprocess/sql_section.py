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
@file: sql_section.py
@time: 2016/11/7 17:46
"""

import pymysql
from xiaolearn.myscrapy.tieba_spider.tieba_spider import settings
import logging

logging.basicConfig(level=logging.INFO)


class MySqlModule():
    _conn = None

    def __init__(self):
        self._conn = pymysql.connect(
                user=settings.MYSQL_USER,
                passwd=settings.MYSQL_PASSWORD,
                host=settings.MYSQL_HOST,
                db=settings.MYSQL_DB,
                charset='utf8'
        )

        # self._conn.autocommit(1)

    def insert(self, sql):
        # logging.debug('insert sql line: {}'.format(sql))
        # logging.info('insert sql line: {}'.format(sql))

        cur = self._conn.cursor()
        line = cur.execute(sql)
        return line

    def insertmany(self, sql,values):
        # logging.debug('insert sql line: {}'.format(sql))
        # logging.info('insert sql line: {}'.format(sql))
        cur = self._conn.cursor()
        line = cur.executemany(sql,values)
        return line

    def select(self, sql):
        cur = self._conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        return data

    def commit(self):
        self._conn.commit()

    def close(self):
        self._conn.close()
