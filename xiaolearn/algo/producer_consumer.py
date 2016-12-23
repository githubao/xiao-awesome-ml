#!/usr/bin/env python
# encoding: utf-8



"""
@description: 队列 生产者和消费者

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: producer_consumer.py
@time: 2016/11/21 21:44
"""

import queue
import threading
import random

write_lock = threading.Lock()

class Producer(threading.Thread):
    def __init__(self,q,con,name):
        super().__init__()
        self.q = q
        self.name = name
        self.con = con
        print('Producer {my.name} Started'.format(my=self))

    def run(self):
        while 1:
            global write_lock
            self.con.acquire()
            if self.q.full():
                with write_lock:
                    print('Queue is full, producer wait!')
                self.con.wait()
            else:
                value = random.randint(0,10)
                with write_lock:
                    print('{my.name} put value {0} into queue'.format(value,my=self))

                self.q.put(self.name +':'+str(value))
                self.con.notify()
            self.con.release()

class Consumer(threading.Thread):
    def __init__(self,q,con,name):
        super().__init__()
        self.q = q
        self.name = name
        self.con = con
        print('Consumer {my.name} Started'.format(my=self))

    def run(self):
        while 1:
            global write_lock
            self.con.acquire()
            if self.q.empty():
                with write_lock:
                    print('Queue is empty, consumer wait!')
                self.con.wait()
            else:
                value = self.q.get()
                with write_lock:
                    print('{my.name} get value {0} from queue'.format(value,my=self))

                self.con.notify()
            self.con.release()



def main():
    q = queue.Queue(10)
    con = threading.Condition()
    p1 = Producer(q,con,'P1')
    p1.start()
    p2 = Producer(q,con,'P2')
    p2.start()
    c1 = Consumer(q,con,'C1')
    c1.start()


if __name__ == '__main__':
    main()

