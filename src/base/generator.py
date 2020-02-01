#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
生成器 generator
@author bascker
"""
import os
import sys
# 用于引入自定义模块: 若当前目录查不到，则 import 模块从 sys.path 找
sys.path.append(os.getcwd())

from src.utils.applogger import AppLogger

LOG = AppLogger("generator")


def main():

    febon = _febon(4)
    # 使用 next() 获取序列下一个元素
    assert 1 == next(febon)
    assert 1 == next(febon)
    assert 2 == next(febon)
    assert 3 == next(febon)
    try:
        next(febon)
    except Exception as e:
        # 超出个数后，跑次 StopIteration 异常
        LOG.error("StopIteration")


def _febon(n):
    '''
    斐波那契数列
    f(n) {
        n <= 2,   return 1
        n >  2,   return f(n - 1) + f(n - 2)
    }
    '''
    a = b = 1
    for i in range(n):
        # 返回 a
        yield a
        # a = b,  b = a + b
        a, b = b, a + b


if __name__ == '__main__':
    main()
