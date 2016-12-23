#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: dmoz_spider.py
@time: 2016/8/28 21:01
"""

import scrapy
from xiaoscrapydemo import items

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self, response):
        for href in response.css('ul.directory.dir-col > li > a::attr("href")'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = items.DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()

            yield item

    def parse_articles_follow_next_page(self,response):
        for article in response.xpath('//article'):
            # item = ArticleItem()
            item = items.DmozItem()
    #         do sth

            yield item

        next_page = response.css('url.navigation > li.next-page > a::attr("href")')
        if next_page:
            url =response.urljoin(next_page[0].extract())
            yield scrapy.Request(url,self.parse_articles_follow_next_page)

    def parse0(self, response):
        filename = response.url.split('/')[-2]+'.html'
        with open(filename,'wb') as f:
            f.write(response.body)

def main():
    print("do sth")


if __name__ == '__main__':
    main()

