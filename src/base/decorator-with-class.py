#!/usr/bin/python
'''
装饰器 decorator 的使用: 类方式定义装饰器
@author bascker
'''
import os
import sys
sys.path.append(os.getcwd())

from functools import wraps
from src.utils.applogger import AppLogger

class LogStartEnd(object):
    LOG = None

    def __init__(self, level=AppLogger.DEBUG):
        self.level = level
        global LOG
        LOG = AppLogger("decorator-with-class", level=self.level)

    def __call__(self, func):

        @wraps(func)
        def decorated(*args, **kwragrs):
            LOG.debug("function %s start" % func.__name__)
            val = func(*args, **kwragrs)
            LOG.debug("function %s end" % func.__name__)

            return val

        return decorated


@LogStartEnd(level=AppLogger.INFO)
def hello():
    print("hello decorator with class")


def main():
    hello()
    assert "hello" == hello.__name__


if __name__ == '__main__':
    main()
