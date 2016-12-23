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
@file: vec_svr.py
@time: 2016/10/31 23:17
"""
import gensim
from xiaolearn.util import timer
from flask import Flask
from xiaolearn.util.settings import *
import logging
from flask import request
import json

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
model = None


@timer.log_time
def load_model():
    # use model file
    # return gensim.models.Word2Vec.load("file/zh_wiki_vectors.model")

    # use vec bin file
    return gensim.models.Word2Vec.load_word2vec_format(FILE_PATH + 'myword2vec/zh_wiki_vectors.bin', binary=True)

    # return None


@app.route('/vec', methods=['POST'])
def word_to_vec():
    word = request.form.get('word')
    res = word2vec(word)
    r = {}
    if res:
        r["code"] = 0
        r["vec"] = res
        r["msg"] = "succeed"
    else:
        r["code"] = -1
        r["vec"] = ""
        r["msg"] = 'sorry, no word {{{}}} was found in dic'.format(word)

    return app.make_response((json.dumps(r), 200))


# @app.route('/vec/<word>',method=['GET'])
def word2vec(word):
    if not word:
        return

    logging.info("user req word: " + word)
    # return ['你',"我"]

    try:
        res = model.most_similar(word)
    except:
        res = None
    # res = [["test", 0.8]]
    l = []
    d = {}
    # d["word"] = word
    # d["score"] = 1
    l.append(word)

    if res:
        for item in res:
            d = {}
            # d["word"] = item[0]
            # d["score"] = round(item[1],3)
            l.append(item[0])

            if len(l) == 11:
                break

    logging.info("response: {}".format(l))

    return l


@app.route('/')
def index():
    return "app run"


if __name__ == '__main__':
    model = load_model()
    app.run()

    # res = word_to_vec()
    # print(res.content)
