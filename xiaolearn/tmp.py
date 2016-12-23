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
@file: tmp.py
@time: 2016/11/1 18:28
"""

import hashlib
import json
import os
import pprint
import re
import string
import sys
import time
from datetime import datetime
from urllib.parse import unquote

import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup
from scipy.sparse import csr_matrix

from xiaolearn.seg.segment import *
from xiaolearn.util.settings import FILE_PATH, get_logger

logger = get_logger()

def tmp():
    pass

def tmp33():
    t = [(1,20),(2,30)]
    for idx,cnt in t:
        print(idx)

def tmp32():
    # print(int(time.time()))
    s = '你好'
    print(s.encode('gbk').decode('utf-8'))


def tmp31():
    print('{}\t{}\t{}\n'.format(1, '\t'.join('none' for item in range(3)), 0))


def tmp30():
    x = np.linspace(0.01, 100, 100000)
    # y = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    # y = x
    y = np.log10(x)
    plt.figure()
    plt.grid(True)
    plt.plot(x, y, 'k.')
    plt.show()


def tmp29():
    plt.figure()
    plt.axis([-2, 2, -2, 2])
    plt.grid(True)
    plt.plot([1, -1], [1, -1], 'k.')
    plt.plot([1, -1], [-1, 1], 'r.')
    plt.show()


def tmp28():
    dic = {'a': 1, 'b': 3}
    kw_args(**dic)


def kw_args(**s):
    # for key,value in s.items():
    #     print(key,': ',value)
    print(s)


def tmp27():
    print(time.time())

    print(hex(11).replace('0x', ''))
    print(hex(9))


def tmp26():
    v1 = np.array([1, 2, 3]).reshape(1, -1)
    logger.info(v1)
    logging.info(v1)


def tmp25():
    l = [0, 0, 0]
    res = np.array(l).reshape(-1, 1)
    print(res)


def tmp24():
    s = {}
    s.clear()
    if s:
        print('ok')
    else:
        print('err')


def tmp23():
    s1 = '关键是我没钱'
    s2 = '你老板多少钱搞点钱的用用'

    s1 = '你喜欢他'
    s2 = '他真的漂亮的座位在你附近吗'

    s1 = '已占'

    print(get_seg_list(s1))
    print(get_seg_post_list(s2))


def tmp22():
    s = '你敢大声喊出你的女朋友的名字么'.encode()
    print(hashlib.md5(s).hexdigest())


def tmp21():
    lines = open("C:\\Users\\BaoQiang\\Desktop\\test.txt", encoding='utf-8')
    lines = {line.strip() for line in lines}
    print(repr(lines))


def tmp20():
    s = '[1,2]'
    print(list(json.loads(s)))
    # print(list(s))


def tmp19():
    body = {
        'word': '你'.encode('utf-8')
    }
    r = requests.post('http://127.0.0.1:5000/vec', data=body, timeout=5)
    response = json.loads(r.content.decode('unicode_escape').replace("'", '"'))
    print(response)


def tmp18():
    f = open("C:\\Users\\BaoQiang\\Desktop\\time.txt", encoding="utf-8")
    fw = open("C:\\Users\\BaoQiang\\Desktop\\time_out.txt", 'w', encoding="utf-8")
    lines = [line.strip('\n') for line in f.readlines()]

    for line in lines:
        l = line.split("time: ")
        if len(l) is not 2:
            print(l)
            continue

        fw.write('{}\t{}\n'.format(l[0], l[1]))

    fw.close()


def tmp17():
    s = [
        {'name': 'a', 'age': 1},
        {'name': 'b', 'age': 2},
        {'name': 'a', 'age': 3},
    ]

    print(sorted(s, key=lambda x: (x['name'], -x['age'])))


def tmp16():
    s = 'hello world'
    # print(s.split(' '))
    print(s.partition('eee'))

    s.expandtabs()

    print(string.whitespace)


def test(when=time.time):
    print(when())


def tmp15():
    test()
    time.sleep(1)
    test()


def tmp14():
    f = open("C:\\Users\\BaoQiang\\Desktop\\child_filter.properties", encoding="unicode_escape")
    line = f.read()
    # line = bytes(f.read()).decode("unicode_escape")
    # line = bytes(line,encoding='unicode_escape')

    print(line)

    # eval("1")
    # array.array(1, 2)


def tmp13():
    f = open("C:\\Users\\BaoQiang\\Desktop\\src.txt", encoding="utf-8")
    lines = f.readlines()
    l = []
    for line in lines:
        l.append(line.replace("\n", ""))

    f = open("C:\\Users\\BaoQiang\\Desktop\\test.txt", encoding="utf-8")
    fw = open("C:\\Users\\BaoQiang\\Desktop\\out.txt", 'w', encoding="utf-8")
    lines = f.readlines()
    l1 = []
    for line in lines:
        for i, s in enumerate(line.replace("\n", "")):
            if "1" == s:
                l1.append(l[i])

        fw.write('{}\n'.format(l1))
        l1.clear()

    fw.close()


def tmp12():
    soup = BeautifulSoup(open('C:\\Users\\BaoQiang\\Desktop\\1.html', encoding='utf-8'), 'lxml')
    texts = soup.select('li')
    for i in texts:
        print(i.text)


def tmp11():
    s = '{"author":"q939864646","comments":[{"author":"720杰然不同","content":"...你楼下是我","type":0},{"author":"q939864646","content":"回复 720杰然不同 :","type":0},{"author":"720杰然不同","content":"回复 q939864646 ：要不你重新预定个吧","type":0},{"author":"q939864646","content":"回复 720杰然不同 :不用了 楼主我知道你是故意的 939864646我扣","type":0},{"author":"720杰然不同","content":"回复 q939864646 ：臭不要脸","type":0},{"author":"q939864646","content":"回复 720杰然不同 : 呢算了 当我没说","type":0}],"content":"我要77楼","mainTopic":"回复：【游戏】没男票没女票的速速来啊","source":"网红蒙蒙","type":0,"url":"http://tieba.baidu.com/p/3238083022?pn=3"}'
    pprint.pprint(s)


def tmp10():
    print(unquote('http://tieba.baidu.com/f/fdir?fd=%C9%FA%BB%EE&sd=%D0%DD%CF%D0%BB%EE%B6%AF', encoding='gbk'))


def tmp9():
    # s= "['c595a6d8a71a11e699b6cc3d827a2960', 'c595f4f8a71a11e6a981cc3d827a2960', 'c5961c0aa71a11e6bb79cc3d827a2960']"
    s = '["1", 2, 4]'
    r = json.loads(s)
    print(r)


def tmp8():
    # fw = open('C:\\Users\\BaoQiang\\Desktop\\test.txt','wb',encoding='utf-8')
    a = [1, 2, 3, '你']
    fw = open('C:\\Users\\BaoQiang\\Desktop\\test.txt', 'wb')
    for i in range(5):
        # fw.write("好".encodea('gbk').decode('gbk'))
        # fw.write("好".encode('utf-8'))
        fw.write(a)
    fw.close()


def tmp7():
    s = '''familynames=\u8D75||\u94B1||\u5B59||\u674E||\u5468||\u5434||\u90D1||\u738B||\u51AF||\u9648||\u891A||\u536B||\u848B||\u6C88||\u97E9||\u6768||\u6731||\u79E6||\u5C24||\u8BB8||\u4F55||\u5415||\u65BD||\u5F20||\u5B54||\u66F9||\u4E25||\u534E||\u91D1||\u9B4F||\u9676||\u59DC||\u621A||\u8C22||\u90B9||\u55BB||\u67CF||\u6C34||\u7AA6||\u7AE0||\u4E91||\u82CF||\u6F58||\u845B||\u595A||\u8303||\u5F6D||\u90CE||\u9C81||\u97E6||\u660C||\u9A6C||\u82D7||\u51E4||\u82B1||\u65B9||\u4FDE||\u4EFB||\u8881||\u67F3||\u9146||\u9C8D||\u53F2||\u5510||\u8D39||\u5EC9||\u5C91||\u859B||\u96F7||\u8D3A||\u502A||\u6C64||\u6ED5||\u6BB7||\u7F57||\u6BD5||\u90DD||\u90AC||\u5B89||\u5E38||\u4E50||\u4E8E||\u65F6||\u5085||\u76AE||\u535E||\u9F50||\u5EB7||\u4F0D||\u4F59||\u5143||\u535C||\u987E||\u5B5F||\u5E73||\u9EC4||\u7A46||\u8427||\u5C39||\u59DA||\u90B5||\u6E5B||\u6C6A||\u7941||\u6BDB||\u79B9||\u72C4||\u7C73||\u8D1D||\u660E||\u81E7||\u8BA1||\u4F0F||\u6210||\u6234||\u8C08||\u5B8B||\u8305||\u5E9E||\u718A||\u7EAA||\u8212||\u5C48||\u9879||\u795D||\u8463||\u6881||\u675C||\u962E||\u84DD||\u95F5||\u5E2D||\u5B63||\u9EBB||\u5F3A||\u8D3E||\u8DEF||\u5A04||\u5371||\u6C5F||\u7AE5||\u989C||\u90ED||\u6885||\u76DB||\u6797||\u5201||\u953A||\u5F90||\u90B1||\u9A86||\u9AD8||\u590F||\u8521||\u7530||\u6A0A||\u80E1||\u51CC||\u970D||\u865E||\u4E07||\u652F||\u67EF||\u661D||\u7BA1||\u5362||\u83AB||\u7ECF||\u623F||\u88D8||\u7F2A||\u5E72||\u89E3||\u5E94||\u5B97||\u4E01||\u5BA3||\u8D32||\u9093||\u90C1||\u5355||\u676D||\u6D2A||\u5305||\u8BF8||\u5DE6||\u77F3||\u5D14||\u5409||\u94AE||\u9F9A||\u7A0B||\u5D47||\u90A2||\u6ED1||\u88F4||\u9646||\u8363||\u7FC1||\u8340||\u7F8A||\u65BC||\u60E0||\u7504||\u9EB4||\u5BB6||\u5C01||\u82AE||\u7FBF||\u50A8||\u9773||\u6C72||\u90B4||\u7CDC||\u677E||\u4E95||\u6BB5||\u5BCC||\u5DEB||\u4E4C||\u7126||\u5DF4||\u5F13||\u7267||\u9697||\u5C71||\u8C37||\u8F66||\u4FAF||\u5B93||\u84EC||\u5168||\u90D7||\u73ED||\u4EF0||\u79CB||\u4EF2||\u4F0A||\u5BAB||\u5B81||\u4EC7||\u683E||\u66B4||\u7518||\u94AD||\u5386||\u620E||\u7956||\u6B66||\u7B26||\u5218||\u666F||\u8A79||\u675F||\u9F99||\u53F6||\u5E78||\u53F8||\u97F6||\u90DC||\u9ECE||\u84DF||\u6EA5||\u5370||\u5BBF||\u767D||\u6000||\u84B2||\u90B0||\u4ECE||\u9102||\u7D22||\u54B8||\u7C4D||\u8D56||\u5353||\u853A||\u5C60||\u8499||\u6C60||\u4E54||\u9633||\u90C1||\u80E5||\u80FD||\u82CD||\u53CC||\u95FB||\u8398||\u515A||\u7FDF||\u8C2D||\u8D21||\u52B3||\u9004||\u59EC||\u7533||\u6276||\u5835||\u5189||\u5BB0||\u90E6||\u96CD||\u6851||\u6842||\u6FEE||\u725B||\u8FB9||\u6248||\u71D5||\u5180||\u50EA||\u6D66||\u5C1A||\u519C||\u6E29||\u522B||\u5E84||\u664F||\u67F4||\u77BF||\u960E||\u5145||\u6155||\u8339||\u4E60||\u5BA6||\u827E||\u9C7C||\u5BB9||\u5411||\u53E4||\u6613||\u614E||\u6208||\u5ED6||\u5EBE||\u7EC8||\u66A8||\u5C45||\u8861||\u6B65||\u803F||\u6EE1||\u5F18||\u6587||\u5BC7||\u7984||\u9619||\u6B27||\u5DE9||\u8042||\u6641||\u6556||\u878D||\u51B7||\u8A3E||\u8F9B||\u961A||\u90A3||\u7B80||\u9976||\u7A7A||\u66FE||\u6C99||\u97A0||\u5173||\u84AF||\u76F8||\u6E38||\u516C||\u4E07\u4FDF||\u53F8\u9A6C||\u4E0A\u5B98||\u6B27\u9633||\u590F\u4FAF||\u8BF8\u845B||\u95FB\u4EBA||\u4E1C\u65B9||\u8D6B\u8FDE||\u7687\u752B||\u5C09\u8FDF||\u516C\u7F8A||\u6FB9\u53F0||\u516C\u51B6||\u5B97\u653F||\u6FEE\u9633||\u6DF3\u4E8E||\u5355\u4E8E||\u592A\u53D4||\u7533\u5C60||\u516C\u5B59||\u4EF2\u5B59||\u8F69\u8F95||\u4EE4\u72D0||\u949F\u79BB||\u5B87\u6587||\u957F\u5B59||\u6155\u5BB9||\u53F8\u5F92||\u53F8\u7A7A||\u821C||\u53F6\u8D6B\u90A3\u62C9||\u4E1B||\u5CB3||\u7687||\u8D6B||\u5178||\u7AE0\u4F73||\u90A3\u62C9||\u51A0||\u5BBE||\u9999||\u679C||\u4F9D\u5C14\u6839\u89C9\u7F57||\u4F9D\u5C14\u89C9\u7F57||\u8428\u561B\u5587||\u8D6B\u820D\u91CC||\u989D\u5C14\u5FB7\u7279||\u8428\u514B\u8FBE||\u94AE\u795C\u7984||\u4ED6\u5854\u5587||\u559C\u5854\u814A||\u8BB7\u6BB7\u5BCC\u5BDF||\u53F6\u8D6B\u90A3\u5170||\u5E93\u96C5\u5587||\u74DC\u5C14\u4F73||\u8212\u7A46\u7984||\u7231\u65B0\u89C9\u7F57||\u7D22\u7EF0\u7EDC||\u7EB3\u5587||\u4E4C\u96C5||\u8303\u59DC||\u78A7\u9C81||\u5F20\u5ED6||\u5F20\u7B80||\u56FE\u95E8||\u592A\u53F2||\u516C\u53D4||\u4E4C\u5B59||\u5B8C\u989C||\u9A6C\u4F73||\u4F5F\u4F73||\u5BCC\u5BDF||\u8D39\u83AB||\u8E47||\u6492||\u51BC||\u6D82||\u8096||\u963F||\u82DF
mewords=\u54C0\u5BB6||\u4FFA||\u5351\u804C||\u672C\u5E9C||\u672C\u5BAB||\u672C\u5B98||\u672C\u4EBA||\u672C\u5E05||\u672C\u738B||\u672C\u5EA7||\u9119\u4EBA||\u4E0D\u624D||\u81E3||\u81E3\u59BE||\u5927\u7237||\u5B64||\u5B64\u5BB6||\u5BE1\u4EBA||\u8D31\u59BE||\u8001\u9053||\u8001\u592B||\u8001\u7EB3||\u8001\u50E7||\u8001\u5B50||\u8001\u8872||\u5974\u5BB6||\u5974\u5A62||\u8D2B\u9053||\u8D2B\u5C3C||\u8D2B\u50E7||\u6D12\u5BB6||\u5C71\u4EBA||\u79C1||\u665A\u8F88||\u5FAE\u81E3||\u4E3A\u7236||\u4E3A\u59BB||\u4E3A\u5144||\u4E3A\u59BE||\u6211||\u543E||\u5C0F\u9053||\u5C0F\u7684||\u5C0F\u5F1F||\u5C0F\u5B98||\u5C0F\u53EF||\u5C0F\u5974||\u5C0F\u4EBA||\u5C0F\u50E7||\u5C0F\u58F0||\u5C0F\u751F||\u5C0F\u5B50||\u7237||\u4E88||\u5728\u4E0B||\u54B1||\u54B1\u5BB6||\u59BE\u8EAB||\u6715
youwords=\u60A8||\u4F60||\u541B||\u8DB3\u4E0B||\u9601\u4E0B||\u540C\u5FD7||\u540C\u5B66'''
    print(s)


def tmp6():
    p = re.compile('kw=(.*)')
    url = 'http://tieba.baidu.com/f?kw=你好'
    m = p.search(url)
    if m:
        print(m.group(1))


def tmp5():
    print(datetime.datetime.now())


def tmp4():
    a = 1.234
    print(round(a, 2))


def tmp3():
    print(FILE_PATH)


def tmp2():
    print(sys.path)
    print(os.sys.path)


def tmp1():
    row = np.array([0, 0, 1, 3, 1, 0, 0])
    col = np.array([0, 2, 1, 3, 1, 0, 0])
    data = np.array([1, 1, 1, 1, 1, 1, 1])

    matrix = csr_matrix((data, (row, col)), shape=(4, 4)).todense()
    print(matrix)
    for i in np.array(matrix[1,]):
        print(i)


if __name__ == '__main__':
    tmp()
