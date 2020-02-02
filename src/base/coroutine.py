#!/usr/bin/python
"""
协程（coroutine）的使用
@author bascker
"""
import os
import sys

sys.path.append(os.getcwd())

from src.utils.applogger import AppLogger

LOG = AppLogger("coroutine.py")


def contain(string):
    """
    协程接受的字符串，是否包含 string
    @param string
    """
    LOG.info("contain for string: %s" % string)
    while True:
        # 获取一个协程
        line = (yield)
        LOG.info('The line "%s" is contains string: %s' % (line, string in line))


def main():
    fn = contain("python")
    # 启动协程
    next(fn)

    # 发送字符串
    fn.send("hello world")
    fn.send("hello python")

    # 关闭协程
    fn.close()


if __name__ == '__main__':
    main()
