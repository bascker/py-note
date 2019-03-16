# -*- coding: utf-8 -*-
'''
字符串工具类

1、常用方法
    1.1 find(): 查找匹配的字串，并返回字串所在位置最左端的索引。找不到，则返回 -1
    1.2 join(): 字符串连接, 用于连接序列中的元素。与 split() 是逆方法
    1.3 lower(): 转小写
    1.4 replace(): 字符串替换
    1.5 split():  字符串分割成序列。默认按空格分割
    1.6 strip(): 去除字符串两侧的空格
'''


def to_str(value):
    return repr(value)


def is_valid_str(string):
    return isinstance(string, str)


def to_lower(string):
    if is_valid_str(string):
        return string.lower()


def to_upper(string):
    if is_valid_str(string):
        return string.upper()


def substr(string, start=0, end=0):
    if is_valid_str(string):
        return string[start:] if start == end else string[start:end]