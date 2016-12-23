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
@file: category_spider.py
@time: 2016/11/11 13:30
"""

import scrapy
import re
from xiaolearn.util.settings import FILE_PATH

fw = open(FILE_PATH + 'tieba/cate.txt', 'w', encoding='utf-8')

ROOT_PATH = 'http://tieba.baidu.com'


class CategorySpider(scrapy.Spider):
    name = "tieba_category"

    allowed_domains = ["tieba.baidu.com"]
    start_urls = ['http://tieba.baidu.com/f/fdir?fd=生活&sd=休闲活动']

    def parse(self, response):
        for name in response.selector.xpath('//*[@class="root_dir_box"]//a/@href'):
            full_url = response.urljoin(ROOT_PATH + name.extract())
            yield scrapy.Request(url=full_url, callback=self.parseItem)

    def parseItem(self, response):
        start_page = response.selector.xpath('//*[@class="pagination"]//a/@href').extract()
        if not start_page or len(start_page) == 0:
            yield None

        for i in range(1, 100):
            url = re.sub('pn=\d', 'pn=%d' % i, start_page[0])
            full_url = ROOT_PATH + url
            yield scrapy.Request(url=full_url, callback=self.parsePage)

    def parsePage(self, response):
        for name in response.selector.xpath('//*[@class="sub_dir_box"]//a/text()'):
            fw.write('{}\n'.format(name.extract()))
            fw.flush()

    def close_spider(self):
        fw.close()
