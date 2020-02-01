#!/usr/bin/python
'''
filter 语法: filter(function, list)
'''
import os
import sys

sys.path.append(os.getcwd())

from src.utils.applogger import AppLogger

LOG = AppLogger("filter")


def main():
    num = [1, 2, 3]
    result = list(filter(lambda x: x % 2 == 1, num))
    LOG.info("org num: %s" % num)
    LOG.info("rs num: %s" % result)


if __name__ == '__main__':
    main()
