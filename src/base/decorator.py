#!/usr/bin/python
'''
装饰器 decorator 的使用: 函数方式定义装饰器
@author bascker
'''
import os
import sys
sys.path.append(os.getcwd())

from functools import wraps
from src.utils.applogger import AppLogger

LOG = AppLogger("decorator.py")


def log_start_end(func):
    """
    不带参数的装饰器
    """
    # 使用 functools.wraps(function), 复制函数名称、注释文档等给注释的函数
    @wraps(func)
    def decorated(*args, **kwargs):
        LOG.debug("function %s start" % func.__name__)
        val = func(*args, **kwargs)
        LOG.debug("function %s end" % func.__name__)
        return val

    return decorated


def log(level=AppLogger.DEBUG):
    """
    带参数的装饰器
    """
    global LOG
    LOG = AppLogger("decorator.py", level=level)
    return log_start_end


@log_start_end
def hello():
    print("hello decorator")


@log(level=AppLogger.INFO)
def hello_info():
    print("hello_info decorator")


def main():
    hello()
    assert "hello" == hello.__name__

    hello_info()


if __name__ == '__main__':
    main()
