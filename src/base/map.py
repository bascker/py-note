#!/usr/bin/python
"""
map 语法:  map(function, list), 将集合元素映射成另一种值
2.x:    返回列表
3.x:    返回迭代器
"""

import os
import sys

sys.path.append(os.getcwd())

from src.utils.applogger import AppLogger

LOG = AppLogger("map")

def main():
    num = [1, 2, 3]
    vals = map(lambda n: n * 2, num)
    # list 兼容 python2/3x 处理
    double_num = list(vals)
    LOG.info("vals: %s, type: %s" % (vals, type(vals)))
    LOG.info("double_num: %s" % double_num)


if __name__ == '__main__':
    main()
