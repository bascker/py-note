#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.utils.properties import Properties

def main():
    properties = Properties('file/db.properties')
    print("是否存在 name 属性：", properties.has_key("name"))
    print("获取默认值：", properties.get("name", "lisa"))
    print("所有 key 值: ", properties.keys())
    print("所有 value 值: ", properties.values())

    for k, v in properties.items():
        print("key = {}, value = {}".format(k, v))

if __name__ == '__main__':
    main()