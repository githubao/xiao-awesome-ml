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
@file: filter_module.py
@time: 2016/11/7 17:46
"""
import json
import logging
import re
import uuid
from datetime import datetime

from sqlprocess.sql_section import MySqlModule
from xiaolearn.util.settings import TIME_FORMAT

logging.basicConfig(level=logging.INFO)

tiebas = {}


def _get_all_tiebas():
    sql = 'select id,tieba from tieba_name'
    data = MySqlModule().select(sql)
    for item in data:
        tiebas[item[1]] = int(item[0])


class FilterModule():
    # _get_all_tiebas()

    def __init__(self, file_name, which_line):
        self.mysql = MySqlModule()

        self.line_num = '{}[{}]'.format(file_name, which_line)
        self.tieba_name = ""
        self.features = '0' * 16

        self.dialogs = []

        self.contents = []
        self.relations = []

    def process_data(self, line):
        if not line:
            return
        line = line.replace('\n', '')

        try:
            data = json.loads(line)
        except:
            logging.info('err parse data: {}'.format(line))
            data = None

        if not data:
            return

        # 存储贴吧的名称，用于后面保存对话数据
        self.tieba_name = data["source"]
        self.url = data["url"]
        self.main_topic = data["mainTopic"]

        json_data = {}
        json_data['content'] = data['content']
        json_data['to'] = ''
        json_data['author'] = data['author']
        json_data['uuid'] = uuid.uuid1().hex
        self.dialogs.append(json_data)

        comments = data['comments']
        if not comments:
            return

        for comment in comments:
            json_data = {}

            chat = comment['content'].replace('"', '\\"')
            json_data['author'] = comment['author']

            reply_to = self._get_reply(chat)
            reply_contains = self._contains_reply(chat)
            if reply_to:
                json_data['content'] = reply_to[0].replace('"', '\\"')
                json_data['to'] = reply_to[1]
                json_data['uuid'] = uuid.uuid1().hex
            elif reply_contains:
                # 如果包含回复的字眼，但是没有找到回复的人，这种数据，我们直接舍弃不要
                continue
            else:
                json_data['content'] = chat
                json_data['to'] = ''
                json_data['uuid'] = uuid.uuid1().hex
            # 把当前对话加入列表
            self.dialogs.append(json_data)

            # with open(FILE_PATH + '/tieba/process.txt', 'a', encoding='utf-8') as fw:
            #     fw.write("{}\n".format(self.dialogs))

    def format_sql(self):
        if not self.dialogs:
            return

        start_content = self.dialogs[0]['content']
        start_author = self.dialogs[0]['author']
        start_uuid = self.dialogs[0]['uuid']

        content = [start_uuid, start_content]
        self.contents.append(content)

        for i in range(len(self.dialogs)):
            # 第一句话
            if i == 0:
                continue

            content = self.dialogs[i]["content"]
            author = self.dialogs[i]['author']
            to = self.dialogs[i]["to"]
            current_uuid = self.dialogs[i]["uuid"]

            # 添加对话数据
            item = [current_uuid, content]
            self.contents.append(item)

            # 添加对话关系
            if to:
                reply = False
                for r in self.relations:
                    if r['end']:
                        continue

                    last_from = r['from']
                    last_to = r['to']

                    # 这时候是正常的对话
                    if last_from == to and last_to == author:
                        l = r['relation']
                        l.append(current_uuid)
                        r['relation'] = l
                        r['from'] = last_to
                        r['to'] = last_from

                        reply = True
                        break

                    # 这时候是有多个重复的对应的b->a的情况,这种把上面的标记为end
                    elif last_from == author and last_to == to:
                        r['end'] = True

                        # 同时添加新一轮的对话关系
                        # l = [current_uuid]
                        # self.relations.append({'relation': l, 'from': author, 'to': to,'end':False})
                        # reply = True
                        break

                        # 这时候是类似“A回复B”，但是上面没有“B回复A”形式的对话

                # 还有一种情况，是B说了一句话，没有回复，但是下面有“C回复B”
                if not reply and to:
                    for j in range(i)[::-1]:
                        last_to = self.dialogs[j]["to"]
                        last_author = self.dialogs[j]['author']
                        if not last_to and last_author == to:
                            l = [self.dialogs[j]['uuid'], current_uuid]
                            self.relations.append({'relation': l, 'from': author, 'to': last_author, 'end': False})
                            break

            # 这时候是没有to的时候
            else:
                # 如果这时候是用户自己说的话，这种数据目前不处理
                if author == start_author:
                    continue

                # 如果relation里面有a和b的对话，而且不是end，这种也不处理
                for r in self.relations:
                    if r['end']:
                        continue

                    last_from = r['from']
                    last_to = r['to']

                    if author in [last_to, last_from]:
                        continue

                l = [self.dialogs[0]['uuid'], current_uuid]
                self.relations.append({'relation': l, 'from': author, 'to': start_author, 'end': False})

    def print_sql(self):
        print(self.contents)
        print(self.relations)
        print("*" * 50)

    def save_sql(self):
        if not self.dialogs:
            return

        # tieba_id = self._get_tieba_id()
        tieba_name = self.tieba_name

        values = []
        current = datetime.now().strftime(TIME_FORMAT)
        sql = 'insert into tieba_content(tieba_name,uuid,content,features,main_topic,line_num,url,time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
        for item in self.contents:
            value = (tieba_name, item[0], item[1], self.features, self.main_topic, self.line_num, self.url, current)
            # mainTopic 只存储一次就好了
            # self.main_topic = ''
            values.append(value)

        success = self.mysql.insertmany(sql, values)

        logging.info('insert {{{}}} content lines'.format(success))
        self.mysql.commit()

        sql2 = 'insert into tieba_relationship(relation,line_num,time) VALUES (%s,%s,%s)'
        values.clear()
        for item in self.relations:
            # 只有一轮对话关系的这种，不要
            # if len(item["relation"]) == 1:
            #     continue

            value = (str(item["relation"]), self.line_num, current)
            values.append(value)

            # if len(values) > 200:
            #     success = mysql.insertmany(sql2, values)
            #     values.clear()


        success = self.mysql.insertmany(sql2, values)
        logging.info('insert {{{}}} relation lines'.format(success))
        self.mysql.commit()

    def clear(self):
        self.dialogs.clear()

    # 判断回复是哪种类型
    def _get_reply(self, content):
        if not content:
            return

        for dialog in self.dialogs:
            author = dialog['author']
            left = re.sub('回复\s?{}\s?(:|：)'.format(author), "", content)
            if left != content:
                return left, author

    def _contains_reply(self, content):
        if not content:
            return

        left = re.sub('回复(.*)(:|：)', "", content)
        if left != content:
            return True
        return False

    # 获取贴吧的id
    def _get_tieba_id(self):
        return tiebas[self.tieba_name] if self.tieba_name in tiebas else 0

