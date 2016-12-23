#!/usr/bin/env python
# encoding: utf-8

"""
@description: 从爬取的贴吧数据中，获取单轮的qa对话的结果

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: single_qa.py
@time: 2016/12/7 13:37
"""

import re
import traceback

from xiaolearn.sqlprocess.mysqlite import SqlLite
from xiaolearn.test import *

# OUT_FILE = FILE_PATH + 'sqlprocess/raw_corpus.txt'

TIEBA_URL = 'http://tieba.baidu.com/p/'


def process_demo():
    IIN_FILE = sys.argv[1]
    OUT_FILE = sys.argv[2]
    fw = open(OUT_FILE, 'w', encoding='utf-8')

    my_sql = SqlLite(IIN_FILE)

    # sql = 'select id,pid,content,reply,time from comment WHERE pid = 100066338427'
    # sql = 'select id,pid,content,reply,time from comment ORDER by random() limit 5000'
    # sql = 'select id,pid,content,reply,time from comment limit 10000'
    sql = 'select id,pid,content,reply,time from comment ORDER by random() limit 10000'
    # sql = 'select id,pid,content,reply,time from comment'
    replys = my_sql.get_sql(sql)

    cnt = 0
    dic = {}
    for item in replys:
        cnt += 1

        (cid, pid, answer, reply, time) = item

        if not reply:
            reply = get_reply(answer)

        # 这时候，把楼层的数据作为回复
        if not reply:
            sub_sql = 'select tid,post_no,content,author from post where id = {} limit 1'.format(pid)
        else:
            sub_sql = 'select t2.tid,t2.post_no,t1.content,t1.reply from comment as t1, post as t2 WHERE pid={} and t1.author="{}" and t1.time<"{}" and t1.pid = t2.id order by t1.time desc limit 1;'.format(
                    pid, reply, time)

        try:
            sub_data = my_sql.get_sql(sub_sql)
            # print(sub_sql)
        except:
            traceback.print_exc()
            print(cid)
            print(sub_sql)
            continue

        if not sub_data:
            continue

        tid, post_no, question, ques_reply = sub_data[0]

        if not ques_reply:
            ques_reply = get_reply(question)

        try:
            question = rm_reply(rm_tag(question), ques_reply)
            answer = rm_reply(rm_tag(answer), reply)
        except:
            traceback.print_exc()
            continue

        if not question or not answer:
            continue

        line = '{}\t{}\t{}\t{}{}[{}]'.format(question, answer, 1, TIEBA_URL, tid, post_no)
        key = '{}\t{}'.format(question, answer)
        dic[key] = line

        if cnt % 1000 == 0:
            print('sql processing data: {}'.format(cnt))

    # 保存去重之后的数据
    idx = 1
    for key, value in dic.items():
        fw.write("{}\t{}\n".format(idx, value))
        idx += 1

    fw.close()
    my_sql.close()


def get_reply(reply):
    no_tag_reply = rm_tag(reply)
    no_tag_reply = no_tag_reply.strip()
    regex = '回复\s+(.+?)\s+[:|：]?'
    m = re.match(regex, no_tag_reply)
    return m.group(1) if m else None


def rm_tag(str):
    str = rm_face(str)
    str = re.sub(r'</?\w+[^>]*>', '', str)
    str = re.sub('\n', '', str)
    return str


def rm_face(str):
    str = re.sub('\[(clientface|face).+\]', '', str)
    return str


def rm_reply(str, author):
    pattern = '回复\s+{}\s+[:|：]?'.format(author)
    str = re.sub(pattern, '', str)
    str = str.strip()
    return str


def main():
    process_demo()


if __name__ == '__main__':
    main()
