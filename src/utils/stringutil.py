# -*- coding: utf-8 -*-
'''
字符串工具类
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