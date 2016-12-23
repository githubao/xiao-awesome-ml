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
@file: dialog.py
@time: 2016/11/8 17:48
"""
import json
import traceback

from sqlprocess.sql_section import MySqlModule
from xiaolearn.util.settings import FILE_PATH

CHAT_FILE = FILE_PATH + '/tieba/chat.txt'
fw = open(CHAT_FILE, 'w', encoding='utf-8')
mysql = MySqlModule()


def get_chat1(reply_to_id, chat):
    sql = 'select id,content from tieba_content where reply_to = {}'.format(reply_to_id)

    data = mysql.select(sql)
    if not data:
        fw.write('{}\n'.format(chat))
        fw.write('{}\n'.format('*' * 30))
        return

    for item in data:
        if chat:
            fw.write('{}\n'.format(chat))
        get_chat1(item[0], item[1])


def get_chat(lines):
    if lines:
        sql = 'select relation from tieba_relationship where line_num in ("{}")'.format('","'.join(lines))
        sub_sql = 'select uuid,content,processed,features,url from tieba_content where line_num in ("{}")'.format('","'.join(lines))
    else:
        sql = 'select relation from tieba_relationship'
        sub_sql = 'select uuid,content,processed,features,url from tieba_content'

    data = mysql.select(sql)
    if not data:
        return

    content = mysql.select(sub_sql)
    d = {}
    for item in content:
        d[item[0]] = item

    for item in data:
        uids = json.loads(item[0].replace('\'', '"'))
        url = ''
        try:
            for u in uids:
                if d[u][2]:
                    fw.write('{}[{}]\t{}\n'.format(d[u][1],d[u][2],d[u][3]))
                else:
                    fw.write('{}\t{}\n'.format(d[u][1],d[u][3]))

        except:
            traceback.print_exc()

        if len(uids):
            url = d[uids[0]][4]

        fw.write('{}\n'.format(url))
        fw.write('*' * 50 + '\n')

    fw.close()


def get_content():
    f = open("C:\\Users\\BaoQiang\\Desktop\\content.txt", "w", encoding="utf-8")
    sql = 'select id,content from tieba_content;'
    data = mysql.select(sql)
    for single in data:
        f.write('{}\t{}\n'.format(single[0], single[1]))

    fw.close()


if __name__ == '__main__':
    # s = 'test[1]'
    lines = open("C:\\Users\\BaoQiang\\Desktop\\line_num.txt").readlines()
    lines = [line.strip('\n') for line in lines]
    get_chat(lines)

    # get_content()
