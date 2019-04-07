#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Properties 文件工具类
'''


COMMENT = '#'
EQUAL = '='

class Properties:

    def __init__(self, filename):
        self.filename = filename
        self.properties = self.__load()

    def __load(self):
        '''
        加载 Properties 文件
        :return:
        '''
        properties = {}
        try:
            file = open(self.filename, 'r')
            for line in file.readlines():
                line = line.strip()             # 去除换行符
                if not line.startswith(COMMENT) and line.find(EQUAL):
                    data = line.split(EQUAL)
                    key = data[0].strip()
                    value = data[1].strip()
                    properties[key] = value
        except Exception as e:
            raise e
        else:
            file.close()

        return properties

    def has_key(self, key):
        return key in self.properties

    def get(self, key, default_value=''):
        return self.properties.get(key, default_value)

    def keys(self):
        return self.properties.keys()

    def values(self):
        return self.properties.values()

    def items(self):
        return self.properties.items()