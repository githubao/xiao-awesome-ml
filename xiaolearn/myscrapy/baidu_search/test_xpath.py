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
@file: test_xpath.py
@time: 2016/11/2 20:30
"""

from xiaolearn.util.settings import *
import re
from lxml import etree

SCRAPY_OUT_PATH = FILE_PATH + 'myscrapy/'
html_path = SCRAPY_OUT_PATH + 'result.html'

text = '''
    <div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li><a href="link5.html">fifth item</a>
     </ul>
 </div>
    '''


def main2():
    html = etree.HTML(text)

    # 打印所有节点
    # result = etree.tostring(html,pretty_print=True).decode()
    # print(result)

    # 所有的li节点
    # li = html.xpath('//li')
    # print(li)

    # 所有的span节点
    # spans = html.xpath('//span')
    # print([span.text for span in spans])

    #包含class的所有li标签的文本
    # data = html.xpath('//li/@class//text()')
    data = html.xpath('//li[@class]//text()')
    print(data)

def main():
    m = re.compile('[\u4e00-\u9fff]+')

    data = open(html_path, 'r', encoding='utf-8').read()

    res = m.findall(data)
    print(res)

    # selector = etree.HTML(data)
    # print(selector.xpath('//body/text()'))
    # print(selector.xpath('//*/text()'))


if __name__ == '__main__':
    # main()
    main2()
