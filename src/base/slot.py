#!/usr/bin/python
"""
__slots__ 的使用
@author bascker
"""

class User(object):

    # 已知 User 有哪些属性，通过 __slots__ 来固定分配内存
    # 告知 python 使用固定长度的集合保存实例的属性
    __slots__ = ['name', 'age', 'sex']

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
