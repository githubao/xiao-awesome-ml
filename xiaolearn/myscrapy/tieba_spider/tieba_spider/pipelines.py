# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from datetime import datetime

from sqlprocess.sql_section import MySqlModule
from xiaolearn.util.settings import TIME_FORMAT


class TiebaSpiderPipeline(object):
    mysql = None

    def open_spider(self, spider):
        self.mysql = MySqlModule()

    def process_item(self, item, spider):
        self._process_insert(item)

    def close_spider(self, spider):
        self.mysql.close()

    def _process_insert(self, item):
        sql = 'insert into tieba_name({},{},{},{},{},{},{}) VALUES ("{}","{}","{}","{}","{}","{}","{}")'
        sql = sql.format('tieba',
                         'cat',
                         'slogan',
                         'alias',
                         'follow_num',
                         'content_num',
                         'time',
                         item['tieba'],
                         item['cat'],
                         item['slogan'],
                         item['alias'],
                         item['follow_num'],
                         item['content_num'],
                         datetime.now().strftime(TIME_FORMAT))

        line = self.mysql.insert(sql)
        self.mysql.commit()
        logging.info('insert {} line(s)'.format(line))
