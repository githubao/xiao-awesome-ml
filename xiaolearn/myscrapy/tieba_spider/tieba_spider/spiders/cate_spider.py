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
@file: cate_spider.py
@time: 2016/11/2 22:09
"""

import scrapy
from xiaolearn.myscrapy.tieba_spider.tieba_spider import items
from xiaolearn.util.settings import *
import json
import traceback
import re
import logging
import urllib.parse

logging.basicConfig(level=logging.INFO)
p = re.compile('kw=(.*)')


def parse_names():
    tieba_names = set()

    with open(FILE_PATH + '/tieba/test.txt', encoding='utf8') as f:
        line = f.readline()
        while line:
            if not line:
                return
            line = line.replace('\n', '')

            try:
                data = json.loads(line)
            except:
                logging.info('err parse data: {}'.format(data))
                traceback.print_exc()

            if not data:
                continue

            source = data['source']
            if source:
                tieba_names.add(source)

            line = f.readline()

    fw = open(FILE_PATH + '/tieba/tiebas.txt', 'a', encoding='utf8')
    for item in tieba_names:
        fw.write('{}\n'.format(item))
    fw.close()

    return tieba_names


class TiebaSpider(scrapy.Spider):
    name = 'tieba_spider'
    allowed_domains = ['tieba.baidu.com']

    # TIEBA_PATH = 'C:\\Users\\BaoQiang\\Desktop\\tiebas.txt'
    TIEBA_PATH = '/mnt/home/baoqiang/tiebas.txt'

    # TIEBA_NAMES = parse_names()
    # TIEBA_NAMES = ["摄影"]

    with open(TIEBA_PATH, encoding="utf8") as f:
        TIEBA_NAMES = f.readlines()
        TIEBA_NAMES = [item.strip() for item in TIEBA_NAMES]

    start_urls = [
        'http://tieba.baidu.com/f?kw=%s' % item for item in TIEBA_NAMES
        ]

    print(start_urls)

    def parse(self, response):
        item = items.TiebaSpiderItem()

        try:
            url = response._url
            m = p.search(url)
            if m:
                item['tieba'] = urllib.parse.unquote(m.group(1))
            else:
                item['tieba'] = None

            item["cat"] = response.selector.xpath(
                    '//*[@class="card_info"]//a/text()').extract()[0]
            slogon = response.selector.xpath(
                    '//*[@class="card_slogan"]/text()').extract()
            item["slogan"] = slogon[0] if slogon else ''
            alias = response.selector.xpath(
                    '//*[@class=" card_title_fname"]/text()').extract()[0].strip()
            if alias and len(alias) > 0:
                item["alias"] = alias[0:len(alias) - 1]
            else:
                item["alias"] = ""

            follow_num = response.selector.xpath(
                    '//*[@class="card_menNum"]/text()').extract()[0]
            content_num = response.selector.xpath(
                    '//*[@class="card_infoNum"]/text()').extract()[0]

            item["follow_num"] = int(follow_num.replace(',', ''))
            item["content_num"] = int(content_num.replace(',', ''))
        except:
            traceback.print_exc()
            return None

        # print(item)

        return item
