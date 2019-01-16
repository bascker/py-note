# -*- coding=utf-8 -*-
# !/usr/bin/python

import Queue
import threading
import time


class WorkManager(object):

    def __init__(self, work_num=1000, thread_num=2):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.__init__work_queue(work_num)
        self.__init__thread_pool(thread_num)

    def __init__thread_pool(self, thread_num):
        '''初始化线程'''
        for i in xrange(thread_num):
            self.threads.append(Work(self.work_queue))

    def __init__work_queue(self, jobs_num):
        '''初始化工作队列'''
        for i in xrange(jobs_num):
            self.add_job(do_job, i)

    def add_job(self, func, *args):
        '''添加一项工作入队'''
        # 任务入队，Queue内部实现了同步机制
        self.work_queue.put((func, list(args)))

    def check_queue(self):
        '''检查剩余队列任务'''
        return self.work_queue.qsize()

    def wait_allcomplete(self):
        '''等待所有线程运行完毕'''
        for item in self.threads:
            if item.isAlive():
                item.join()


class Work(threading.Thread):

    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        # 死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
                # 任务异步出队，Queue内部实现了同步机制
                do, args = self.work_queue.get(block=False)
                do(args)
                # 通知系统任务完成
                self.work_queue.task_done()
            except Exception as e:
                print(str(e))
                break


def do_job(args):
    '''具体要做的任务'''
    print(args)
    time.sleep(0.1)  # 模拟处理时间
    print(threading.current_thread(), list(args))


if __name__ == '__main__':
    start = time.time()
    work_manager = WorkManager(10, 2)
    work_manager.wait_allcomplete()
    end = time.time()
    print("Cost all time: %s" % (end - start))