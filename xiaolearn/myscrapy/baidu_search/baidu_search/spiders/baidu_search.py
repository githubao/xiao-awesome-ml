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
@file: baidu_search.py
@time: 2016/11/2 14:43
"""

import scrapy
from w3lib.html import remove_tags
from xiaolearn.util.settings import *
import re

SCRAPY_OUT_PATH = FILE_PATH + 'myscrapy/'
outfile = SCRAPY_OUT_PATH + 'content.txt'
with open(outfile,'w',encoding='utf-8'):
    pass

hanzi = re.compile('[\u4e00-\u9fff]+')

line = '我也没说你是地球的'


class BaiduSearchSpider(scrapy.Spider):
    name = 'baidu_search'
    allowed_domains = ['baidu.com']

    start_urls = [
        'https://www.baidu.com/s?wd=%s&pn=%s' %(line,i*10)  for i in range(0,10)
    ]

    def parse(self, response):
        # hrefs = response.selector.xpath('//div[contains(@class,"c-container")]/h3/a/@href').extract()
        containers = response.selector.xpath('//div[contains(@class,"c-container")]')
        for container in containers:
            href = container.xpath('h3/a/@href').extract()[0]
            title = remove_tags(container.xpath('h3/a').extract()[0])
            abstract = container.xpath('.//div[contains(@class,"c-abstract")]').extract()
            abstract = remove_tags(abstract[0]) if abstract else ''
            request = scrapy.Request(href, callback=self.parse_url)
            request.meta['title'] = title
            request.meta['abstract'] = abstract
            yield request

    def parse_url(self, response):
        d = {}
        d['url'] = response.url
        # content = remove_tags(response.selector.xpath('//body').extract()[0])
        content = hanzi.findall(response.text)
        d['content'] = ' '.join(content)
        d['title'] = response.meta['title']
        d['abstract'] = response.meta['abstract']
        d['content_len'] = len(content)

        with open(outfile, "a+", encoding='utf-8') as f:
            f.write('{}\n'.format(d))


            # def parse(self, response):
            #     filename = SCRAPY_OUT_PATH+'result.html'
            #     # with open(filename,'w',encoding='utf-8') as f:
            #     #     f.write(response.body)
            #     with open(filename,'wb') as f:
            #         f.write(response.body)


if __name__ == 'main':
    print('he')
