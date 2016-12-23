# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tieba = scrapy.Field()
    cat = scrapy.Field()
    slogan = scrapy.Field()
    follow_num = scrapy.Field()
    content_num = scrapy.Field()
    alias = scrapy.Field()



